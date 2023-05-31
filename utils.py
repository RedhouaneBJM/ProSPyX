#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 11:13:44 2023

@author: boudjehe
"""



import numpy as np
from scipy import ndimage as ndi
from skimage.restoration import unwrap_phase
from skimage.registration import phase_cross_correlation
from skimage.transform import rescale  # , resize, downscale_local_mean
import matplotlib.pyplot as plt
import matplotlib.path as mplPath
import sys
import glob
import os
from skimage.transform import rescale,resize
from scipy import ndimage as ndi
from matplotlib_scalebar.scalebar import ScaleBar
from PyQt5.QtCore import QCoreApplication, QObject, QThread, pyqtSignal, pyqtSlot
import roipoly
import shutil
import math
import h5py
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
def progbar(curr, total, textstr=""):
    """
    Create a progress bar for for-loops. 

    Parameters
    ----------
    curr : int
        Current value to shown in the progress bar
    total : int
        Maximum size of the progress bar.         
    textstr : str
        String to be shown at the right side of the progress bar
    """
    termwidth, termheight = shutil.get_terminal_size()
    full_progbar = int(math.ceil(termwidth / 2))
    # ~ full_progbar = termwidth - len(textstr) - 2 # some margin
    frac = curr / total
    filled_progbar = round(frac * full_progbar)
    textbar = "#" * filled_progbar + "-" * (full_progbar - filled_progbar)
    textperc = "[{:>7.2%}]".format(frac)
    print("\r", textbar, textperc, textstr, end="")

def rmlinearphase(image, mask):
    """
    Removes linear phase from object

    Parameters
    ----------
    image : array_like
        Input image
    mask : bool
        Boolean array with ones where the linear phase should be
        computed from

    Returns
    -------
    im_output : array_like
        Linear ramp corrected image
    """

    ph = np.exp(1j * np.angle(image))
    [gx, gy] = np.gradient(ph)
    gx = -np.real(1j * gx / ph)
    gy = -np.real(1j * gy / ph)

    nrm = mask.sum()
    agx = (gx * mask).sum() / nrm
    agy = (gy * mask).sum() / nrm

    (xx, yy) = np.indices(image.shape)
    p = np.exp(-1j * (agx * xx + agy * yy))  # ramp
    ph_corr = ph * p  # correcting ramp
    # taking the mask into account
    ph_corr *= np.conj((ph_corr * mask).sum() / nrm)

    # applying to the image
    im_output = np.abs(image) * ph_corr
    # ph_err = (mask * np.angle(ph_corr) ** 2).sum() / nrm

    return im_output  # , ph_err


def interp_spectral(img_e, ps_e, energy, img_ehigh, ps_high, ehigh):
    """
    Inteporlate the pixel size of input image accordingly to the highest energy
    """
    print(f"\nEnergy of {energy:.04f} keV")
    if energy == ehigh:
        print(f"This is the highest energy. No needs for interpolation")
        interp_img = img_e.copy()
    else:
        scalefactor = (ehigh/energy)  # scaling factor
        newps_e = ps_e/scalefactor  # new pixel size
        highshape = img_ehigh.shape
        print(f"New pixel size: {newps_e:.04e} nm (Old value: {ps_e:.04e} nm)")
        print(
            f"Pixel size is {ps_high:.04e}nm at the highest energy of {ehigh:.04f} keV")
        print(f"Rescaling the image at the energy {energy:.04f} keV")
        interp_img = rescale(img_e, 1/scalefactor, anti_aliasing=False)
        if interp_img.shape == highshape:
            print("Same shape, no need for padding/cropping")
        else:
            print(f"Old shape {interp_img.shape}")
            print(f"Padding/cropping image to new array shape")
            interp_img = pad_crop(interp_img, highshape)
            print(
                f"New interp shape {interp_img.shape} (high energy value {highshape})")
    return interp_img


def pad_crop(img, newshape):
    """
    Pad or crop images
    """
    oldshape = img.shape
    dr = (newshape[0]-oldshape[0])
    # print(f"dr={dr}")
    paddr = int(dr/2)
    dc = (newshape[1]-oldshape[1])
    # print(f"dr={dc}")
    paddc = int(dc/2)

    outimg = img.copy()

    # padding/cropping rows
    if dr > 0:
        outimg = np.pad(outimg, ((paddr, dr-paddr), (0, 0)))
    elif dr < 0:
        outimg = outimg[paddr, -(dr-paddr)]
    else:
        print("No changes in the number of rows")

    # padding/cropping columns
    if dc > 0:
        outimg = np.pad(outimg, ((0, 0), (paddc, dc-paddc)))
    elif dc < 0:
        outimg = outimg[paddc, -(dc-paddc)]
    else:
        print("No changes in the number of cols")

    return outimg


def unwrapping_phase(imgin, mask):
    """
    Unwrap phase
    """
    #print("\nUnwrapping phase")
    unwrapimg = unwrap_phase(imgin)
    if np.any(mask == True):
        #print('Correcting for air/vacuum regions')
        vals = unwrapimg[np.where(mask == True)].mean()
        unwrapimg -= 2 * np.pi * np.round(vals / (2 * np.pi))
    return unwrapimg


def removing_phaseramp(imgin, mask):
    """
    Remove phase ramp
    """
    imgin = np.exp(1j * imgin).copy()
    # ~ corrimg = np.angle(remove_linearphase(imgin, mask, 100)).copy()
    corrimg = np.angle(rmlinearphase(imgin, mask)).copy()
    return corrimg


def shift_image(imgin, shift):
    """
    Shift the image according to shift using mode="grid-wrap"
    """
    return ndi.shift(imgin, shift=shift, mode="grid-wrap")


def convert_phase2delta(imgin, energy,dz):
    """
    Convert from phase shifts to integrated delta values
    
    """
    


        
    wavelen =  (12.4 / energy) * 1e-10
    factor = -wavelen / (2*np.pi*dz*1e-6)

    return imgin*factor, factor


def convert_to_beta(input_img,energy,dz,apply_log=True):
    """
    Converts the image gray-levels from amplitude to beta
    """
    wavelen =  (12.4 / energy) * 1e-10
    factor = wavelen / (2*np.pi*dz*1e-6)

    # In case the log has not yet been applied to the image
    if apply_log:
        input_img = np.log(input_img)
    return input_img * (-factor), factor

def get_thickness():
    
    while True:
        try:
            dz= float(input("Enter the thickness sample in micrometer: "))
            break  # exit loop if input is valid
            
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    return dz

    
def sort_array(input_array, ref_array):
    """
    Sort array based on another array

    Parameters
    ----------
    input_array : array_like
        Array to be sorted
    ref_array : array_like
        Array on which the sorting will be based

    Returns
    -------
    sorted_input_array : array_like
        Sorted input array
    sorted_ref_array : array_like
        Sorted reference array
    """
    idxsort = np.argsort(ref_array)
    sorted_ref_array = ref_array[idxsort]
    sorted_input_array = input_array[idxsort]

    return sorted_input_array, sorted_ref_array




class NavigationToolbar2QT(NavigationToolbar):
    
    #only display the buttons we need
    NavigationToolbar.toolitems =  (
     ('Home', 'Reset original view', 'home', 'home'),
     ('Back', 'Back to  previous view', 'back', 'back'),
     ('Forward', 'Forward to next view', 'forward', 'forward'),
     (None, None, None, None),
     ('Pan', 'Pan axes with left mouse, zoom with right', 'move', 'pan'),
     ('Zoom', 'Zoom to rectangle', 'zoom_to_rect', 'zoom'),
     (None, None, None, None),
     ('Subplots', 'Configure subplots', 'subplots', 'configure_subplots'),
     ('Customize', 'Edit axis, curve and image parameters', 'qt4_editor_options', 'edit_parameters'),
     ('Save', 'Save the figure', 'filesave', 'save_figure'),
     ('', 'Rotate the image', 'rotate', 'home')
     )
   
   
    def __init__(self, canvas, parent):
       
        
       NavigationToolbar.__init__(self, canvas, parent)




