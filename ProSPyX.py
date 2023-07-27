# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'betaNL.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog,QApplication, QMainWindow, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton,QMessageBox
from PyQt5.QtGui import QDoubleValidator
from utils import *
import sys
import io

#import cairosvg




class InputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Input Dialog')
        self.input_label = QLabel('sample thickness in micron:', self)
        self.input_line_edit = QLineEdit(self)
        double_validator = QDoubleValidator(self)
        self.input_line_edit.setValidator(double_validator)
        
        self.ok_button = QPushButton('OK', self)
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button = QPushButton('Cancel', self)
        self.cancel_button.clicked.connect(self.reject)
        layout = QVBoxLayout(self)
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input_label)
        input_layout.addWidget(self.input_line_edit)
        layout.addLayout(input_layout)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)
        self.setModal(True)  # Set the dialog to modal
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        
        
        
        
    def getValue(self):
        # while True:
        #     if self.exec_() == QDialog.Accepted:
        #         try:
        #             value = float(self.input_line_edit.text())
        #             return value
        #         except ValueError:
        #             pass 
        if self.exec_() == QDialog.Accepted:

            value = (self.input_line_edit.text())
            if value =='':
                value=''
            else:
                
                value = float(value.replace(',', '.'))
            return value
  
class InputTextDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Input Dialog')
        self.input_label = QLabel('Suffix:', self)
        self.input_line_edit = QLineEdit(self)
        self.ok_button = QPushButton('OK', self)
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button = QPushButton('Cancel', self)
        self.cancel_button.clicked.connect(self.reject)
        layout = QVBoxLayout(self)
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input_label)
        input_layout.addWidget(self.input_line_edit)
        layout.addLayout(input_layout)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)
        self.setModal(True)  # Set the dialog to modal
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        
        
    def getText(self):
        while True:
            if self.exec_() == QDialog.Accepted:
                try:
                    value = (self.input_line_edit.text())
                    return value
                except ValueError:
                    pass 
