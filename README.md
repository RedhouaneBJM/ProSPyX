<p style="text-align: center;">

# Introduction
ProSPyX is an open-source Python software, developed using PyQt5, suitable for fast processing of large X-ray spectral ptychography datasets. The software allows the user to perform constant and phase ramp removal, phase unwrapping, pixel interpolation, and alignment of phase contrast images directly and interactively through multiple buttons. In parallel, it processes the amplitude images of the complex transmittance function of the sample in a back-end manner. Once the post-processing step is complete, the user can perform contrast conversion and then extract both delta and beta spectra to check for the presence of the resonant chemical species within a defined region of interest.

A paper on ProSPyX has been published in the Journal of Synchrotron Radiation and can be downloaded from http://doi.org/10.1107/S160057752400016X.

# How to use it

## Download of the package
### Using the zip file
* Click on the green button labeled '_Code_' on the right-hand side.
* Click on '_Download ZIP_' option from the drop-down menu.
* Unzip '_ProSPyX-main_' file.
### Using Git
* Type on a terminal `git clone https://github.com/RedhouaneBJM/ProSPyX.git`

## Installation of the package
ProSPyX requires Python 3.9 or an older version.

Inside the created folder after downloading/clone github repository files open a terminal :
* Type `pip install -r requirements.txt`

#### Important Note

To ensure the proper functioning of the software, please create a virtual environment dedicated to ProSPyX to install the requirements to avoid any potential interference with already installed packages (`conda create --name your_env_name` if you have Anaconda installed. For non-anaconda users, `virtualenv your_env_name` if the package virtualenv is installed). Newer versions of dependencies might lead to deprecation warnings or even total crashes.
## Give it a try
* Download the dataset from `https://zenodo.org/records/10000776` or you can use your own dataset
* run with `python ProSPyX.py` from a terminal
* To import the data, go to the '_Data_' tab. First, enter the '_Prefix_' and validate it by pressing the enter key. After that, click on '_Browse_' to define the path where the data is stored
* A video tutorial demonstrating how to process X-ray spectral ptychography images using ProSPyX is available on YouTube at https://www.youtube.com/watch?v=l9P8i0mD_UA.

__Note__: if you want to use your dataset, there are some prior requirements regarding the main folder and subfolder names and how the data and metadata are stored inside the hierarchical data format (HDF) file. After the phase retrieval step, each ptychographic reconstruction should be stored in one HDF file with its metadata. Each file is saved separately inside a subfolder. All subfolders must be stored in a unique main folder. The name of all HDF files and subfolders must contain the same prefix which is unique to this dataset (you can download our dataset to get a better idea). The purpose of that is to be able to find and distinguish this data set. <br>
Below is an example of the structure of an HDF file. Regarding the name of HDF file, _xxx_ and _yyy_ are two different strings and may differ from one HDF file to another. _prefix_ must be the same for all HDF files as explained above.<br>
'_object_0_', '_dx_spec_' and '_energy_' refers to the complex transmittivity function of the sample, pixel size, and acquisition energy, respectively.

```
HDF5 "prefix_xxx_yyy.h5" {
GROUP "/" {
   GROUP "reconstruction" {
      GROUP "p" {
         DATASET "dx_spec" {
            DATATYPE  H5T_IEEE_F32LE
            DATASPACE  SIMPLE { ( 2, 1 ) / ( 2, 1 ) }
         }
         DATASET "energy" {
            DATATYPE  H5T_IEEE_F32LE
            DATASPACE  SIMPLE { ( 1, 1 ) / ( 1, 1 ) }
         }
         GROUP "objects" {
            DATASET "object_0" {
               DATATYPE  H5T_COMPOUND {
                  H5T_IEEE_F32LE "r";
                  H5T_IEEE_F32LE "i";
               }
               DATASPACE  SIMPLE { ( 930, 1076 ) / ( 930, 1076 ) }
            }
         }
      }
   }
}
}
```
</p>