class Ui_MainWindow(QMainWindow):
    params = dict()
    # -------------
    # Edit section
    # -------------
    params['path'] = None
    params['sufix'] = None
    params['vmin'] = -np.pi
    params['vmax'] = np.pi
    params['colormap'] = 'bone'  # "turbo", "nipy_spectral"
    params['crop'] = [100, -100, 100, 100]
    
    figure1 = plt.figure('before')
    figure2 = plt.figure('after')

    canvas1 = FigureCanvas(figure1)
    canvas2 = FigureCanvas(figure2)
    
    #Key variables
    contrast=0
    data_=0
    ROI_=0
    mask_=0
    add_mask_=0
    mask_all_=0
    load_mask_=0
    phase_amp=0
    var1=False
    x_i=[]
    y_i=[]
    use_shifts=0
    factor=[]
    #text=[]
    #text.append("Phase shift in radians")
    #text.append("Amplitude")
    ylabel_contrast=[]
    ylabel_contrast.append("Delta values")
    ylabel_contrast.append("Beta values")
    
    
    
    
    plt.close(fig='before')
    
    list_cmap=plt.colormaps()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1235, 928)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        
        self.toolbar1 = NavigationToolbar(self.canvas1, self)
        
        self.toolbar2 = NavigationToolbar(self.canvas2, self)
        
        ############################ EDITING TOOLBAR ###################
        
        self.toolbar1.actions()[10].setIcon(QtGui.QIcon('rotate.png'))
        self.toolbar1.actions()[10].triggered.connect(self.rotate)
        self.toolbar2.actions()[10].setIcon(QtGui.QIcon('rotate.png'))
        self.toolbar2.actions()[10].triggered.connect(self.rotate)
        

        ################################################################
        
        
        
        self.intInputValidation=QtGui.QIntValidator()
        self.DoubleInputValidation=QtGui.QDoubleValidator()
        
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.listofprojections = QtWidgets.QLabel(self.frame)
        self.listofprojections.setObjectName("listofprojections")
        self.gridLayout_15.addWidget(self.listofprojections, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_SaveProj = QtWidgets.QPushButton(self.frame)
        self.pushButton_SaveProj.setObjectName("pushButton_SaveProj")
        self.gridLayout.addWidget(self.pushButton_SaveProj, 1, 0, 1, 1)
        self.pushButton_SaveAllProj = QtWidgets.QPushButton(self.frame)
        self.pushButton_SaveAllProj.setObjectName("pushButton_SaveAllProj")
        self.gridLayout.addWidget(self.pushButton_SaveAllProj, 2, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        
        
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_15, 1, 0, 1, 1)
        self.gridLayout_16 = QtWidgets.QGridLayout()
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setObjectName("tabWidget")
        
        
        ##################### Add Qradio boutton ####################
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_path = QtWidgets.QLabel(self.tab)
        self.label_path.setObjectName("label_path")
        self.gridLayout_13.addWidget(self.label_path, 2, 0, 1, 1)
        self.Suffix = QtWidgets.QLabel(self.tab)
        self.Suffix.setObjectName("Suffix")
        self.gridLayout_13.addWidget(self.Suffix, 0, 0, 1, 1)
        self.lineEdit_Suffix = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_Suffix.setObjectName("lineEdit_Suffix")
        self.gridLayout_13.addWidget(self.lineEdit_Suffix, 0, 1, 1, 1)
        self.pushButton_browse = QtWidgets.QPushButton(self.tab)
        self.pushButton_browse.setObjectName("pushButton_browse")
        self.gridLayout_13.addWidget(self.pushButton_browse, 2, 1, 1, 1)

        
        
        
        
        
        self.radioButton_absorption = QtWidgets.QRadioButton("Amplitude", self.tab)
        self.radioButton_absorption.setObjectName("radioButton_absorption")
        self.gridLayout_13.addWidget(self.radioButton_absorption, 5, 1, 1, 1)
    
        self.radioButton_phase = QtWidgets.QRadioButton("Phase", self.tab)
        self.radioButton_phase.setObjectName("radioButton_phase")
        self.gridLayout_13.addWidget(self.radioButton_phase, 6, 1, 1, 1)
        self.radioButton_phase.setChecked(True)
            
        
        
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_13.addItem(spacerItem, 4, 0, 1, 2)
        self.gridLayout_14.addLayout(self.gridLayout_13, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        
        
        
        
        #############################################################
        
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pushButton_SaveMasks_ = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_SaveMasks_.setObjectName("pushButton_SaveMasks_")
        self.gridLayout_7.addWidget(self.pushButton_SaveMasks_, 5, 0, 1, 1)
        self.pushButton_Interpolate_ = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_Interpolate_.setObjectName("pushButton_Interpolate_")
        self.gridLayout_7.addWidget(self.pushButton_Interpolate_, 6, 0, 1, 1)
        self.pushButton_MaskAll_ = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_MaskAll_.setObjectName("pushButton_MaskAll_")
        self.gridLayout_7.addWidget(self.pushButton_MaskAll_, 2, 0, 1, 1)
        self.pushButton_AddMask_ = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_AddMask_.setObjectName("pushButton_AddMask_")
        self.gridLayout_7.addWidget(self.pushButton_AddMask_, 1, 0, 1, 1)
        self.pushButton_ApplyMask_ = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_ApplyMask_.setObjectName("pushButton_ApplyMask_")
        self.gridLayout_7.addWidget(self.pushButton_ApplyMask_, 3, 0, 1, 1)
        self.pushButton_AlignAll_ = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_AlignAll_.setObjectName("pushButton_AlignAll_")
        self.gridLayout_7.addWidget(self.pushButton_AlignAll_, 6, 1, 1, 1)
        self.pushButton_RemoveAllMask_ = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_RemoveAllMask_.setObjectName("pushButton_RemoveAllMask_")
        self.gridLayout_7.addWidget(self.pushButton_RemoveAllMask_, 2, 1, 1, 1)
        self.pushButton_Conv2Delta_ = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_Conv2Delta_.setObjectName("pushButton_Conv2Delta_")
        self.gridLayout_7.addWidget(self.pushButton_Conv2Delta_, 0, 1, 1, 1)
        self.pushButton_ApplyAllMask_ = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_ApplyAllMask_.setObjectName("pushButton_ApplyAllMask_")
        self.gridLayout_7.addWidget(self.pushButton_ApplyAllMask_, 3, 1, 1, 1)
        self.pushButton_DrawMask_ = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_DrawMask_.setObjectName("pushButton_DrawMask_")
        self.gridLayout_7.addWidget(self.pushButton_DrawMask_, 0, 0, 1, 1)
        self.pushButton_Unwrap_ = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_Unwrap_.setObjectName("pushButton_Unwrap_")
        self.gridLayout_7.addWidget(self.pushButton_Unwrap_, 4, 0, 1, 1)
        self.pushButton_UnwrapAll_ = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_UnwrapAll_.setObjectName("pushButton_UnwrapAll_")
        self.gridLayout_7.addWidget(self.pushButton_UnwrapAll_, 4, 1, 1, 1)
        self.pushButton_RemoveMask_ = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_RemoveMask_.setObjectName("pushButton_RemoveMask_")
        self.gridLayout_7.addWidget(self.pushButton_RemoveMask_, 1, 1, 1, 1)
        self.pushButton_LoadMask_ = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_LoadMask_.setObjectName("pushButton_LoadMask_")
        self.gridLayout_7.addWidget(self.pushButton_LoadMask_, 5, 1, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_11.setObjectName("gridLayout_11")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem1, 1, 0, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_LeftAlign = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_LeftAlign.setObjectName("pushButton_LeftAlign")
        self.gridLayout_3.addWidget(self.pushButton_LeftAlign, 1, 0, 1, 1)
        self.pushButton_RightAlign = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_RightAlign.setObjectName("pushButton_RightAlign")
        self.gridLayout_3.addWidget(self.pushButton_RightAlign, 1, 2, 1, 1)
        self.lineEdit_Alignment = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_Alignment.setValidator(self.intInputValidation)
        self.lineEdit_Alignment.setObjectName("lineEdit_Alignment")
        self.gridLayout_3.addWidget(self.lineEdit_Alignment, 1, 1, 1, 1)
        self.pushButton_DownAlign = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_DownAlign.setObjectName("pushButton_DownAlign")
        self.gridLayout_3.addWidget(self.pushButton_DownAlign, 2, 1, 1, 1)
        self.pushButton_UpAlign = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_UpAlign.setObjectName("pushButton_UpAlign")
        self.gridLayout_3.addWidget(self.pushButton_UpAlign, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 3, 1, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_shifts = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_shifts.setObjectName("pushButton_shifts")
        self.gridLayout_4.addWidget(self.pushButton_shifts, 0, 0, 1, 1)
        self.pushButton_Diff = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_Diff.setObjectName("pushButton_Diff")
        self.gridLayout_4.addWidget(self.pushButton_Diff, 1, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_9, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem3, 2, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem4, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem5, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lineEdit_StepCrop = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_StepCrop.setValidator(self.intInputValidation)
        self.lineEdit_StepCrop.setObjectName("lineEdit_StepCrop")
        self.gridLayout_5.addWidget(self.lineEdit_StepCrop, 1, 1, 1, 1)
        self.pushButton_CropUp = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_CropUp.setObjectName("pushButton_CropUp")
        self.gridLayout_5.addWidget(self.pushButton_CropUp, 2, 1, 1, 1)
        self.pushButton_CropDown = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_CropDown.setObjectName("pushButton_CropDown")
        self.gridLayout_5.addWidget(self.pushButton_CropDown, 0, 1, 1, 1)
        self.pushButton_CropRight = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_CropRight.setObjectName("pushButton_CropRight")
        self.gridLayout_5.addWidget(self.pushButton_CropRight, 1, 0, 1, 1)
        self.pushButton_CropLeft = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_CropLeft.setObjectName("pushButton_CropLeft")
        self.gridLayout_5.addWidget(self.pushButton_CropLeft, 1, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem6, 3, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButton_crop = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_crop.setObjectName("pushButton_crop")
        self.gridLayout_6.addWidget(self.pushButton_crop, 1, 0, 1, 1)
        self.pushButton_reset = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.gridLayout_6.addWidget(self.pushButton_reset, 2, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_6, 1, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_8, 1, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem7, 1, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem8, 0, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem9, 1, 2, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem10, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_20.setObjectName("gridLayout_20")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_20.addItem(spacerItem11, 0, 2, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_20.addItem(spacerItem12, 0, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_20.addItem(spacerItem13, 5, 1, 1, 1)
        self.pushButton_DrawMean_pix = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_DrawMean_pix.setObjectName("pushButton_DrawMean_pix")
        self.gridLayout_20.addWidget(self.pushButton_DrawMean_pix, 1, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_x = QtWidgets.QLabel(self.tab_5)
        self.label_x.setObjectName("label_x")
        self.horizontalLayout_5.addWidget(self.label_x)
        self.LineEdit_X = QtWidgets.QLineEdit(self.tab_5)
        self.LineEdit_X.setValidator(self.intInputValidation)
        self.LineEdit_X.setObjectName("LineEdit_X")
        self.horizontalLayout_5.addWidget(self.LineEdit_X)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_y = QtWidgets.QLabel(self.tab_5)
        self.label_y.setObjectName("label_y")
        self.horizontalLayout_4.addWidget(self.label_y)
        self.lineEdit_Y = QtWidgets.QLineEdit(self.tab_5)
        
        self.lineEdit_Y.setObjectName("lineEdit_Y")
        self.lineEdit_Y.setValidator(self.intInputValidation)
        self.horizontalLayout_4.addWidget(self.lineEdit_Y)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        self.gridLayout_20.addLayout(self.horizontalLayout_6, 0, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_20.addItem(spacerItem14, 2, 1, 1, 1)
        self.gridLayout_19 = QtWidgets.QGridLayout()
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.pushButton_RoiMean = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_RoiMean.setObjectName("pushButton_RoiMean")
        self.gridLayout_19.addWidget(self.pushButton_RoiMean, 1, 0, 1, 1)
        self.pushButton_Draw_ROI = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_Draw_ROI.setObjectName("pushButton_Draw_ROI")
        self.gridLayout_19.addWidget(self.pushButton_Draw_ROI, 0, 0, 1, 3)
        self.pushButton_RoiVar = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_RoiVar.setObjectName("pushButton_RoiVar")
        self.gridLayout_19.addWidget(self.pushButton_RoiVar, 1, 2, 1, 1)
        self.pushButton_RoiStd = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_RoiStd.setObjectName("pushButton_RoiStd")
        self.gridLayout_19.addWidget(self.pushButton_RoiStd, 1, 1, 1, 1)
        self.gridLayout_20.addLayout(self.gridLayout_19, 3, 0, 1, 3)
        self.tabWidget.addTab(self.tab_5, "")
        self.gridLayout_16.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.operations = QtWidgets.QLabel(self.frame)
        self.operations.setObjectName("operations")
        self.gridLayout_16.addWidget(self.operations, 0, 0, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_16, 0, 0, 1, 1)
        self.gridLayout_18.addWidget(self.frame, 0, 0, 5, 1)
        self.gridLayout_toolbar1 = QtWidgets.QGridLayout()
        self.gridLayout_toolbar1.setObjectName("gridLayout_toolbar1")
        self.gridLayout_toolbar1.addWidget(self.toolbar1, 0, 0, 0, 0)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_toolbar1.addItem(spacerItem15, 0, 0, 1, 1)
        self.gridLayout_18.addLayout(self.gridLayout_toolbar1, 0, 1, 1, 1)
        self.Before = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Before.setFont(font)
        self.Before.setObjectName("Before")
        self.gridLayout_18.addWidget(self.Before, 0, 2, 1, 1)
        self.gridLayout_canvas1 = QtWidgets.QGridLayout()
        self.gridLayout_canvas1.setObjectName("gridLayout_canvas1")
        self.gridLayout_canvas1.addWidget(self.canvas1, 0, 0, 0, 0)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_canvas1.addItem(spacerItem16, 0, 0, 1, 1)
        self.gridLayout_18.addLayout(self.gridLayout_canvas1, 1, 1, 1, 2)
        self.gridLayout_toolbar2 = QtWidgets.QGridLayout()
        self.gridLayout_toolbar2.addWidget(self.toolbar2, 0, 0, 0, 0)
        self.gridLayout_toolbar2.setObjectName("gridLayout_toolbar2")
        
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_toolbar2.addItem(spacerItem17, 0, 0, 1, 1)
        self.gridLayout_18.addLayout(self.gridLayout_toolbar2, 2, 1, 1, 1)
        self.AfterPro = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.AfterPro.setFont(font)
        self.AfterPro.setObjectName("AfterPro")
        self.gridLayout_18.addWidget(self.AfterPro, 2, 2, 1, 1)
        self.gridLayout_canvas1_2 = QtWidgets.QGridLayout()
        self.gridLayout_canvas1_2.setObjectName("gridLayout_canvas1_2")
        self.gridLayout_canvas1_2.addWidget(self.canvas2, 0, 0, 0, 0)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_canvas1_2.addItem(spacerItem18, 0, 0, 1, 1)
        self.gridLayout_18.addLayout(self.gridLayout_canvas1_2, 3, 1, 1, 2)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.LVmin = QtWidgets.QLabel(self.frame_2)
        self.LVmin.setObjectName("LVmin")
        self.gridLayout_2.addWidget(self.LVmin, 1, 1, 1, 1)
        self.VMIN = QtWidgets.QLineEdit(self.frame_2)
        self.VMIN.setValidator(self.DoubleInputValidation)
        self.VMIN.setObjectName("VMIN")
        self.gridLayout_2.addWidget(self.VMIN, 1, 2, 1, 1)
        self.VMAX = QtWidgets.QLineEdit(self.frame_2)
        self.VMAX.setValidator(self.DoubleInputValidation)
        self.VMAX.setObjectName("VMAX")
        self.gridLayout_2.addWidget(self.VMAX, 1, 3, 1, 1)
        self.LVMax = QtWidgets.QLabel(self.frame_2)
        self.LVMax.setObjectName("LVMax")
        self.gridLayout_2.addWidget(self.LVMax, 1, 4, 1, 1)
        self.VMIN_2 = QtWidgets.QLineEdit(self.frame_2)
        self.VMIN_2.setValidator(self.DoubleInputValidation)
        self.VMIN_2.setObjectName("VMIN_2")
        self.gridLayout_2.addWidget(self.VMIN_2, 2, 2, 1, 1)
        self.VMAX_2 = QtWidgets.QLineEdit(self.frame_2)
        self.VMAX_2.setValidator(self.DoubleInputValidation)
        self.VMAX_2.setObjectName("VMAX_2")
        self.gridLayout_2.addWidget(self.VMAX_2, 2, 3, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.frame_2)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_2.addWidget(self.horizontalSlider, 0, 0, 1, 5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Labelcolormap = QtWidgets.QLabel(self.frame_2)
        self.Labelcolormap.setObjectName("Labelcolormap")
        self.horizontalLayout.addWidget(self.Labelcolormap)
        self.comboBox_colormap = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_colormap.setObjectName("comboBox_colormap")
        self.horizontalLayout.addWidget(self.comboBox_colormap)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 5, 1, 1)
        self.label_vmin2 = QtWidgets.QLabel(self.frame_2)
        self.label_vmin2.setObjectName("label_vmin2")
        self.gridLayout_2.addWidget(self.label_vmin2, 2, 1, 1, 1)
        self.label_vmax2 = QtWidgets.QLabel(self.frame_2)
        self.label_vmax2.setObjectName("label_vmax2")
        self.gridLayout_2.addWidget(self.label_vmax2, 2, 4, 1, 1)
        self.gridLayout_18.addWidget(self.frame_2, 4, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        for i in range (0,len(self.list_cmap)):
            self.comboBox_colormap.addItem(self.list_cmap[i])
        
        self.comboBox_colormap.setCurrentIndex(124)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        #buttons connections
        
        self.pushButton_DrawMask_.clicked.connect(self.draw_mask)
        self.pushButton_AddMask_.clicked.connect(self.add_mask)
        self.pushButton_MaskAll_.clicked.connect(self.mask_all)
        
        self.radioButton_absorption.clicked.connect(self.absorption_contrast)
        self.radioButton_phase.clicked.connect(self.phase_contrast)
        
        
        self.input_dialog = InputDialog(self)
        self.input_text_dialog=InputTextDialog(self)
        
        
        self.pushButton_Conv2Delta_.clicked.connect(self.convert_to_delta)

        self.pushButton_ApplyMask_.clicked.connect(self.apply_mask)
        self.pushButton_ApplyAllMask_.clicked.connect(self.apply_all_masks)
        self.pushButton_RemoveMask_.clicked.connect(self.remove_mask)
        self.pushButton_RemoveAllMask_.clicked.connect(self.remove_all_mask)

        self.pushButton_Unwrap_.clicked.connect(self.unwrapping_phase)
        self.pushButton_UnwrapAll_.clicked.connect(self.unwrapping_all)
        self.pushButton_SaveMasks_.clicked.connect(self.save_masks)
        self.pushButton_LoadMask_.clicked.connect(self.load_masks)
        self.pushButton_Interpolate_.clicked.connect(self.interpolate)
        self.pushButton_AlignAll_.clicked.connect(self.align_all)
        self.pushButton_shifts.clicked.connect(self.plot_shifts)
        self.pushButton_Diff.clicked.connect(self.show_diff)

        self.pushButton_LeftAlign.clicked.connect(self.moveleft)
        self.pushButton_RightAlign.clicked.connect(self.moveright)
        self.pushButton_UpAlign.clicked.connect(self.moveup)
        self.pushButton_DownAlign.clicked.connect(self.movedown)

        self.pushButton_CropLeft.clicked.connect(self.cropright)
        self.pushButton_CropRight.clicked.connect(self.cropleft)
        self.pushButton_CropUp.clicked.connect(self.croptop)
        self.pushButton_CropDown.clicked.connect(self.cropbottom)
        self.pushButton_crop.clicked.connect(self.croparray)
        self.pushButton_reset.clicked.connect(self.resetselection)
        
        
        self.VMIN.returnPressed.connect(self.cmvmin)
        self.VMAX.returnPressed.connect(self.cmvmax)
        self.lineEdit_Alignment.returnPressed.connect(self.setalignpixel)
        self.lineEdit_StepCrop.returnPressed.connect(self.setcropval)
        self.tableWidget.itemClicked.connect(self.get_ItemIndex)
        
        
        self.lineEdit_Suffix.returnPressed.connect(self.get_sufix)
        self.pushButton_browse.clicked.connect(self.read_data)
        
        self.pushButton_SaveProj.clicked.connect(self.save_projection)
        self.pushButton_SaveAllProj.clicked.connect(self.save_all_projection)
        self.horizontalSlider.valueChanged.connect(self.slide_projs)
        
        
        self.pushButton_Draw_ROI.clicked.connect(self.draw_ROI)
        self.pushButton_RoiMean.clicked.connect(self.draw_mean)
        self.pushButton_RoiStd.clicked.connect(self.draw_std)
        self.pushButton_RoiVar.clicked.connect(self.draw_var)
        self.LineEdit_X.returnPressed.connect(self.get_x)
        
        self.lineEdit_Y.returnPressed.connect(self.get_y)
        self.pushButton_DrawMean_pix.clicked.connect(self.plot_intensity_at_pixel)
        
        self.VMAX_2.returnPressed.connect(self.cmvmax_org)
        self.VMIN_2.returnPressed.connect(self.cmvmin_org)
        
        self.comboBox_colormap.currentTextChanged.connect(self.get_cmap)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ProSPyX"))
        self.listofprojections.setText(_translate("MainWindow", "List of projections: "))
        self.pushButton_SaveProj.setText(_translate("MainWindow", "Save the current projection"))
        self.pushButton_SaveAllProj.setText(_translate("MainWindow", "Save all projections"))
        
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Suffix"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Energy"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Min_B"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Min_A"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Max_B"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Max_A"))
        self.label_path.setText(_translate("MainWindow", "            Path:"))
        self.Suffix.setText(_translate("MainWindow", "       Suffix :"))
        self.pushButton_browse.setText(_translate("MainWindow", "Browse"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Data"))
        self.pushButton_SaveMasks_.setText(_translate("MainWindow", "Save mask"))
        self.pushButton_Interpolate_.setText(_translate("MainWindow", "Interpolate"))
        self.pushButton_MaskAll_.setText(_translate("MainWindow", "Mask all"))
        self.pushButton_AddMask_.setText(_translate("MainWindow", "Add mask"))
        self.pushButton_ApplyMask_.setText(_translate("MainWindow", "Apply mask"))
        self.pushButton_AlignAll_.setText(_translate("MainWindow", "Align all"))
        self.pushButton_RemoveAllMask_.setText(_translate("MainWindow", "Remove all mask"))
        self.pushButton_Conv2Delta_.setText(_translate("MainWindow", "Contrast conversion"))
        self.pushButton_ApplyAllMask_.setText(_translate("MainWindow", "Apply all mask"))
        self.pushButton_DrawMask_.setText(_translate("MainWindow", "Draw mask"))
        self.pushButton_Unwrap_.setText(_translate("MainWindow", "Unwrap"))
        self.pushButton_UnwrapAll_.setText(_translate("MainWindow", "Unwrap all"))
        self.pushButton_RemoveMask_.setText(_translate("MainWindow", "Remove mask"))
        self.pushButton_LoadMask_.setText(_translate("MainWindow", "Load mask"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Processing"))
        self.pushButton_LeftAlign.setText(_translate("MainWindow", "←"))
        self.pushButton_RightAlign.setText(_translate("MainWindow", "→"))
        self.pushButton_DownAlign.setText(_translate("MainWindow", "↑"))
        self.pushButton_UpAlign.setText(_translate("MainWindow", "↓"))
        self.pushButton_shifts.setText(_translate("MainWindow", "Shifts"))
        self.pushButton_Diff.setText(_translate("MainWindow", "Diff"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Align"))
        self.pushButton_CropUp.setText(_translate("MainWindow", "↑"))
        self.pushButton_CropDown.setText(_translate("MainWindow", "↓"))
        self.pushButton_CropRight.setText(_translate("MainWindow", "→"))
        self.pushButton_CropLeft.setText(_translate("MainWindow", "←"))
        self.pushButton_crop.setText(_translate("MainWindow", "Crop"))
        self.pushButton_reset.setText(_translate("MainWindow", "Reset"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Crop"))
        self.pushButton_DrawMean_pix.setText(_translate("MainWindow", "Plot intensity_at_pixel"))
        self.label_x.setText(_translate("MainWindow", "x"))
        self.label_y.setText(_translate("MainWindow", "y"))
        self.pushButton_RoiMean.setText(_translate("MainWindow", "Mean_ROI"))
        self.pushButton_Draw_ROI.setText(_translate("MainWindow", "Draw ROI"))
        self.pushButton_RoiVar.setText(_translate("MainWindow", "Var_ROI"))
        self.pushButton_RoiStd.setText(_translate("MainWindow", "Std_ROI"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Stats"))
        self.operations.setText(_translate("MainWindow", "Operations :"))
        self.Before.setText(_translate("MainWindow", "Before processing"))
        self.AfterPro.setText(_translate("MainWindow", "After processing"))
        self.LVmin.setText(_translate("MainWindow", "Vmin_A "))
        self.LVMax.setText(_translate("MainWindow", "Vmax_A"))
        self.Labelcolormap.setText(_translate("MainWindow", "Colormap:"))
        self.label_vmin2.setText(_translate("MainWindow", "Vmin_B"))
        self.label_vmax2.setText(_translate("MainWindow", "Vmax_B"))
   
    
   
    def test1(self):
        
        print("test for absorption ")

    def absorption_contrast(self):
        
        if self.data_==0:
            print("There is no data ")
            QMessageBox.warning(None, 'Error',"There is no data")
            
        else:
            
            print("abs")
            self.X01_previous_phase=self.X01
            self.X1_previous_phase=self.X1
            # self.X02_previous_phase=self.X02
            # self.X2_previous_phase=self.X2
            
            self.X01=self.X03
            self.X1=self.X3
            self.X2 = self.X1[:, self.hcen, :].copy()
            self.X02=self.X01[:, self.hcen, :].copy()
            
            
                    
            
            
            
            self.pushButton_ApplyMask_.setText("Normalization")
            self.pushButton_ApplyMask_.clicked.disconnect(self.apply_mask)
            self.pushButton_ApplyMask_.clicked.connect(self.Normalization)
            
            self.pushButton_ApplyAllMask_.setText("Normalization all")
            self.pushButton_ApplyAllMask_.clicked.disconnect(self.apply_all_masks)
            self.pushButton_ApplyAllMask_.clicked.connect(self.Normalization_all)
            
            
            
            
            self.pushButton_Unwrap_.setText('Convert to (\u03BC*sample thickness)')
            self.pushButton_Unwrap_.clicked.disconnect(self.unwrapping_phase)
            self.pushButton_Unwrap_.clicked.connect(self.convert_mudz)
            
            self.pushButton_UnwrapAll_.setText('Convert to (\u03BC*sample thickness) all')
            self.pushButton_UnwrapAll_.clicked.disconnect(self.unwrapping_all)
            self.pushButton_UnwrapAll_.clicked.connect(self.convert_mudz_all)
            
            
            self.phase_amp=1
            self.update_list()
            self.update_org()
            self.update_pro()
            
        
    
    def phase_contrast(self):
        
        if self.data_==0:
            print("There is no data ")
            QMessageBox.warning(None, 'Error',"There is no data")
            
        else:
            
        
            print("ph")
            self.X01_previous_absorption=self.X03
            self.X1_previous_absorption=self.X3
            # self.X02_previous_absorption=self.X02
            # self.X2_previous_absorption=self.X2
            
            self.X01=self.X01_previous_phase#self.X03
            self.X1=self.X1_previous_phase#self.X03
            self.X2 = self.X1[:, self.hcen, :].copy()
            self.X02=self.X01[:, self.hcen, :].copy()
            
           
            self.pushButton_ApplyMask_.setText("Apply mask")
            self.pushButton_ApplyMask_.clicked.disconnect(self.Normalization)
            self.pushButton_ApplyMask_.clicked.connect(self.apply_mask)
            
            
            self.pushButton_ApplyAllMask_.setText("Apply all mask")
            self.pushButton_ApplyAllMask_.clicked.disconnect(self.Normalization_all)
            self.pushButton_ApplyAllMask_.clicked.connect(self.apply_all_masks)
            
           
            self.pushButton_Unwrap_.setText("Unwrap")
            self.pushButton_Unwrap_.clicked.disconnect(self.convert_mudz)
            self.pushButton_Unwrap_.clicked.connect(self.unwrapping_phase)
            
            
            self.pushButton_UnwrapAll_.setText("Unwrap all")
            self.pushButton_UnwrapAll_.clicked.disconnect(self.convert_mudz_all)
            self.pushButton_UnwrapAll_.clicked.connect(self.unwrapping_all)
            
            self.phase_amp=0
            self.update_list()
            self.update_org()
            self.update_pro()
    
    
    
    def rotate(self):
        
        if self.data_==0:
            print("There is no data to rotate")
            QMessageBox.warning(None, 'Error',"There is no data to rotate")
            
        else:
            tmp_b=np.rot90(self.X01[0],1/2)
            tmp_a=np.rot90(self.X1[0],1/2)
            nprojs=len(self.X1)
            nr_b,nc_b=tmp_b.shape
            nr_a,nc_a=tmp_a.shape
            
            
            tmp_before=np.zeros((nprojs,nr_b,nc_b))
            tmp_after=np.zeros((nprojs,nr_a,nc_a))
            tmp_abs_before=np.zeros((nprojs,nr_a,nc_a))
            tmp_abs_after=np.zeros((nprojs,nr_a,nc_a))
            
            
            
            
            if self.phase_amp==0:
                
            
                for i in range(len(self.X1)):
                
                    tmp_before[i]=np.rot90(self.X01[i],1/2)
                    tmp_after[i]=np.rot90(self.X1[i],1/2)
                    tmp_abs_before[i]=np.rot90(self.X03[i],1/2)
                    tmp_abs_after[i]=np.rot90(self.X3[i],1/2)
        
                del self.X1
                del self.X01
                del self.X03
                del self.X3
        
        
                self.X1=tmp_after
                self.X01=tmp_before
                self.X03=tmp_abs_before
                self.X3= tmp_abs_after
                
                
            else:
                
                for i in range(len(self.X1)):
                
                    tmp_before[i]=np.rot90(self.X01[i],1/2)
                    tmp_after[i]=np.rot90(self.X1[i],1/2)
                    tmp_abs_before[i]=np.rot90(self.X01_previous_phase[i],1/2)
                    tmp_abs_after[i]=np.rot90(self.X1_previous_phase[i],1/2)
        
                del self.X1
                del self.X01
                del self.X03
                del self.X1_previous_phase
        
        
                self.X1_previous_phase=tmp_abs_after
                self.X01=tmp_before
                self.X01_previous_phase=tmp_abs_before
                self.X1= tmp_after
                self.X03=tmp_before
                self.X3=tmp_after
                
                
            
            
            self.projs, self.rows, self.cols = self.X1.shape
            self.projs0, self.rows0, self.cols0 = self.X01.shape
            self.hcen = int(self.rows / 2.0)
            self.hcen0 = int(self.rows0 / 2.0)
            self.X2 = self.X1[:, self.hcen, :].copy()
            self.X02=self.X01[:, self.hcen, :].copy()
            self.mask = np.zeros_like(self.X1, dtype=bool)
            self.cl, self.cr, self.ct, self.cb = 0, 0, 0, 0
            
            self.ind = 0
            self.mask = np.zeros_like(self.X1, dtype=bool)
            self.colormap = self.params["colormap"]
            self.vmin = self.params["vmin"]
            self.vmax = self.params["vmax"]
            
            self.vmin_2=self.params["vmin"]
            self.vmax_2=self.params["vmax"]
            self.crop = self.params["crop"]
            self.colormap = self.params["colormap"]
            self.pixel = self.pixel
            self.maxenergy = np.max(self.energy)
            self.maxind = self.energy.argmax()
            self.pxmaxenergy = self.pixel[self.maxind][0]
            self.maxenergyproj = self.X1[self.maxind].copy()
            self.cropval = 1
            self.alignpixel = 1.0
            self.shift = np.zeros((2,self.projs, 2))
            self.step_crop = 1
            self.limh0=0
            self.limhf=self.cols
            self.limv0=0
            self.limvf=self.rows
        

        
        
        
        self.update_pro()
        self.update_org()
    def get_cmap(self):
        
        if self.data_==0:
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
            
        else :
            
        
            self.colormap=self.comboBox_colormap.currentText()
            self.update_org()
            self.update_pro()
        
    
    def get_sufix(self):
        
        self.params['sufix']=self.lineEdit_Suffix.text()    
        
        
    

    def read_data(self):


            
            fname=QFileDialog.getExistingDirectory(self,'choose the folder where data are stored')

                    
            if fname and self.params['sufix']:
                self.params['path'] = fname
                print("Variales defined")
                self.data_wcard = os.path.join(os.path.abspath(
                    self.params['path']), self.params['sufix']+'*')
                self.files_wcard = os.path.join(self.data_wcard, self.params['sufix']+'*_recons.h5')
                
                
                
                
                
                self.file_list = glob.glob(self.files_wcard)
                
                if len(self.file_list)>=1:
                    self.data_=1
                    self.params['path'] = fname
                    #self.params['sufix'] = 
                    self.contrast=0
                    
                    # -------------
                
                    

                    
                    self.energy = np.zeros(len(self.file_list))

                    for ii in range(len(self.file_list)):
                        
                        
                        f=h5py.File(self.file_list[ii],'r')



                        self.energy[ii]=np.array(f.get('/reconstruction/p/energy'))


                    f.close()


                    self.file_list,self.energy=sort_array(np.array(self.file_list), self.energy)

                    
                    # self.num_files = len(self.file_list)
                    self.num_files = len(self.file_list)
                    # self.objdata0, self.probedata0, self.pixel0, self.energy0 = read_ptyr(self.file_list[-1])
                    # self.nr, self.nc = self.objdata0.shape
                    
                    self.f=h5py.File(self.file_list[-1],'r')
                    
                    
                    self.objdata0=np.array(self.f.get('/reconstruction/p/objects/object_0'))
                    self.pixel0=np.transpose(np.array(self.f.get('/reconstruction/p/dx_spec')))
                    self.energy0=np.array(self.f.get('/reconstruction/p/energy'))

                    self.f.close()
                    
                    
                    self.nr, self.nc = self.objdata0.shape
                    
                    
                    
                
                    # initializing the arrays for memory allocation
                    self.X1 = np.zeros((self.num_files, self.nr, self.nc), dtype=float)  # only phases
                    self.X01=np.zeros((self.num_files, self.nr, self.nc), dtype=float)
                    self.X03=np.zeros((self.num_files, self.nr, self.nc), dtype=float)
                    self.X3=np.zeros((self.num_files, self.nr, self.nc), dtype=float)
                    

                    
                    # objdata = np.zeros((num_files,nr,nc),dtype=np.complex64) # if complex
                    self.pixel = np.zeros((self.num_files, 2))
                    
                    self.problematic = []
                    for ii in range(self.num_files):
                        
                        
                        self.f=h5py.File(self.file_list[ii],'r')
            # List all groups




                        self.objdata_aux=np.array(self.f.get('/reconstruction/p/objects/object_0'))
                        self.pixel[ii]=np.transpose(np.array(self.f.get('/reconstruction/p/dx_spec')))
                        self.energy[ii]=np.array(self.f.get('/reconstruction/p/energy'))

                        self.f.close()
                    # loop to read the files (only phases)
                
                        
                        if self.objdata0.shape != self.objdata_aux.shape:
                            
                            print(
                                f"Array shape ({self.objdata_aux.shape}) is different from initial one ({self.objdata0.shape})")
                            drx = (int(((self.objdata0.shape[0] - self.objdata_aux.shape[0]))))
                            dry = (int(((self.objdata0.shape[1] - self.objdata_aux.shape[1]))))
                            
                            if drx == 0 and dry == 0:
                
                                print("no padding or cropping because the 2 arrays have the same dims")
                            if drx == 0 and dry > 0:
                
                                print(f"Padding in y axis  with margins of {dry} pixels")
                                self.objdata_aux = np.pad(
                                    self.objdata_aux, ((0, 0), (0, dry)), mode='reflect')
                
                            if drx == 0 and dry < 0:
                                print(
                                    f"Padding objdata0  in y axis  with margins of {dry} pixels")
                                
                                self.objdata_aux = np.resize(
                                    self.objdata_aux, (self.objdata0.shape[0], self.objdata0.shape[1]))
                
                            if drx > 0 and dry == 0:
                                print(f"Padding in x axis with margins of {drx} ")
                                self.objdata_aux = np.pad(
                                    self.objdata_aux, ((0, drx), (0, 0)), mode='reflect')
                
                            if drx > 0 and dry > 0:
                                print(
                                    f"Padding in x axis with margins of {drx} and y axis  with margins of {dry} pixels")
                                self.objdata_aux = np.pad(
                                    self.objdata_aux, ((0, drx), (0, dry)), mode='reflect')
                
                            if drx > 0 and dry < 0:
                                print(
                                    f"Padding in x axis with margins of {drx} and y axis  with margins of {dry} pixels")
                                self.objdata_aux = np.pad(
                                    self.objdata_aux, ((0, drx), (0, 0)), mode='reflect')
                                self.objdata_aux = np.resize(
                                    self.objdata_aux, (self.objdata0.shape[0], self.objdata0.shape[1]))
                            if drx < 0 and dry == 0:
                                print(
                                    f"Padding objdata with 0 in x axis with margins of {drx}")
                                #objdata[ii] = np.pad(objdata[ii],((0,np.abs(drx)),(0,0)),mode='constant',constant_values=0)
                
                            if drx < 0 and dry > 0:
                                print(
                                    f"Padding objdata with 0 in x axis with margins of {drx}")
                                #objdata[ii] = np.pad(objdata[ii],((0,np.abs(drx)),(0,0)),mode='constant',constant_values=0)
                                print(f"Padding in y axis  with margins of {dry} pixels")
                                self.objdata_aux = np.pad(
                                    self.objdata_aux, ((0, 0), (0, dry)), mode='reflect')
                                self.objdata_aux = np.resize(
                                    self.objdata_aux, (self.objdata0.shape[0], self.objdata0.shape[1]))
                
                            if drx < 0 and dry < 0:
                                print(
                                    f"Padding objdata with 0 in x axis with margins of {drx} and in y axis with margins of {dry}")
                                #objdata[ii] = np.pad(objdata[ii],((0,np.abs(drx)),(0,np.abs(dry))),mode='constant',constant_values=(0,0))
                                self.objdata_aux = np.resize(
                                    self.objdata_aux, (self.objdata0.shape[0], self.objdata0.shape[1]))
                
                        self.X1[ii] = np.angle(self.objdata_aux)  # only phase
                        self.X01[ii]=np.angle(self.objdata_aux)
                        self.X03[ii]=np.abs(self.objdata_aux)
                        self.X3[ii]=np.abs(self.objdata_aux)
                    self.X1 = self.X1.copy()
                    
                    self.X01_previous_phase=self.X01
                    self.X1_previous_phase=self.X1
                    self.X01_previous_absorption=self.X03
                    self.X1_previous_absorption=self.X3
                    self.before_delta=np.zeros_like(self.X1)
                    self.before_beta=np.zeros_like(self.X3)
                    if np.iscomplexobj(self.X1):
                
                        raise ValueError("The array is complex")
                    self.projs, self.rows, self.cols = self.X1.shape
                    self.projs0, self.rows0, self.cols0 = self.X01.shape
                    self.hcen = int(self.rows / 2.0)
                    self.hcen0 = int(self.rows0 / 2.0)
                    self.X2 = self.X1[:, self.hcen, :].copy()
                    self.X02=self.X01[:, self.hcen, :].copy()
                    self.mask = np.zeros_like(self.X1, dtype=bool)
                    self.cl, self.cr, self.ct, self.cb = 0, 0, 0, 0
                    
                    self.ind = 0
                    self.mask = np.zeros_like(self.X1, dtype=bool)
                    self.colormap = self.params["colormap"]
                    self.vmin = self.params["vmin"]
                    self.vmax = self.params["vmax"]
                    
                    self.vmin_2=self.params["vmin"]
                    self.vmax_2=self.params["vmax"]
                    self.crop = self.params["crop"]
                    self.colormap = self.params["colormap"]
                    self.pixel = self.pixel
                    self.maxenergy = np.max(self.energy)
                    self.maxind = self.energy.argmax()
                    self.pxmaxenergy = self.pixel[self.maxind][0]
                    self.maxenergyproj = self.X1[self.maxind].copy()
                    self.cropval = 1
                    self.alignpixel = 1.0
                    self.shift = np.zeros((2,self.projs, 2))
                    self.step_crop = 1
                    self.limh0=0
                    self.limhf=self.cols
                    self.limv0=0
                    self.limvf=self.rows
                    # self.X01 = self.X1
                    
                    # self.X02 = self.X2
                    
                    self.horizontalSlider.setMaximum(len(self.file_list))
                    self.tableWidget.setRowCount(len(self.file_list))
                    for i in range(0,len(self.file_list)):
                        self.tableWidget.setItem(i,0, QtWidgets.QTableWidgetItem(self.params['sufix']))
                        self.tableWidget.setItem(i,1, QtWidgets.QTableWidgetItem("{:5.4f}".format(self.energy[i])))
                        self.tableWidget.setItem(i,2, QtWidgets.QTableWidgetItem("{:4.2f}".format(np.min(self.X01[i]))))
                        self.tableWidget.setItem(i,3, QtWidgets.QTableWidgetItem("{:4.2f}".format(np.min(self.X1[i]))))
                        self.tableWidget.setItem(i,4, QtWidgets.QTableWidgetItem("{:4.2f}".format(np.max(self.X01[i]))))
                        self.tableWidget.setItem(i,5, QtWidgets.QTableWidgetItem("{:4.2f}".format(np.max(self.X1[i]))))
                        
                        
                    #self.tableWidget.setItem(0,0, QtWidgets.QTableWidgetItem("Name"))
                    self.tableWidget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                    #self.tableWidget.horizontalHeader().setStretchLastSection(True)
                    self.tableWidget.horizontalHeader().setSectionResizeMode(
                        QtWidgets.QHeaderView.ResizeToContents)
                    
                    
                    rows = 2
                    columns = self.projs

                    self.text0 = [['' for _ in range(columns)] for _ in range(rows)]


                    self.text0[0] = ["Phase shift [rad]"] * columns

                    self.text0[1] = ["Amplitude [a.u.]"] * columns
                    
                    
                    self.text = [['' for _ in range(columns)] for _ in range(rows)]


                    self.text[0] = ["Phase shift [rad]"] * columns

                    self.text[1] = ["Amplitude [a.u.]"] * columns
                    
                    
                    from PyQt5.QtGui import QPainter
                    
                    self.update_org()
                    self.update_pro()
                    QMessageBox.information(None, "Processing Done", "reading of the data is done")
                    from PyQt5.QtSvg import QSvgGenerator
                    from PyQt5.QtGui import QPainter, QColor, QPalette  # Add the QPalette import here



                    



                else:
                    print("you need to define correct path")
                    QMessageBox.warning(None, 'Error',"you need to define correct path")
                    
            else:
                print("please define the path and sufix correctly")
                QMessageBox.warning(None, 'Error',"please define the path and/or sufix correctly")
                #self.params["sufix"]= self.input_text_dialog.getText()
                    
                    
                

               
   
    def update_list(self):
        
        if self.data_==0:
            print("No data")
            
        else:
            
        
        
            for i in range(0,len(self.file_list)):
            
                self.tableWidget.setItem(i,2, QtWidgets.QTableWidgetItem("{:4.2f}".format(np.min(self.X01[i]))))    
                self.tableWidget.setItem(i,4, QtWidgets.QTableWidgetItem("{:4.2f}".format(np.max(self.X01[i]))))
                self.tableWidget.setItem(i,3, QtWidgets.QTableWidgetItem("{:4.2f}".format(np.min(self.X1[i]))))
                self.tableWidget.setItem(i,5, QtWidgets.QTableWidgetItem("{:4.2f}".format(np.max(self.X1[i]))))
            #self.tableWidget.setItem(0,0, QtWidgets.QTableWidgetItem("Name"))
            #self.tableWidget.horizontalHeader().setStretchLastSection(True)
            #self.tableWidget.horizontalHeader().setSectionResizeMode(
                #QtWidgets.QHeaderView.Stretch)
                self.tableWidget.horizontalHeader().setSectionResizeMode(
                    QtWidgets.QHeaderView.ResizeToContents)
    def get_ItemIndex(self):
        
        screen = QtWidgets.QApplication.primaryScreen()
        screenshot = screen.grabWindow(self.centralwidget.winId())

# Save the screenshot as an image file
        screenshot.save('mainwindow.png', 'PNG', 100)
        
        if self.data_==0:
            print("No data")
            
        else:
            
        
            self.ind=self.tableWidget.currentRow()
            self.update_org()
            self.update_pro()
        
    def slide_projs(self):
        
        if self.data_==0:
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
        else:
            
        
            self.ind=self.horizontalSlider.value()
            self.update_org()
            self.update_pro()

    def update_org(self):
        
        if self.data_==0:
            print("No data")
            
        else:
            
        
            
            self.figure1.clear()
            scalebar=ScaleBar(self.pixel[self.ind,0])
            ax1=self.figure1.add_subplot(121)
            
            ax2 = self.figure1.add_subplot(122)
            x=0
            
            
            plt.ion()
            im1 = ax1.imshow(
                self.X01[self.ind],
                cmap=self.colormap,#self.colormap,
                vmin=self.vmin_2,
                #vmin=np.min(self.X01[self.ind]),
                vmax=self.vmax_2,
                #vmax=np.max(self.X01[self.ind])
            origin="lower")
            
            ax1.plot([1, self.cols0-1], [self.hcen0, self.hcen0], 'b--')
            # ~ self.vmin,self.vmax = self.im1.get_clim() # get colormap limits
            ax1.axis("tight")
            (im2,) = ax2.plot(self.X02[self.ind, :])
            ax2.plot([0, self.cols0], [0, 0])
            pmin,pmax = ax2.get_ylim()  # get plot limits
            # ax2.axis('tight')
            #ax2.set_ylim([2 * self.vmin_2, 2 * self.vmax_2])
            ax2.set_ylim([2 * np.min(self.X01[self.ind]), 2 * np.max(self.X01[self.ind])])
            ax2.set_xlim([0, self.cols0])
    
            im1.axes.lines.clear()
            
            
            #im1.set_clim(self.vmin_2, self.vmax_2)
            #im1.set_clim(np.min(self.X01[self.ind]), np.max(self.X01[self.ind]))
            
            im2.axes.set_ylim([pmin, pmax])
            im2.axes.set_xlim([0, self.cols0])
            #self.ax2.set_xlim([0, self.cols])
            ax1.set_ylabel("Projection {}".format(self.ind + 1))
            ax1.add_artist(scalebar)
                
            ax2.set_ylabel(self.text0[self.phase_amp][self.ind])
            
            self.figure1.tight_layout()
            #self.figure2.tight_layout(pad=0.55)
            ax1.axes.figure.canvas.draw()
            ax2.axes.figure.canvas.draw()
    
            self.canvas1.draw()

    def update_pro(self):
        
        if self.data_==0:
            print("No data")
            
        else:
            
            plt.close('all')
            self.figure2.clear()
            scalebar=ScaleBar(self.pixel[self.ind,0])
            self.ax1 = self.figure2.add_subplot(121)
            self.ax2 = self.figure2.add_subplot(122)
            #self.ax1.set_title("Use scroll wheel or \n left/right arrows to navigate images")
            plt.ion()
            self.im1 = self.ax1.imshow(
                self.X1[self.ind],
                cmap=self.colormap,
                #vmin=self.vmin,
                vmin=np.min(self.X1[self.ind]),
                #vmax=self.vmax,
                vmax=np.max(self.X1[self.ind])
                
            , origin="lower")
            self.ax1.plot([1, self.cols-1], [self.hcen, self.hcen], 'b--')
            # ~ self.vmin,self.vmax = self.im1.get_clim() # get colormap limits
            self.ax1.axis("tight")
            (self.im2,) = self.ax2.plot(self.X2[self.ind, :])
            self.ax2.plot([0, self.cols], [0, 0])
            self.pmin, self.pmax = self.ax2.get_ylim()  # get plot limits
            # ax2.axis('tight')
            #self.ax2.set_ylim([2 * self.vmin, 2 * self.vmax])
            self.ax2.set_ylim([2 * np.min(self.X1[self.ind]), 2 * np.max(self.X1[self.ind])])
            self.ax2.set_xlim([0, self.cols])
    
            self.im1.axes.lines.clear()
    
            try:
                
                self.im1.set_data(
                    self.X1[self.ind, :, :] + self.mask[self.ind, :, :])
                self.im2.set_ydata(self.X2[self.ind, :])
            except ValueError:
                
                self.im1.axes.cla()  # clear canvas
                self.im1 = self.ax1.imshow(
                    self.X1[self.ind],
                    cmap=self.colormap,
                    #vmin=self.vmin,
                    vmin=np.min(self.X1[self.ind]),
                    #vmax=self.vmax,
                    vmax=np.max(self.X1[self.ind]),origin="lower"
                )
                self.ax1.axis("tight")
                self.im2.axes.cla()
                (self.im2,) = self.ax2.plot(self.X2[self.ind])
                self.ax2.plot([0, self.X1.shape[2]], [0, 0])
                self.pmin, self.pmax = self.ax2.get_ylim()  # get plot limits
    
            if self.cl != 0 or self.cr != 0 or self.ct != 0 or self.cb != 0:
                
                self.im1.axes.lines.clear()

                self.limh0, self.limhf = self.cl, (self.cols - self.cr)
                self.limv0, self.limvf = self.ct, (self.rows - self.cb)
                self.im1.axes.plot([self.limh0, self.limhf], [
                                   self.limv0, self.limv0], "r--")
                self.im1.axes.plot([self.limh0, self.limhf], [
                                   self.limvf, self.limvf], "r--")
                self.im1.axes.plot([self.limh0, self.limh0], [
                                   self.limv0, self.limvf], "r--")
                self.im1.axes.plot([self.limhf, self.limhf], [
                                   self.limv0, self.limvf], "r--")
            self.im1.set_clim(self.vmin, self.vmax)
            #self.im1.set_clim(np.min(self.X1[self.ind]), np.max(self.X1[self.ind]))
            self.im2.axes.set_ylim([self.pmin, self.pmax])
            self.im2.axes.set_xlim([0, self.cols])
            #self.ax2.set_xlim([0, self.cols])
            self.ax1.set_ylabel("Projection {}".format(self.ind + 1))
            self.ax1.add_artist(scalebar)
            
            if self.contrast==0:

                
                self.ax2.set_ylabel(self.text[self.phase_amp][self.ind])
            else:
                self.ax2.set_ylabel(self.ylabel_contrast[self.phase_amp])
            
            #self.ax2.set_ylabel("Projection {}".format(self.ind + 1))
            self.figure2.tight_layout()
            #self.figure2.tight_layout(pad=0.55)
            self.ax1.axes.figure.canvas.draw()
            self.ax2.axes.figure.canvas.draw()
    
            self.canvas2.draw()
            
            

    def draw_ROI(self):
        
        if self.data_==0:
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
        else:
            
            self.ROI=np.zeros_like(self.X1, dtype=bool)
            self.ROI_mask = self.X1[self.ind, :, :] + self.ROI[self.ind, :, :]
            fig_mask = plt.figure('draw ROI')
            ax_ROI = fig_mask.add_subplot(111)
            ax_ROI.imshow(
                self.ROI_mask,
                cmap=self.colormap,
                #vmin=self.vmin,
                vmin=np.min(self.X1[self.ind]),
                #vmax=self.vmax
                vmax=np.max(self.X1[self.ind]),origin="lower"
            )
            self.RoiDraw = roipoly.roipoly(ax=ax_ROI)
            
            
            self.ROI_=1
        
    def draw_mean(self):

        
        if self.data_==1 and self.ROI_==1:
            
            
            if len(self.RoiDraw.allxpoints)!=0 and len(self.RoiDraw.allypoints)!=0:
                
                mean_ROI=[]
                mean_abs=[]
                msk=self.RoiDraw.getMask(self.ROI_mask)
                msk=msk.astype(int)
                
                if self.phase_amp==0:
                    
                
                    for img in self.X1:
                        tmp1=img*msk
                        tmp2=tmp1[np.nonzero(tmp1)]
                        
                        mean_ROI.append((np.mean(tmp2)))
                    for img in self.X3:
                        tmp1=img*msk
                        tmp2=tmp1[np.nonzero(tmp1)]
                        
                        mean_abs.append((np.mean(tmp2)))  
                        
                else:
                    
                    for img in self.X1_previous_phase:
                        tmp1=img*msk
                        tmp2=tmp1[np.nonzero(tmp1)]
                        
                        mean_ROI.append((np.mean(tmp2)))
                    for img in self.X1:
                        tmp1=img*msk
                        tmp2=tmp1[np.nonzero(tmp1)]
                        
                        mean_abs.append((np.mean(tmp2)))  
                    
                  
                
                mean_ROI=np.array(mean_ROI)
                mean_abs=np.array(mean_abs)
                
                if self.contrast==1:
                    
                    fig_mean,(ax_mean,ax_abs)= plt.subplots(1,2)
                    #ax_mean = fig_mean.add_subplot(111)
                    ax_mean.set_xlabel('energy [KeV]')
                    ax_mean.set_ylabel("delta " "("" \u03B4"")")
                    ax_mean.set_title('Spectra from phase images for sample thickness={} micron'.format(self.dz) , horizontalalignment='center', verticalalignment='top')
                    ax_mean.plot(self.energy,mean_ROI,'bo')
                    
                    ax_abs.set_xlabel('energy [KeV]')
                    ax_abs.set_ylabel("beta " "("" \u03B2"")")
                    ax_abs.set_title('Spectra from absorption images for sample thickness={} micron'.format(self.dz) , horizontalalignment='center', verticalalignment='top')         
                    ax_abs.plot(self.energy,mean_abs,'bo')
                    
                    combined_arr_beta = np.vstack((self.energy, mean_abs*1e5)).T
                    np.savetxt('beta.txt', combined_arr_beta, delimiter=',', header='energy(KeV),absorption(au)', comments='')
                    
                    combined_arr_delta = np.vstack((self.energy, mean_ROI*1e4)).T
                    np.savetxt('delta.txt', combined_arr_delta, delimiter=',', header='energy(KeV),delta(au)', comments='')
                    
                else:
                    
                    fig_mean,(ax_mean,ax_abs) = plt.subplots(1,2)
                    #ax_mean = fig_mean.add_subplot(111)
                    ax_mean.set_xlabel('energy [KeV]')
                    ax_mean.set_ylabel("phase shift [rad]")
                    ax_mean.set_title('phase shift spectra', horizontalalignment='center', verticalalignment='top')
                    ax_mean.plot(self.energy,mean_ROI,'bo')
                    
                    ax_abs.set_xlabel('energy [KeV]')
                    ax_abs.set_ylabel(self.text[1][self.ind])
                    ax_abs.set_title(self.text[1][self.ind].replace(" [a.u.]", "")+' spectra', horizontalalignment='center', verticalalignment='top')         
                    ax_abs.plot(self.energy,mean_abs,'bo')
                    
                    
                plt.tight_layout()    
                plt.show()
            else:
                print("You need to define the ROI")
                QMessageBox.warning(None, 'Error',"You need to define the ROI")
        else:
            print("No data or ROI")
            QMessageBox.warning(None, 'Error',"No data or ROI")
    def draw_var(self):
        

            
        if self.data_==1 and self.ROI_==1:
            
            if len(self.RoiDraw.allxpoints)!=0 and len(self.RoiDraw.allypoints)!=0:
            
            
                var_ROI=[]
                var_abs=[]
                msk=self.RoiDraw.getMask(self.ROI_mask)
                msk=msk.astype(int)
                
                if self.phase_amp==0:
                    
                
                    for img in self.X1:
                        tmp1=img*msk
                        tmp2=tmp1[np.nonzero(tmp1)]
                        
                        var_ROI.append((np.var(tmp2)))
                        
                    for img in self.X3:
                        tmp1=img*msk
                        tmp2=tmp1[np.nonzero(tmp1)]
                        var_abs.append((np.var(tmp2)))
                        
                else:
                    for img in self.X1_previous_phase:
                        tmp1=img*msk
                        tmp2=tmp1[np.nonzero(tmp1)]
                        
                        var_ROI.append((np.var(tmp2)))
                        
                    for img in self.X1:
                        tmp1=img*msk
                        tmp2=tmp1[np.nonzero(tmp1)]
                        var_abs.append((np.var(tmp2)))
                    
                    
                var_ROI=np.array(var_ROI)
                var_abs=np.array(var_abs)
                
                if self.contrast==1:
               
                    fig_var,(ax_var,ax_abs) = plt.subplots(1,2)
                    #ax_var = fig_var.add_subplot(111)
                    ax_var.set_xlabel('energy [KeV]')
                    ax_var.set_ylabel("delta variance")
                    ax_var.set_title('delta variance spectra for sample thickness={} micron' .format(self.dz), horizontalalignment='center', verticalalignment='top')
                    ax_var.plot(self.energy,var_ROI,'-ok',color="blue")
                    
                    ax_abs.set_xlabel('energy [KeV]')
                    ax_abs.set_ylabel("beta variance")
                    ax_abs.set_title('beta variance spectra for sample thickness={} micron'.format(self.dz) , horizontalalignment='center', verticalalignment='top')         
                    ax_abs.plot(self.energy,var_abs,'-ok',color="blue")
                    
                    
                else:
                
                
                    fig_var,(ax_var,ax_abs) = plt.subplots(1,2)
                    #ax_var = fig_var.add_subplot(111)
                    ax_var.set_xlabel('energy [KeV]')
                    ax_var.set_ylabel("phase shift variance")
                    ax_var.set_title('phase variance spectra ', horizontalalignment='center', verticalalignment='top')
                    ax_var.plot(self.energy,var_ROI,'-ok',color="blue")
                    
                    ax_abs.set_xlabel('energy [KeV]')
                    ax_abs.set_ylabel(self.text[1][self.ind].replace(" [a.u.]", "")+" variance")
                    ax_abs.set_title(self.text[1][self.ind].replace(" [a.u.]", "")+' variance spectra ', horizontalalignment='center', verticalalignment='top')
                    ax_abs.plot(self.energy,var_abs,'-ok',color="blue")  
                        
                plt.tight_layout()
                plt.show()
            else:
                print("You need to define the ROI")
                QMessageBox.warning(None, 'Error',"You need to define the ROI")
        else:
            print("No data or ROI")
            QMessageBox.warning(None, 'Error',"No data or ROI")
        
    def draw_std(self):
        
        if self.data_==1 and self.ROI_==1:  
            if len(self.RoiDraw.allxpoints)!=0 and len(self.RoiDraw.allypoints)!=0:
                
            
                std_ROI=[]
                std_abs=[]
                msk=self.RoiDraw.getMask(self.ROI_mask)
                msk=msk.astype(int)
                
                
                if self.phase_amp==0:
                    
                    
                    for img in self.X1:
                        tmp1=img*msk
                        tmp2=tmp1[np.nonzero(tmp1)]
                        
                        std_ROI.append((np.std(tmp2)))
                        
                        
                    for img in self.X3:
                        tmp1=img*msk
                        tmp2=tmp1[np.nonzero(tmp1)]
                        
                        std_abs.append((np.std(tmp2)))
                        
                else:
                    for img in self.X1_previous_phase:
                        tmp1=img*msk
                        tmp2=tmp1[np.nonzero(tmp1)]
                        
                        std_ROI.append((np.std(tmp2)))
                        
                        
                    for img in self.X1:
                        tmp1=img*msk
                        tmp2=tmp1[np.nonzero(tmp1)]
                        
                        std_abs.append((np.std(tmp2))) 

                std_abs=np.array(std_abs) 
                std_ROI=np.array(std_ROI)
                
                if self.contrast==1:
                    
                    fig_std,(ax_std,ax_abs) = plt.subplots(1,2)
                    #ax_std = fig_std.add_subplot(111)
                    ax_std.set_xlabel('energy [KeV]')
                    ax_std.set_ylabel("delta standard deviation")
                    ax_std.set_title('delta standard deviation spectra for sample thickness={} micron' .format(self.dz), horizontalalignment='center', verticalalignment='top')
                    ax_std.plot(self.energy,std_ROI,'-ok',color="blue")
                    
                    ax_abs.set_xlabel('energy [KeV]')
                    ax_abs.set_ylabel("beta standard deviation")
                    ax_abs.set_title('beta standard deviation spectra for sample thickness={} micron'.format(self.dz) , horizontalalignment='center', verticalalignment='top')         
                    ax_abs.plot(self.energy,std_abs,'-ok',color="blue")
                    
                    
                else:
                    fig_std,(ax_std,ax_abs) = plt.subplots(1,2)
                    #ax_std = fig_std.add_subplot(111)
                    ax_std.set_xlabel('energy [KeV]')
                    ax_std.set_ylabel('phase shift standard deviation')
                    ax_std.set_title('phase shift standard deviation spectra ', horizontalalignment='center', verticalalignment='top')
                    ax_std.plot(self.energy,std_ROI,'-ok',color="blue")
                    
                    ax_abs.set_xlabel('energy [KeV]')
                    ax_abs.set_ylabel(self.text[1][self.ind].replace(" [a.u.]", "")+" standard deviation")
                    ax_abs.set_title(self.text[1][self.ind].replace(" [a.u.]", "")+' standard deviation spectra ', horizontalalignment='center', verticalalignment='top')
                    ax_abs.plot(self.energy,std_abs,'-ok',color="blue")
                    
                plt.tight_layout()   
                plt.show()
            else:
                print ("You need to define the ROI")
                QMessageBox.warning(None, 'Error',"You need to define the ROI")
        else:
            print("No data or ROI")
            QMessageBox.warning(None, 'Error',"No data or ROI")
    def draw_mask(self):
        """
        Draw the mask using roipoly
        """
        
        if self.data_==0:
            QMessageBox.warning(None, 'Error',"No data")
            print("No data")
        
        else:
            self.mask = np.zeros_like(self.X1, dtype=bool)
            print("\nDrawing the poly")
            self.img_mask = self.X1[self.ind, :, :] + self.mask[self.ind, :, :]
            # create another fig in order to close later
            fig_mask = plt.figure('draw mask')
            ax_mask = fig_mask.add_subplot(111)
            ax_mask.imshow(
                self.img_mask,
                cmap=self.colormap,
                #vmin=self.vmin,
                vmin=np.min(self.X1[self.ind]),
                #vmax=self.vmax
                vmax=np.max(self.X1[self.ind]),origin="lower"
            )
            self.ROI_draw = roipoly.roipoly(ax=ax_mask)
            
            self.mask_=1
            
    def get_x(self):
        
        if self.data_==0:
            
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
        else :

            self.x_i=eval(self.LineEdit_X.text())

        
    def get_y(self):
        
        if self.data_==0:
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
        else:
            
            self.y_i=eval(self.lineEdit_Y.text())
        
    def plot_intensity_at_pixel(self):
        
        if self.data_==0:
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
        else:
            if self.x_i!=[] and self.y_i!=[]:
                if self.x_i < self.X1.shape[1] and self.y_i< self.X1.shape[2]:
                    fig_pixel = plt.figure()
                    ax_pixel = fig_pixel.add_subplot(111)
                    ax_pixel.set_xlabel('X-ray energies KeV')
                    ax_pixel.set_ylabel('intensity at pixel ({},{})'.format(self.x_i,self.y_i))
                   
                    pixels_values=self.X1[:,self.x_i,self.y_i]
                    ax_pixel.plot(self.energy,pixels_values,'+')
                    plt.show() 
                    print("spectra plotted")
                else:
                    print("\nCan't plot the spectra.Please define correct coordinates ")
                    QMessageBox.warning(None, 'Error',"Can't plot the spectra.Please define correct coordinates")
            else:
                print("(x,y) are not defined")
                QMessageBox.warning(None, 'Error',"(x,y) are not defined")
                

                

    def add_mask(self):
        """
        Add the mask to the plot
        """


        if self.data_==1 and self.mask_==1:
            if len(self.ROI_draw.allxpoints)!=0 and len(self.ROI_draw.allypoints)!=0 :
                
                print("\nAdding mask")
                self.mask[self.ind, :, :] |= self.ROI_draw.getMask(self.img_mask)
                #self.ROI_draw.displayROI()
                
                self.update_pro()
                self.add_mask_=1
                
            
            else:
                print("You need to define the mask")
                QMessageBox.warning(None, 'Error',"You need to define the mask")
                
        else:
            print("No data or Mask")
            QMessageBox.warning(None, 'Error',"No data or Mask")
        
        if self.load_mask_==1:
            
            self.update_pro()
            self.add_mask_=1


    def mask_all(self):
        """
        Use the same mask for all projections
        """
        

            
        if self.data_==1 and self.mask_==1:
            if len(self.ROI_draw.allxpoints)!=0 and len(self.ROI_draw.allypoints)!=0:
                
                print("\nRepeating the same mask for all projections")
                print("Please wait...")
                mask = self.ROI_draw.getMask(self.img_mask)
                self.mask |= np.array([mask for _ in range(self.projs)])
                print("Done")
                self.mask_all_=1
                self.update_pro()
            else:
                print("You need to define the mask")
                QMessageBox.warning(None, 'Error',"You need to define the mask")
        else:
            print("No data or Mask")
            QMessageBox.warning(None, 'Error',"No data or mask")

    def convert_to_delta(self):
        """
        Convert images from phase shifts to integrated delta values
        """
        
        
        if self.data_==0:
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
        else:
            

            
            if self.contrast==1:
                
                print("second time")
                #QMessageBox.warning(None, 'Error',"images already converted")
                self.dz = self.input_dialog.getValue()
    
                if self.dz:
                    
                    
                
                    
                    print(self.dz)
            
                    #     self.label.setText(f'You entered: {value}')
                    # #self.dz=get_thickness()
                    # if value is not None:
                    #     self.label.setText(f'You entered: {value}')
            
                    if self.phase_amp==0:
                        
                        
                        for ii in range(self.projs):
                            
                            strbar = "Projection {} out of {}".format(ii + 1, self.projs)
                            self.X1[ii], factor = convert_phase2delta(
                                self.before_delta[ii],
                                self.energy[ii],self.dz)
                            self.X3[ii],_ = convert_to_beta(
                                 self.before_beta[ii],
                                 self.energy[ii],self.dz)
                             
                            
                            
                            self.X2[ii] = self.X1[ii, self.hcen, :].copy()
                            progbar(ii + 1, self.projs, strbar)
                            
                            
                    else:

                        for ii in range(self.projs):
                            strbar = "Projection {} out of {}".format(ii + 1, self.projs)
                            self.X1[ii],_ = convert_to_beta(
                                self.before_beta[ii],
                                self.energy[ii],self.dz)
                            self.X1_previous_phase[ii],factor = convert_phase2delta(
                                 self.before_delta[ii],
                                 self.energy[ii],self.dz)
                            
                            
                            
                            self.X2[ii] = self.X1[ii, self.hcen, :].copy()
                            progbar(ii + 1, self.projs, strbar)
                        
                        
                    print("\r")
                    print("Done")
                    # factor is negative so that we need to exchange vmin and vmax
                    # self.vmin = self.vmax*(factor)
                    # self.vmax = self.vmin*(factor)
                    # self.pmin, self.pmax = self.vmin, self.vmax
                    # self.var1=True
                    self.update_pro()
                    self.update_list()
                    QMessageBox.information(None, "Processing Done", "conversion to delta contrast is completed")
                
                
                
                
                
                
            else:
                print("first time")
            
                self.dz = self.input_dialog.getValue()
    
                if self.dz:
                    
                    
                
                    
                    print(self.dz)
            
                    #     self.label.setText(f'You entered: {value}')
                    # #self.dz=get_thickness()
                    # if value is not None:
                    #     self.label.setText(f'You entered: {value}')
            
                    if self.phase_amp==0:
                        
                        self.before_delta=self.X1.copy()
                        self.before_beta=self.X3.copy()
                        for ii in range(self.projs):
                            
                            strbar = "Projection {} out of {}".format(ii + 1, self.projs)
                            self.X1[ii], factor = convert_phase2delta(
                                self.X1[ii],
                                self.energy[ii],self.dz)
                            self.X3[ii],_ = convert_to_beta(
                                 self.X3[ii],
                                 self.energy[ii],self.dz)
                             
                            
                            
                            self.X2[ii] = self.X1[ii, self.hcen, :].copy()
                            progbar(ii + 1, self.projs, strbar)
                            
                            
                    else:
                        self.before_delta=self.X1_previous_phase.copy()
                        self.before_beta=self.X1.copy()
                        for ii in range(self.projs):
                            strbar = "Projection {} out of {}".format(ii + 1, self.projs)
                            self.X1[ii],_ = convert_to_beta(
                                self.X1[ii],
                                self.energy[ii],self.dz)
                            self.X1_previous_phase[ii],factor = convert_phase2delta(
                                 self.X1_previous_phase[ii],
                                 self.energy[ii],self.dz)
                            
                            
                            
                            self.X2[ii] = self.X1[ii, self.hcen, :].copy()
                            progbar(ii + 1, self.projs, strbar)
                        
                        
                    print("\r")
                    print("Done")
                    # factor is negative so that we need to exchange vmin and vmax
                    self.vmin = self.vmax*(factor)
                    self.vmax = self.vmin*(factor)
                    self.contrast=1
                    self.pmin, self.pmax = self.vmin, self.vmax
                    self.var1=True
                    self.update_pro()
                    self.update_list()
                    QMessageBox.information(None, "Processing Done", "conversion to delta contrast is completed")
                    
                else:
                    #QMessageBox.warning(None, 'Error',"Please define the sample thickness in micron")
                    print("Please define the sample thickness in micron")
    def apply_mask(self):
        """
        Apply the linear phase correction using current mask
        """
        

            
        if self.data_==1 and self.mask_==1 and self.add_mask_==1:
            if len(self.ROI_draw.allxpoints)!=0 and len(self.ROI_draw.allypoints)!=0 :
                print("\nApply the linear phase correction using current mask")
                self.X1[self.ind] = removing_phaseramp(
                    self.X1[self.ind],
                    self.mask[self.ind],
                )
                self.X2[self.ind] = self.X1[self.ind, self.hcen, :].copy()
                self.update_list()
                self.update_pro()
                
                QMessageBox.information(None, "Processing Done", "constant and ramp removal of image "+ str(self.ind+1)+" is done")
            else:
                print("You need to define mask")
                QMessageBox.warning(None, 'Error',"You need to define mask")
                
                
                
        elif self.load_mask_==1:
            
            print("\nApply the linear phase correction using current mask")
            self.X1[self.ind] = removing_phaseramp(
                self.X1[self.ind],
                self.mask[self.ind],
            )
            self.X2[self.ind] = self.X1[self.ind, self.hcen, :].copy()
            self.update_list()
            self.update_pro()
            QMessageBox.information(None, "Processing Done", "constant and ramp removal of image "+ str(self.ind+1)+" is done")
        else:
            
            print("No data or mask")
            QMessageBox.warning(None, 'Error',"No data or mask")
            
            
    def Normalization(self):
        """
        Normalization using current mask
        """


            
        if self.data_==1 and self.mask_==1 and self.add_mask_==1:
            if len(self.ROI_draw.allxpoints)!=0 and len(self.ROI_draw.allypoints)!=0 :
                print("\nNormalization using current mask")
                self.X1[self.ind] = air_normalization(
                    self.X1[self.ind],
                    self.mask[self.ind],
                )
                self.X2[self.ind] = self.X1[self.ind, self.hcen, :].copy()
                self.text[self.phase_amp][self.ind]="Normalized amplitude [a.u.]"
                self.update_list()
                self.update_pro()
                
                QMessageBox.information(None, "Processing Done", "Normalization of image "+ str(self.ind+1)+" is done")
            else:
                print("You need to define mask")
                QMessageBox.warning(None, 'Error',"You need to define mask")
                
                
                
        elif self.load_mask_==1:
            
            print("\nNormalization using current mask")
            self.X1[self.ind] = air_normalization(
                self.X1[self.ind],
                self.mask[self.ind],
            )
            self.X2[self.ind] = self.X1[self.ind, self.hcen, :].copy()
            self.update_list()
            self.update_pro()
            QMessageBox.information(None, "Processing Done", "Normalization of image "+ str(self.ind+1)+" is done")
        else:
            
            print("No data or mask")
            QMessageBox.warning(None, 'Error',"No data or mask")
            
            
    def apply_all_masks(self):
        """
        Apply the linear phase correction using current mask to all projections
        """

            
        if self.data_==1 and self.mask_==1 and self.mask_all_==1:
            
            if len(self.ROI_draw.allxpoints)!=0 and len(self.ROI_draw.allypoints)!=0 :
                print(
                    "\nApply the linear phase correction using current mask to all projections"
                )
                for ii in range(self.projs):
                    self.ind = ii
                    strbar = "Projection {} out of {}".format(ii + 1, self.projs)
                    self.X1[ii] = removing_phaseramp(
                        self.X1[ii],
                        self.mask[ii],
                    )
                    self.X2[ii] = self.X1[ii, self.hcen, :].copy()
        
                    #self.update_pro()
                    progbar(ii + 1, self.projs, strbar)
                print("\r")
                print("Done")
                self.update_list()
                self.update_pro()
                QMessageBox.information(None, "Processing Done", "constant and ramp removal of all images is done")
            else:
                print("You need to define mask")
                QMessageBox.warning(None, 'Error',"You need to define mask")
                
                
        elif self.load_mask_==1:
            
            
            print("\nApply the linear phase correction using current mask")
            for ii in range(self.projs):
                self.ind = ii
                strbar = "Projection {} out of {}".format(ii + 1, self.projs)
                self.X1[ii] = removing_phaseramp(
                    self.X1[ii],
                    self.mask[ii],
                )
                self.X2[ii] = self.X1[ii, self.hcen, :].copy()
    
                #self.update_pro()
                progbar(ii + 1, self.projs, strbar)
            print("\r")
            print("Done")
            self.update_list()
            self.update_pro()
            QMessageBox.information(None, "Processing Done", "constant and ramp removal of all images is done")
        else:
            print("No data or mask")
            QMessageBox.warning(None, 'Error',"No data or mask")
            
            
            
    def Normalization_all(self):
        """
        Normalization of all projections using current mask
        """

            
        if self.data_==1 and self.mask_==1 and self.mask_all_==1:
            
            if len(self.ROI_draw.allxpoints)!=0 and len(self.ROI_draw.allypoints)!=0 :
                print(
                    "\nNormalization of all projections using current mask"
                )
                for ii in range(self.projs):
                    
                    
                    if self.text[self.phase_amp][ii]=="Normalized amplitude [a.u.]":
                        
                        print("skip! already normalized")
                        
                    else:
                        
                        self.ind = ii
                        strbar = "Projection {} out of {}".format(ii + 1, self.projs)
                        self.X1[ii] = air_normalization(
                            self.X1[ii],
                            self.mask[ii],
                        )
                        self.X2[ii] = self.X1[ii, self.hcen, :].copy()
                        self.text[self.phase_amp][self.ind]="Normalized amplitude [a.u.]"
        
                    #self.update_pro()
                        progbar(ii + 1, self.projs, strbar)
                print("\r")
                print("Done")
                self.update_list()
                self.update_pro()
                QMessageBox.information(None, "Processing Done", "All images are normalized")
            else:
                print("You need to define mask")
                QMessageBox.warning(None, 'Error',"You need to define mask")
                
                
        elif self.load_mask_==1:
            
            
            print(
                "\nNormalization of all projections using current mask"
            )
   
            
            for ii in range(self.projs):
                
                
                if self.text[self.phase_amp][ii]=="Normalized amplitude [a.u.]":
                    
                    print("skip! already normalized")
                    
                else:
                    
                    self.ind = ii
                    strbar = "Projection {} out of {}".format(ii + 1, self.projs)
                    self.X1[ii] = air_normalization(
                        self.X1[ii],
                        self.mask[ii],
                    )
                    self.X2[ii] = self.X1[ii, self.hcen, :].copy()
                    self.text[self.phase_amp][self.ind]="Normalized amplitude [a.u.]"
    
                #self.update_pro()
                    progbar(ii + 1, self.projs, strbar)
            print("\r")
            print("Done")
            self.update_list()
            self.update_pro()
            
            
            
        else:
            print("No data or mask")
            QMessageBox.warning(None, 'Error',"No data or mask")
            
            
            
    def remove_mask(self):
        """
        Remove the current selected area from the mask
        """
        
        if self.data_==1 and self.mask_==1 and self.add_mask_==1:
            if len(self.ROI_draw.allxpoints)!=0 and len(self.ROI_draw.allypoints)!=0 :
                
            
            
                print("\nRemoving mask")
                self.mask[self.ind, :, :] &= ~self.ROI_draw.getMask(self.img_mask)
        
                self.update_pro()
                self.add_mask_=0
                #self.mask_=0
                
            else:
                print("No mask to remove")
                QMessageBox.warning(None, 'Error',"No mask to remove")
                self.update_pro()
                
        elif self.load_mask_==1:
            
            self.mask[self.ind,:,:] = np.zeros_like(self.X1[self.ind,:,:], dtype=bool)
            self.add_mask_=0
            self.update_pro()
        else:
            print("No data or mask")
            QMessageBox.warning(None, 'Error',"No data or mask")
            

    def remove_all_mask(self):
        """
        Remove all the masks
        """

        if self.data_==1 and self.mask_==1 and self.mask_all_==1:
            if len(self.ROI_draw.allxpoints)!=0 and len(self.ROI_draw.allypoints)!=0 :
                print("\nRemoving all mask")
                print("Please wait...")
                mask = self.ROI_draw.getMask(self.img_mask)
                # self.mask[self.mask_ind,:,:] &= ~self.ROI_draw.getMask(self.img_mask)
                self.mask &= ~np.array([mask for _ in range(self.projs)])
                print("Done")
        
                self.update_pro()
                self.mask_all_=0
                self.mask_=0
            else:
                print("No mask to remove")
                QMessageBox.warning(None, 'Error',"No mask to remove")
                self.update_pro()
                
                
                
        elif self.load_mask_==1:
            self.mask = np.zeros_like(self.X1, dtype=bool)
            self.mask_all_=0
            self.mask_=0
            self.update_pro()        

        else:
            print("No data or mask")
            QMessageBox.warning(None, 'Error',"No data or mask")
            

    
    def unwrapping_phase(self, event):
        """
        Unwrap phase
        """
        
        
        if self.data_==0:
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
        else:
            
        
            print(f"\nUnwrapping phase projection {self.ind}")
            self.X1[self.ind] = unwrapping_phase(
                self.X1[self.ind],
                self.mask[self.ind]
            )
            self.X2[self.ind] = self.X1[self.ind, self.hcen, :].copy()
    
            self.update_pro()
            self.update_list()
            QMessageBox.information(None, "Processing Done", "unwrapping of image "+ str(self.ind+1)+" is done")
            
            
    def convert_mudz(self, event):
        """
        Converting to linear attenuation coefficient times thickness
        """
        
        
        if self.data_==0:
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
        else:
            
        
            print(f"\nConverting to linear attenuation coefficient times thickness {self.ind}")
            
            if self.text[self.phase_amp][self.ind]=="\u03BC*sample thickness [a.u.]":
                print("skip! already converted")
                
            else:
                
                self.X1[self.ind] = convert_to_mudz(
                    self.X1[self.ind]
                )
                self.X2[self.ind] = self.X1[self.ind, self.hcen, :].copy()
                
                self.text[self.phase_amp][self.ind]="\u03BC*sample thickness [a.u.]"
            
                self.update_pro()
                self.update_list()
                QMessageBox.information(None, "Processing Done", "converting of image "+ str(self.ind+1)+" is done")
    def unwrapping_all(self, event):
        """
        Unwrap phase of all projections
        """
        if self.data_==0:
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
            
        else:
            
            print("\nUnwrapping all projections")
            for ii in range(self.projs):
                self.ind = ii
                strbar = "Projection {} out of {}".format(ii + 1, self.projs)
                self.X1[ii] = unwrapping_phase(
                    self.X1[ii],
                    self.mask[ii]
                )
                self.X2[self.ind] = self.X1[self.ind, self.hcen, :].copy()
    
                self.update_pro()
                progbar(ii + 1, self.projs, strbar)
            print("\r")
            print("Done")
        self.update_pro()
        self.update_list()
        QMessageBox.information(None, "Processing Done", "unwrapping of all images is done")
        
    def convert_mudz_all(self, event):
        """
        Converting all images
        """
        if self.data_==0:
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
            
        else:
            
            print("\nConverting all images")
            for ii in range(self.projs):
                
                
                if self.text[self.phase_amp][ii]=="\u03BC*sample thickness [a.u.]":
                    
                    print("skip! already converted")
                    
                
                else:
                    
                
                
                    self.ind = ii
                    strbar = "Projection {} out of {}".format(ii + 1, self.projs)
                    self.X1[ii] = convert_to_mudz(
                        self.X1[ii]
                    )
                    
                    self.text[self.phase_amp][ii]="\u03BC*sample thickness [a.u.]"
                    self.X2[self.ind] = self.X1[self.ind, self.hcen, :].copy()
        
                    self.update_pro()
                    progbar(ii + 1, self.projs, strbar)
            print("\r")
            print("Done")
        self.update_pro()
        self.update_list()
        QMessageBox.information(None, "Processing Done", "Converting of all images is done")
    def save_masks(self):
        
        """
        Save mask to file
        """
        
        if self.data_==0:
                print("Nothing to save")
                QMessageBox.warning(None, 'Error',"Nothing to save")
        else:
            
            
                options = QFileDialog.Options()
                options |= QFileDialog.DontUseNativeDialog
                fileName= QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
                if fileName[0] and self.mask_==1:
                    if len(self.ROI_draw.allxpoints)!=0 and len(self.ROI_draw.allypoints)!=0 :
                    
                
                        p1=fileName[0]
            
                        p2='.npz'
                        outputfname=p1+p2
                        mask=np.zeros_like(self.X1,dtype=bool)
                        
                        mask[:,:,:] = self.ROI_draw.getMask(self.img_mask)
                        
                        #np.savez('airmask', mask=self.mask)
                        np.savez(outputfname,mask=mask)
                        QMessageBox.information(None, "Processing Done", "mask saved")
                    else:
                       QMessageBox.warning(None, 'Error',"Mask not defined correctly") 

                else:
                    print("Please select a directory for saving")
                    #QMessageBox.warning(None, 'Error',"Please select a directory for saving")

    def load_masks(self, event):
        """
        Load masks from file
        """
        
        if self.data_==0:
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
        else:
            
            
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName,_= QFileDialog.getOpenFileName(self,"Load Mask","","NPZ Files (*.npz)", options=options)
            if fileName:
                
                
                data = np.load(fileName)
                if "mask" in data:
                    if data["mask"].shape==self.X1[:,:,:].shape:
                        
                        self.mask=data["mask"]
                        self.load_mask_=1
                        QMessageBox.information(None, "Processing Done", "mask loaded")
                    else:
                        QMessageBox.warning(None, 'Error',"loaded mask doesn't have the same shape as the current images ")
                        
                    
                else:
                    QMessageBox.warning(None, 'Error',"No mask found in this file ")
            
            else:
                print("ok")
            
            
            # print("\nLoad masks from file")
            # with np.load('airmask.npz') as data:
            #     self.mask = data['mask']
    
            self.update_pro()

    def interpolate(self):
        """
        Inteporlate the pixel size of input image accordingly to the highest energy
        """
        if self.data_==0:
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
        else:
            
        
            print("\nInterpolate the image accross the different energies")
    
    
    
            if self.phase_amp==0:
                
                for ii in range(self.projs):
                    self.ind = ii
                    strbar = "Projection {} out of {}".format(ii+1, self.projs)
                    imgin = self.X1[ii].copy()
                    imgin2=self.X3[ii].copy()
                    self.X1[ii] = interp_spectral(
                        imgin,
                        self.pixel[ii][0],
                        self.energy[ii],
                        self.X1[self.maxind],
                        self.pxmaxenergy,
                        self.maxenergy,
                    )
                    
                    
                    self.X3[ii] = interp_spectral(
                        imgin2,
                        self.pixel[ii][0],
                        self.energy[ii],
                        self.X3[self.maxind],
                        self.pxmaxenergy,
                        self.maxenergy,
                        )+1e-12
                    
                    progbar(ii+1, self.projs, strbar)
            else:
                
                for ii in range(self.projs):
                    self.ind = ii
                    strbar = "Projection {} out of {}".format(ii+1, self.projs)
                    imgin = self.X1[ii].copy()
                    imgin2=self.X1_previous_phase[ii].copy()
                    self.X1[ii] = interp_spectral(
                        imgin,
                        self.pixel[ii][0],
                        self.energy[ii],
                        self.X1[self.maxind],
                        self.pxmaxenergy,
                        self.maxenergy,
                    )+1e-12
                    
                    
                    self.X1_previous_phase[ii] = interp_spectral(
                        imgin2,
                        self.pixel[ii][0],
                        self.energy[ii],
                        self.X1_previous_phase[self.maxind],
                        self.pxmaxenergy,
                        self.maxenergy,
                        )
                    
                    progbar(ii+1, self.projs, strbar)
                
                
                
                

            print("\r")
            print("Done")
            self.update_pro()
            QMessageBox.information(None, "Processing Done", "interpolation is done")
            self.update_list()
    def align_all(self):
        """
        Align all the images with subpixel precision
        """
        
        if self.data_==0:
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
        else:
            
            
            
            if self.phase_amp==1 and self.use_shifts==1:
                print("using shifts estimated from phase contrast images ")
                
                for ii in range(self.projs):
                    
                    self.shift[self.phase_amp,:]= self.shift[0,:]
                    self.X1[ii] = shift_image(self.X1[ii], shift=self.shift[0,ii])
                QMessageBox.information(None, "Processing Done", "alignement is done")
            
            elif self.phase_amp==1 and self.use_shifts==0:
                
                QMessageBox.warning(None, 'Error',"Please estimate shifts using phase contrast images")
                
            
            else:
            
            
                print("\nAlignment of the images accross the different energies")
                print('Estimating shifts')
                self.shift = np.zeros((2,self.projs, 2))
                # The reference is the projection at the highest energy
                refimg = self.X1[
                    self.maxind,
                    self.limv0:self.limvf,
                    self.limh0:self.limhf,
                ].copy()
                for ii in range(self.projs):
                    print(f"\nEnergy of {self.energy[ii]:0.4f} keV")
                    if self.energy[ii] == self.maxenergy:
                        print("The highest energy. It must have 0 shift")
                    offsetimg = self.X1[
                        ii,
                        self.limv0:self.limvf,
                        self.limh0:self.limhf
                    ]
                    self.shift[self.phase_amp,ii], error, diffphase = phase_cross_correlation(
                        refimg,
                        offsetimg,
                        # upsample_factor=100,
                        # overlap_ratio=0.9,
                    )
                    print(f"Offset for image {ii+1}  (y,x): {self.shift[self.phase_amp,ii]}")
                    print(f"Shifting the image to align it")
                    self.X1[ii] = shift_image(self.X1[ii], shift=self.shift[self.phase_amp,ii])
                    self.use_shifts=1
                    #self.X03[ii]=shift_image(self.X03[ii],shift=self.shift[self.phase_amp,ii])+1e-12
                self.update_pro()
                self.update_list()
                QMessageBox.information(None, "Processing Done", "alignement is done")


    def plot_shifts(self, event):
        """
        Plot the shifts
        """
        

        if self.data_==0:
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
        else:
            
            fig_shifts = plt.figure()
            ax_shifts = fig_shifts.add_subplot(111)
            ax_shifts.plot(self.shift[self.phase_amp,:, 0], 'ro-', label="Vertical")
            ax_shifts.plot(self.shift[self.phase_amp,:, 1], 'b*--', label="Horizontal")
            ax_shifts.set_xlabel('image index')
            ax_shifts.set_ylabel('shifts in pixels')
            
            plt.legend()
            plt.show()

    def show_diff(self, event):
        """
        Display the difference between current image and image
        at the highest energy. The RMS value is displayed
        """
        if self.data_==0:
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
        else:
            
        
            offsetimg = self.X1[self.ind].copy()
            diffimg = np.abs(offsetimg-self.X1[self.maxind])
            rms = np.sqrt(np.sum(diffimg**2))
            fig_diff = plt.figure()
            ax_diff = fig_diff.add_subplot(111)
            ax_diff.imshow(
                diffimg,
                cmap=self.colormap,
                vmin=self.pmin,
                vmax=self.pmax, origin="lower"
            )
            ax_diff.set_title("RMS: {}".format(rms))
            plt.show()

    def moveleft(self):
        """
        Move image left
        """
        
        print("here")
        if self.data_==0:
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
        else:
            
            print("Moving left")
            self.shift[self.phase_amp,self.ind, 1] -= self.alignpixel
            
            self.shift[np.abs(self.phase_amp-1),self.ind,1]=self.shift[self.phase_amp,self.ind, 1]
            
            if self.phase_amp==0:
                self.X1[self.ind] = shift_image(
                     self.X1[self.ind], (0, -self.alignpixel))
                
                self.X3[self.ind] = shift_image(
                     self.X3[self.ind], (0, -self.alignpixel))+1e-12
            else:
                self.X1[self.ind] = shift_image(
                     self.X1[self.ind], (0, -self.alignpixel))+1e-12
                self.X1_previous_phase[self.ind]=shift_image(self.X1_previous_phase[self.ind],(0, -self.alignpixel))
                
           
            
           
            # self.X1[self.ind] = shift_image(
            #     self.X1[self.ind], (0, -self.alignpixel))+1e-12
              
            # self.X03[self.ind] = shift_image(
            #     self.X03[self.ind], (0, -self.alignpixel))+1e-12
                
            
            self.X2[self.ind] = self.X1[self.ind, self.hcen, :].copy()
            self.update_pro()
            self.update_list()
    def moveright(self):
        """
        Move image right
        """
        if self.data_==0:
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
        else:
            
        
            print("Moving right")
            self.shift[self.phase_amp,self.ind, 1] += self.alignpixel
            self.shift[np.abs(self.phase_amp-1),self.ind,1]=self.shift[self.phase_amp,self.ind, 1]
            
            if self.phase_amp==0:
                
            
                self.X1[self.ind] = shift_image(
                    self.X1[self.ind], (0, self.alignpixel))
                
            
                self.X3[self.ind] = shift_image(
                    self.X3[self.ind], (0, self.alignpixel))+1e-12    
            
            
            else:
                self.X1[self.ind] = shift_image(
                    self.X1[self.ind], (0, self.alignpixel))+1e-12
                
                self.X1_previous_phase[self.ind]=shift_image(
                    self.X1_previous_phase[self.ind], (0, self.alignpixel))
                
                
                
                
            
            self.X2[self.ind] = self.X1[self.ind, self.hcen, :].copy()
            self.update_pro()
            self.update_list()
    def moveup(self):
        """
        Move image up
        """
        
        if self.data_==0:
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
        else:
            
        
            print("Moving up")
            self.shift[self.phase_amp,self.ind, 0] -= self.alignpixel
            self.shift[np.abs(self.phase_amp-1),self.ind,0]= self.shift[self.phase_amp,self.ind, 0]
            
            
            if self.phase_amp==0:
                
                self.X1[self.ind] = shift_image(
                    self.X1[self.ind], (-self.alignpixel, 0))
                self.X3[self.ind] = shift_image(
                    self.X3[self.ind], (-self.alignpixel, 0))+1e-12  
                
            else:
                self.X1[self.ind] = shift_image(
                    self.X1[self.ind], (-self.alignpixel, 0))+1e-12
                self.X1_previous_phase[self.ind]=shift_image(
                    self.X1_previous_phase[self.ind], (-self.alignpixel, 0))
                
             
            self.X2[self.ind] = self.X1[self.ind, self.hcen, :].copy()
            self.update_pro()
            self.update_list()
    def movedown(self):
        """
        Moveimage down
        """
        if self.data_==0:
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
        else:
            
        
            print("Moving down")
            self.shift[self.phase_amp,self.ind, 0] += self.alignpixel
            self.shift[np.abs(self.phase_amp-1),self.ind,0]= self.shift[self.phase_amp,self.ind, 0]
            
            
            
            if self.phase_amp==0:
                
                self.X1[self.ind] = shift_image(
                self.X1[self.ind], (self.alignpixel, 0))
            
                self.X3[self.ind] = shift_image(
                self.X3[self.ind], (self.alignpixel, 0))+1e-12
            
            else:
               self.X1[self.ind] = shift_image(
                   self.X1[self.ind], (self.alignpixel, 0))+1e-12
               
               self.X1_previous_phase[self.ind] = shift_image(
                   self.X1_previous_phase[self.ind], (self.alignpixel, 0))
            
             
            # self.X03[self.ind] = shift_image(
            #     self.X03[self.ind], (self.alignpixel, 0))+1e-12
             
            self.X2[self.ind] = self.X1[self.ind, self.hcen, :].copy()
            self.update_pro()
            self.update_list()
    def cropleft(self):
        """
        Crop images left
        """
        if self.data_==0:
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
        else:
            
            cropv = self.cropval
            self.cl += cropv
            print("Cropping {} pixels left".format(self.cl))
    
            self.update_pro()

    def cropright(self):
        """
        Crop images right
        """
        if self.data_==0:
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
        else:
            
        
            cropv = self.cropval
            self.cr += cropv
            print("Cropping {} pixels right".format(self.cr))
    
            self.update_pro()

    def croptop(self):
        """
        Crop images top
        """
        if self.data_==0:
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
        else:
            
        
            cropv = self.cropval
            self.ct += cropv
            print("Cropping {} pixels top".format(self.ct))

            self.update_pro()

    def cropbottom(self):
        """
        Crop images down
        """
       
        
        if self.data_==0:
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
        else:
            print(self.cb)
            cropv = self.cropval
            self.cb += cropv
            print("Cropping {} pixels bottom".format(self.cb))

            self.update_pro()

    def croparray(self, event):
        """
        Definitive cropping of the image
        """
        

        
        if self.data_==0:
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
        else:
            if self.phase_amp==0:
                
                self.X1 = self.X1[:, self.limv0:self.limvf, self.limh0:self.limhf]
                self.X3=self.X3[:, self.limv0:self.limvf, self.limh0:self.limhf]
            else:
                self.X1 = self.X1[:, self.limv0:self.limvf, self.limh0:self.limhf]
                self.X1_previous_phase=self.X1_previous_phase[:, self.limv0:self.limvf, self.limh0:self.limhf]
            #self.X03 = self.X03[:, self.limv0:self.limvf, self.limh0:self.limhf]
            self.projs, self.rows, self.cols = self.X1.shape
            self.hcen = int(self.rows / 2.0)
            self.X2 = self.X1[:, self.hcen, :].copy()
            self.cl, self.cr, self.ct, self.cb = 0, 0, 0, 0
            
            
            self.update_list()
            self.update_pro()
    def resetselection(self, event):
        """
        Definitive cropping of the image
        """
        
        if self.data_==0:
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
        else:
            
            self.cl, self.cr, self.ct, self.cb = 0, 0, 0, 0
    
            self.update_pro()



    def cmvmin(self):
        """
        Set the vmin equals to ``val`` on colormap
        """
        
        if self.data_==0:
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
        else:
            
            val = self.VMIN.text()
            val=(val.replace(',', '.'))
            if eval(val) >= self.vmax:
                print("vmin is equal or larger than vmax. Choose smaller value")
                QMessageBox.warning(None, 'Error',"vmin is equal or larger than vmax. Choose smaller value")
            else:
                self.vmin = eval(val)  # np.clip(eval(val), 0, self.vmax - 1)
                self.pmin = self.vmin
    
                self.update_org()
                self.update_pro()

    def cmvmax(self):
        """
        Set the vmax equals to ``val`` on colormap
        """
        
        if self.data_==0:
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
        else:
            
            val = self.VMAX.text()
            val=(val.replace(',', '.'))
            if eval(val) <= self.vmin:
                print("vmax is equal or smaller than vmin. Choose larger value")
                QMessageBox.warning(None, 'Error',"vmax is equal or smaller than vmin. Choose larger value")
            else:
                self.vmax = eval(val)
                self.pmax = self.vmax
    
                self.update_org()
                self.update_pro()
            
    def cmvmin_org(self):
        """
        Set the vmin equals to ``val`` on colormap
        """
        if self.data_==0:
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
        else:
            
            val = self.VMIN_2.text()
            val=(val.replace(',', '.'))
            if eval(val) >= self.vmax_2:
                print("vmin is equal or larger than vmax. Choose smaller value")
                QMessageBox.warning(None, 'Error',"vmin is equal or larger than vmax. Choose smaller value")
            else:
                self.vmin_2 = eval(val)  # np.clip(eval(val), 0, self.vmax - 1)
                #self.pmin = self.vmin
    
                self.update_org()
            

    def cmvmax_org(self):
        """
        Set the vmax equals to ``val`` on colormap
        """
        if self.data_==0:
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
        else:
            
        
            val = self.VMAX_2.text()
            val=(val.replace(',', '.'))
            print(val)
            if eval(val) <= self.vmin_2:
                print("vmax is equal or smaller than vmin. Choose larger value")
                QMessageBox.warning(None, 'Error',"vmax is equal or smaller than vmin. Choose larger value")
            else:
                
                self.vmax_2 = eval(val)
                #self.pmax = self.vmax
    
                self.update_org()
            

    def setalignpixel(self):
        """
        Set the amount of pixels to manual alignment
        """

        if self.data_==0:
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
        else:
            
            self.alignpixel = eval((self.lineEdit_Alignment.text()))
            print("Aligning with {} pixel precision".format(self.alignpixel))

    def setcropval(self):
        """
        Set the amount of pixels to crop
        """

        if self.data_==0:
            print("No data")
            QMessageBox.warning(None, 'Error',"No data")
        else:
            
            self.cropval = int(eval(self.lineEdit_StepCrop.text()))
            print("Setting cropping value to {} pixels".format(self.cropval))

    def save_projection(self):

        if self.data_==0:
            print("Nothing to save")
            QMessageBox.warning(None, 'Error',"Nothing to save")
        else:
            

                
                
        
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName= QFileDialog.getSaveFileName(self,"save projection","","All Files (*)", options=options)
            if fileName[0]:
            
                p1=fileName[0]
    
                p2='.npz'
                outputfname=p1+p2
                np.savez(outputfname,pixel=self.pixel[self.ind],energy=self.energy[self.ind],projection=self.X1[self.ind])
                QMessageBox.information(None, "Processing Done", "saving of image "+str(self.ind+1)+" is done")
            else:
                print("Please select a directory for saving")

    def save_all_projection(self):

        
        if self.data_==0:
            print("Nothing to save")
            QMessageBox.warning(None, 'Error',"Nothing to save")
        else:
            
            

            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName = QFileDialog.getSaveFileName(self,"save all projections","","All Files (*)", options=options)
            if fileName[0]:
                p1=fileName[0]
                
                p2='.npz'
                outputfname=p1+p2
                
                np.savez(outputfname,self.X1,pixel=self.pixel,energy=self.energy,projection=self.X1)
                QMessageBox.information(None, "Processing Done", "saving of all images is done")
            else:
                print("Please select a directory for saving")
  
    
        


if __name__ == "__main__":

    

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    QtWidgets.QApplication.processEvents()
    sys.exit(app.exec_())

