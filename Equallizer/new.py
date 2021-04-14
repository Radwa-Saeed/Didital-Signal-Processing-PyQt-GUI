# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QSlider
from PyQt5 import QtCore, QtGui, QtWidgets ,QtPrintSupport
import pandas as pd
import numpy as np
import os
import sys
from pyqtgraph import PlotWidget ,PlotItem
import pathlib
import pyqtgraph as pg 
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from scipy.fftpack import rfft
import scipy.fftpack as fftpk
import scipy
from scipy.io import wavfile
import math
import librosa

class Ui_MainWindow(QtGui.QMainWindow):
# class Ui_MainWindow(object):
    gain=[]
    fftband1=[]
    fftband2=[]
    fftband3=[]
    fftband4=[]
    fftband5=[]
    equalizers=[]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(984, 894)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setFocusPolicy(QtCore.Qt.WheelFocus)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.signal_1 = PlotWidget(self.centralwidget)
        self.signal_1.setGeometry(QtCore.QRect(22, 39, 461, 192))
        self.signal_1.setStyleSheet("background-color:rgb(0, 0, 0);")
        self.signal_1.setRubberBandSelectionMode(QtCore.Qt.IntersectsItemBoundingRect)
        self.signal_1.setObjectName("signal_1")
        self.spectro_3 = QtWidgets.QGraphicsView(self.centralwidget)
        self.spectro_3.setGeometry(QtCore.QRect(490, 649, 471, 192))
        self.spectro_3.setObjectName("spectro_3")
        self.spectro_1 = QtWidgets.QGraphicsView(self.centralwidget)
        self.spectro_1.setGeometry(QtCore.QRect(492, 39, 471, 192))
        self.spectro_1.setObjectName("spectro_1")
        self.signal_3 = PlotWidget(self.centralwidget)
        self.signal_3.setGeometry(QtCore.QRect(20, 649, 461, 192))
        self.signal_3.setStyleSheet("background-color:rgb(0, 0, 0);")
        self.signal_3.setRubberBandSelectionMode(QtCore.Qt.IntersectsItemBoundingRect)
        self.signal_3.setObjectName("signal_3")
        self.Zoom_in = QtWidgets.QPushButton(self.centralwidget)
        self.Zoom_in.setGeometry(QtCore.QRect(211, 269, 41, 51))
        self.Zoom_in.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("zoom-in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Zoom_in.setIcon(icon)
        self.Zoom_in.setIconSize(QtCore.QSize(30, 30))
        self.Zoom_in.setObjectName("Zoom_in")
        self.zoom_out = QtWidgets.QPushButton(self.centralwidget)
        self.zoom_out.setGeometry(QtCore.QRect(258, 269, 42, 51))
        self.zoom_out.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("zoom-ou.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_out.setIcon(icon1)
        self.zoom_out.setIconSize(QtCore.QSize(30, 30))
        self.zoom_out.setObjectName("zoom_out")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(306, 269, 41, 51))
        self.clear.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("eraser.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear.setIcon(icon2)
        self.clear.setIconSize(QtCore.QSize(30, 30))
        self.clear.setObjectName("clear")
        self.pause = QtWidgets.QPushButton(self.centralwidget)
        self.pause.setGeometry(QtCore.QRect(115, 269, 42, 51))
        self.pause.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause.setIcon(icon3)
        self.pause.setIconSize(QtCore.QSize(30, 30))
        self.pause.setObjectName("pause")
        self.play = QtWidgets.QPushButton(self.centralwidget)
        self.play.setGeometry(QtCore.QRect(20, 269, 42, 51))
        self.play.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play.setIcon(icon4)
        self.play.setIconSize(QtCore.QSize(30, 30))
        self.play.setObjectName("play")
        self.right = QtWidgets.QPushButton(self.centralwidget)
        self.right.setGeometry(QtCore.QRect(163, 269, 42, 51))
        self.right.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("right-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.right.setIcon(icon5)
        self.right.setIconSize(QtCore.QSize(30, 30))
        self.right.setObjectName("right")
        self.left = QtWidgets.QPushButton(self.centralwidget)
        self.left.setGeometry(QtCore.QRect(68, 269, 41, 51))
        self.left.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("left-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.left.setIcon(icon6)
        self.left.setIconSize(QtCore.QSize(30, 30))
        self.left.setObjectName("left")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(72, 239, 411, 22))
        self.horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.horizontalSlider.setInputMethodHints(QtCore.Qt.ImhNone)
        self.horizontalSlider.setPageStep(10)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.sec = QtWidgets.QLabel(self.centralwidget)
        self.sec.setGeometry(QtCore.QRect(26, 239, 41, 20))
        self.sec.setObjectName("sec")
        self.equalizer = QtWidgets.QPushButton(self.centralwidget)
        self.equalizer.setGeometry(QtCore.QRect(353, 269, 42, 51))
        self.equalizer.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("equalizer-66.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.equalizer.setIcon(icon7)
        self.equalizer.setIconSize(QtCore.QSize(30, 30))
        self.equalizer.setCheckable(False)
        self.equalizer.setChecked(False)
        self.equalizer.setObjectName("equalizer")
 
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 570, 55, 16))
        self.label_2.setTabletTracking(False)
        self.label_2.setObjectName("label_2")
        self.veq1 = QtWidgets.QLabel(self.centralwidget)
        self.veq1.setGeometry(QtCore.QRect(90, 589, 55, 16))
        self.veq1.setTabletTracking(False)
        self.veq1.setObjectName("veq1")

        # self.eq1 = QtWidgets.QSlider(self.centralwidget)
        # self.eq1.setGeometry(QtCore.QRect(81, 340, 22, 221))
        # self.eq1.setTabletTracking(False)
        # self.eq1.setMaximum(5)
        # self.eq1.setTracking(True)
        # self.eq1.setOrientation(QtCore.Qt.Vertical)
        # self.eq1.setInvertedAppearance(False)
        # self.eq1.setInvertedControls(False)
        # self.eq1.setObjectName("eq1")

        # self.eq1.setValue(1)
        # self.eq1.setTickPosition(QSlider.TicksRight)
        # self.eq1.setTickInterval(6)

        # self.eq2 = QtWidgets.QSlider(self.centralwidget)
        # self.eq2.setGeometry(QtCore.QRect(170, 340, 22, 221))
        # self.eq2.setTabletTracking(False)
        # self.eq2.setMaximum(5)
        # self.eq2.setPageStep(10)
        # self.eq2.setOrientation(QtCore.Qt.Vertical)
        # self.eq2.setObjectName("eq2")

        # self.eq2.setValue(1)
        # self.eq2.setTickPosition(QSlider.TicksRight)
        # self.eq2.setTickInterval(6)

        # self.eq3 = QtWidgets.QSlider(self.centralwidget)
        # self.eq3.setGeometry(QtCore.QRect(259, 340, 22, 221))
        # self.eq3.setTabletTracking(False)
        # self.eq3.setMaximum(5)
        # self.eq3.setOrientation(QtCore.Qt.Vertical)
        # self.eq3.setObjectName("eq3")
        # self.eq3.setValue(1)
        # self.eq3.setTickPosition(QSlider.TicksRight)
        # self.eq3.setTickInterval(6)

        # self.eq4 = QtWidgets.QSlider(self.centralwidget)
        # self.eq4.setGeometry(QtCore.QRect(348, 340, 22, 221))
        # self.eq4.setTabletTracking(False)
        # self.eq4.setMaximum(5)
        # self.eq4.setOrientation(QtCore.Qt.Vertical)
        # self.eq4.setObjectName("eq4")

        # self.eq4.setValue(1)
        # self.eq4.setTickPosition(QSlider.TicksRight)
        # self.eq4.setTickInterval(6)


        # self.eq5 = QtWidgets.QSlider(self.centralwidget)
        # self.eq5.setGeometry(QtCore.QRect(437, 340, 22, 221))
        # self.eq5.setTabletTracking(False)
        # self.eq5.setMaximum(5)
        # self.eq5.setOrientation(QtCore.Qt.Vertical)
        # self.eq5.setObjectName("eq5")

        # self.eq5.setValue(1)
        # self.eq5.setTickPosition(QSlider.TicksRight)
        # self.eq5.setTickInterval(6)


        # self.eq6 = QtWidgets.QSlider(self.centralwidget)
        # self.eq6.setGeometry(QtCore.QRect(526, 340, 22, 221))
        # self.eq6.setTabletTracking(False)
        # self.eq6.setMaximum(30)
        # self.eq6.setOrientation(QtCore.Qt.Vertical)
        # self.eq6.setObjectName("eq6")

        # self.eq6.setValue(1)
        # self.eq6.setTickPosition(QSlider.TicksRight)
        # self.eq6.setTickInterval(6)

        # self.eq7 = QtWidgets.QSlider(self.centralwidget)
        # self.eq7.setGeometry(QtCore.QRect(615, 340, 22, 221))
        # self.eq7.setTabletTracking(False)
        # self.eq7.setMaximum(30)
        # self.eq7.setOrientation(QtCore.Qt.Vertical)
        # self.eq7.setObjectName("eq7")

        # self.eq7.setValue(1)
        # self.eq7.setTickPosition(QSlider.TicksRight)
        # self.eq7.setTickInterval(6)

        # self.eq8 = QtWidgets.QSlider(self.centralwidget)
        # self.eq8.setGeometry(QtCore.QRect(700, 339, 22, 221))
        # self.eq8.setTabletTracking(False)
        # self.eq8.setMaximum(30)
        # self.eq8.setOrientation(QtCore.Qt.Vertical)
        # self.eq8.setObjectName("eq8")

        # self.eq8.setValue(1)
        # self.eq8.setTickPosition(QSlider.TicksRight)
        # self.eq8.setTickInterval(6)



        # self.eq9 = QtWidgets.QSlider(self.centralwidget)
        # self.eq9.setGeometry(QtCore.QRect(793, 340, 22, 221))
        # self.eq9.setTabletTracking(False)
        # self.eq9.setMaximum(30)
        # self.eq9.setOrientation(QtCore.Qt.Vertical)
        # self.eq9.setObjectName("eq9")

        
        # self.eq9.setValue(1)
        # self.eq9.setTickPosition(QSlider.TicksRight)
        # self.eq9.setTickInterval(6)

        # self.eq10 = QtWidgets.QSlider(self.centralwidget)
        # self.eq10.setGeometry(QtCore.QRect(882, 340, 22, 221))
        # self.eq10.setTabletTracking(False)
        # self.eq10.setMaximum(30)
        # self.eq10.setOrientation(QtCore.Qt.Vertical)
        # self.eq10.setObjectName("eq10")
        
        # self.eq10.setValue(1)
        # self.eq10.setTickPosition(QSlider.TicksRight)
        # self.eq10.setTickInterval(6)        

        for i in range(0,10):
            self.equalizers.append(QtWidgets.QSlider(self.centralwidget))

            if i ==0:
                self.equalizers[i].setGeometry(QtCore.QRect(81, 340, 22, 221))
                self.equalizers[i].setObjectName("eq1")
            
            elif i ==1:
                self.equalizers[i].setGeometry(QtCore.QRect(170, 340, 22, 221))
                self.equalizers[i].setObjectName("eq2")
            
            elif i ==2:
                self.equalizers[i].setGeometry(QtCore.QRect(259, 340, 22, 221))
                self.equalizers[i].setObjectName("eq3")
            
            elif i ==3:
                self.equalizers[i].setGeometry(QtCore.QRect(348, 340, 22, 221))
                self.equalizers[i].setObjectName("eq4")
            
            elif i ==4:
                self.equalizers[i].setGeometry(QtCore.QRect(437, 340, 22, 221))
                self.equalizers[i].setObjectName("eq5")
            
            elif i ==5:
                self.equalizers[i].setGeometry(QtCore.QRect(526, 340, 22, 221))
                self.equalizers[i].setObjectName("eq6")
            
            elif i ==6:
                self.equalizers[i].setGeometry(QtCore.QRect(615, 340, 22, 221))
                self.equalizers[i].setObjectName("eq7")
            
            elif i ==7:
                self.equalizers[i].setGeometry(QtCore.QRect(700, 340, 22, 221))
                self.equalizers[i].setObjectName("eq8")
            
            elif i ==8:
                self.equalizers[i].setGeometry(QtCore.QRect(793, 340, 22, 221))
                self.equalizers[i].setObjectName("eq9")
            
            else :
                self.equalizers[i].setGeometry(QtCore.QRect(882, 340, 22, 221))
                self.equalizers[i].setObjectName("eq10")

            self.equalizers[i].setTabletTracking(False)
            self.equalizers[i].setMaximum(5)
            self.equalizers[i].setOrientation(QtCore.Qt.Vertical)
            self.equalizers[i].setValue(1)
            self.equalizers[i].setTickInterval(1)
            


        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 571, 55, 16))
        self.label_4.setTabletTracking(False)
        self.label_4.setObjectName("label_4")
        self.veq2 = QtWidgets.QLabel(self.centralwidget)
        self.veq2.setGeometry(QtCore.QRect(180, 590, 55, 16))
        self.veq2.setTabletTracking(False)
        self.veq2.setObjectName("veq2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(240, 571, 55, 16))
        self.label_6.setTabletTracking(False)
        self.label_6.setObjectName("label_6")
        self.veq3 = QtWidgets.QLabel(self.centralwidget)
        self.veq3.setGeometry(QtCore.QRect(270, 590, 55, 16))
        self.veq3.setTabletTracking(False)
        self.veq3.setObjectName("veq3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(330, 571, 55, 16))
        self.label_8.setTabletTracking(False)
        self.label_8.setObjectName("label_8")
        self.veq4 = QtWidgets.QLabel(self.centralwidget)
        self.veq4.setGeometry(QtCore.QRect(360, 590, 55, 16))
        self.veq4.setTabletTracking(False)
        self.veq4.setObjectName("veq4")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(420, 571, 55, 16))
        self.label_10.setTabletTracking(False)
        self.label_10.setObjectName("label_10")
        self.veq5 = QtWidgets.QLabel(self.centralwidget)
        self.veq5.setGeometry(QtCore.QRect(450, 590, 55, 16))
        self.veq5.setTabletTracking(False)
        self.veq5.setObjectName("veq5")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(510, 571, 55, 16))
        self.label_12.setTabletTracking(False)
        self.label_12.setObjectName("label_12")
        self.veq6 = QtWidgets.QLabel(self.centralwidget)
        self.veq6.setGeometry(QtCore.QRect(540, 590, 55, 16))
        self.veq6.setTabletTracking(False)
        self.veq6.setObjectName("veq6")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(600, 571, 55, 16))
        self.label_14.setTabletTracking(False)
        self.label_14.setObjectName("label_14")
        self.veq7 = QtWidgets.QLabel(self.centralwidget)
        self.veq7.setGeometry(QtCore.QRect(630, 590, 55, 16))
        self.veq7.setTabletTracking(False)
        self.veq7.setObjectName("veq7")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(680, 571, 55, 16))
        self.label_16.setTabletTracking(False)
        self.label_16.setObjectName("label_16")
        self.veq8 = QtWidgets.QLabel(self.centralwidget)
        self.veq8.setGeometry(QtCore.QRect(710, 590, 55, 16))
        self.veq8.setTabletTracking(False)
        self.veq8.setObjectName("veq8")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(770, 571, 55, 16))
        self.label_18.setTabletTracking(False)
        self.label_18.setObjectName("label_18")
        self.veq9 = QtWidgets.QLabel(self.centralwidget)
        self.veq9.setGeometry(QtCore.QRect(800, 590, 55, 16))
        self.veq9.setTabletTracking(False)
        self.veq9.setObjectName("veq9")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(860, 571, 55, 16))
        self.label_20.setTabletTracking(False)
        self.label_20.setObjectName("label_20")
        self.veq10 = QtWidgets.QLabel(self.centralwidget)
        self.veq10.setGeometry(QtCore.QRect(890, 590, 55, 16))
        self.veq10.setTabletTracking(False)
        self.veq10.setObjectName("veq10")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(420, 5, 131, 31))
        self.label_22.setObjectName("label_22")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 620, 121, 31))
        self.label.setObjectName("label")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(401, 269, 42, 51))
        self.save.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save.setIcon(icon8)
        self.save.setIconSize(QtCore.QSize(30, 30))
        self.save.setObjectName("save")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(812, 230, 151, 31))
        self.comboBox.setEditable(True)
        self.comboBox.setIconSize(QtCore.QSize(30, 30))
        self.comboBox.setObjectName("comboBox")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon9, "")
        self.comboBox.addItem(icon9, "")
        self.comboBox.addItem(icon9, "")
        self.comboBox.addItem(icon9, "")
        self.comboBox.addItem(icon9, "")
        self.spect = QtWidgets.QPushButton(self.centralwidget)
        self.spect.setGeometry(QtCore.QRect(449, 269, 41, 51))
        self.spect.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("spec3.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.spect.setIcon(icon10)
        self.spect.setIconSize(QtCore.QSize(30, 30))
        self.spect.setObjectName("spect")
        self.Zoom_in.raise_()
        self.signal_1.raise_()
        self.spectro_3.raise_()
        self.spectro_1.raise_()
        self.signal_3.raise_()
        self.zoom_out.raise_()
        self.clear.raise_()
        self.pause.raise_()
        self.play.raise_()
        self.right.raise_()
        self.left.raise_()
        self.horizontalSlider.raise_()
        self.sec.raise_()
        self.equalizer.raise_()
        # self.eq1.raise_()
        self.label_2.raise_()
        self.veq1.raise_()
        self.equalizers[0].raise_()
        self.equalizers[1].raise_()
        self.equalizers[2].raise_()
        self.equalizers[3].raise_()
        self.equalizers[4].raise_()
        self.equalizers[5].raise_()
        self.equalizers[6].raise_()
        self.equalizers[7].raise_()
        self.equalizers[8].raise_()
        self.equalizers[9].raise_()
        # self.eq2.raise_()
        # self.eq3.raise_()
        # self.eq4.raise_()
        # self.eq5.raise_()
        # self.eq6.raise_()
        # self.eq7.raise_()
        # self.eq8.raise_()
        # self.eq9.raise_()
        # self.eq10.raise_()
        self.label_4.raise_()
        self.veq2.raise_()
        self.label_6.raise_()
        self.veq3.raise_()
        self.label_8.raise_()
        self.veq4.raise_()
        self.label_10.raise_()
        self.veq5.raise_()
        self.label_12.raise_()
        self.veq6.raise_()
        self.label_14.raise_()
        self.veq7.raise_()
        self.label_16.raise_()
        self.veq8.raise_()
        self.label_18.raise_()
        self.veq9.raise_()
        self.label_20.raise_()
        self.veq10.raise_()
        self.label_22.raise_()
        self.label.raise_()
        self.save.raise_()
        self.spect.raise_()
        self.comboBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 984, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSignal_tools = QtWidgets.QMenu(self.menubar)
        self.menuSignal_tools.setObjectName("menuSignal_tools")
        self.menuSpectrogram = QtWidgets.QMenu(self.menuSignal_tools)
        self.menuSpectrogram.setObjectName("menuSpectrogram")
        self.menuPlayBack = QtWidgets.QMenu(self.menubar)
        self.menuPlayBack.setObjectName("menuPlayBack")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionsiganl_1 = QtWidgets.QAction(MainWindow)
        self.actionsiganl_1.setObjectName("actionsiganl_1")
        self.actionsignal_2 = QtWidgets.QAction(MainWindow)
        self.actionsignal_2.setObjectName("actionsignal_2")
        self.actionsignal_3 = QtWidgets.QAction(MainWindow)
        self.actionsignal_3.setObjectName("actionsignal_3")
        self.actionzoom_in = QtWidgets.QAction(MainWindow)
        self.actionzoom_in.setObjectName("actionzoom_in")
        self.actionzoom_out = QtWidgets.QAction(MainWindow)
        self.actionzoom_out.setObjectName("actionzoom_out")
        self.actionscroll_left = QtWidgets.QAction(MainWindow)
        self.actionscroll_left.setObjectName("actionscroll_left")
        self.actionscroll_right = QtWidgets.QAction(MainWindow)
        self.actionscroll_right.setObjectName("actionscroll_right")
        self.actionsavs_as_pdf = QtWidgets.QAction(MainWindow)
        self.actionsavs_as_pdf.setObjectName("actionsavs_as_pdf")
        self.actionEqualizer = QtWidgets.QAction(MainWindow)
        self.actionEqualizer.setObjectName("actionEqualizer")
        self.actionPlay = QtWidgets.QAction(MainWindow)
        self.actionPlay.setObjectName("actionPlay")
        self.actionStop = QtWidgets.QAction(MainWindow)
        self.actionStop.setObjectName("actionStop")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionColor_Pallette_2 = QtWidgets.QAction(MainWindow)
        self.actionColor_Pallette_2.setObjectName("actionColor_Pallette_2")
        self.actionColor_Pallette_3 = QtWidgets.QAction(MainWindow)
        self.actionColor_Pallette_3.setObjectName("actionColor_Pallette_3")
        self.actionColor_Pallette_4 = QtWidgets.QAction(MainWindow)
        self.actionColor_Pallette_4.setObjectName("actionColor_Pallette_4")
        self.actionColor_Palette_4 = QtWidgets.QAction(MainWindow)
        self.actionColor_Palette_4.setObjectName("actionColor_Palette_4")
        self.actionColor_Palette_5 = QtWidgets.QAction(MainWindow)
        self.actionColor_Palette_5.setObjectName("actionColor_Palette_5")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionsavs_as_pdf)
        self.menuEdit.addAction(self.actionzoom_in)
        self.menuEdit.addAction(self.actionzoom_out)
        self.menuSpectrogram.addSeparator()
        self.menuSpectrogram.addAction(self.actionColor_Pallette_2)
        self.menuSpectrogram.addAction(self.actionColor_Pallette_3)
        self.menuSpectrogram.addAction(self.actionColor_Pallette_4)
        self.menuSpectrogram.addAction(self.actionColor_Palette_4)
        self.menuSpectrogram.addAction(self.actionColor_Palette_5)
        self.menuSignal_tools.addAction(self.menuSpectrogram.menuAction())
        self.menuSignal_tools.addAction(self.actionEqualizer)
        self.menuPlayBack.addAction(self.actionPlay)
        self.menuPlayBack.addAction(self.actionStop)
        self.menuPlayBack.addAction(self.actionscroll_left)
        self.menuPlayBack.addAction(self.actionscroll_right)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPlayBack.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSignal_tools.menuAction())

        self.retranslateUi(MainWindow)
        # self.eq10.valueChanged['int'].connect(self.veq10.setNum)
        # self.eq1.valueChanged['int'].connect(self.veq1.setNum)
        # self.eq6.valueChanged['int'].connect(self.veq6.setNum)
        self.horizontalSlider.valueChanged['int'].connect(self.sec.setNum)
        # self.eq2.valueChanged['int'].connect(self.veq2.setNum)
        # self.eq5.valueChanged['int'].connect(self.veq5.setNum)
        # self.eq9.valueChanged['int'].connect(self.veq9.setNum)
        # self.eq8.valueChanged['int'].connect(self.veq8.setNum)
        # self.eq7.valueChanged['int'].connect(self.veq7.setNum)
        # self.eq4.valueChanged['int'].connect(self.veq4.setNum)
        # self.eq3.valueChanged['int'].connect(self.veq3.setNum)
        self.comboBox.activated['QString'].connect(self.spectro_1.show)
        self.spect.clicked.connect(self.spectro_1.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.signal_1, self.horizontalSlider)
        MainWindow.setTabOrder(self.horizontalSlider, self.play)
        MainWindow.setTabOrder(self.play, self.left)
        MainWindow.setTabOrder(self.left, self.pause)
        MainWindow.setTabOrder(self.pause, self.right)
        MainWindow.setTabOrder(self.right, self.Zoom_in)
        MainWindow.setTabOrder(self.Zoom_in, self.zoom_out)
        MainWindow.setTabOrder(self.zoom_out, self.clear)
        MainWindow.setTabOrder(self.clear, self.equalizer)
        MainWindow.setTabOrder(self.equalizer, self.save)
        MainWindow.setTabOrder(self.save, self.spect)
        MainWindow.setTabOrder(self.spect, self.spectro_1)
        MainWindow.setTabOrder(self.spectro_1, self.comboBox)
        # MainWindow.setTabOrder(self.comboBox, self.eq1)
        # MainWindow.setTabOrder(self.eq1, self.eq2)
        # MainWindow.setTabOrder(self.eq2, self.eq3)
        # MainWindow.setTabOrder(self.eq3, self.eq4)
        # MainWindow.setTabOrder(self.eq4, self.eq5)
        # MainWindow.setTabOrder(self.eq5, self.eq6)
        # MainWindow.setTabOrder(self.eq6, self.eq7)
        # MainWindow.setTabOrder(self.eq7, self.eq8)
        # MainWindow.setTabOrder(self.eq8, self.eq9)
        # MainWindow.setTabOrder(self.eq9, self.eq10)
        # MainWindow.setTabOrder(self.eq10, self.signal_3)
        # MainWindow.setTabOrder(self.signal_3, self.spectro_3)
        MainWindow.setTabOrder(self.spectro_3, self.equalizer)
        MainWindow.setTabOrder(self.equalizer, self.clear)
        MainWindow.setTabOrder(self.clear, self.zoom_out)
        MainWindow.setTabOrder(self.zoom_out, self.left)
        MainWindow.setTabOrder(self.left, self.right)
        MainWindow.setTabOrder(self.right, self.Zoom_in)
        MainWindow.setTabOrder(self.Zoom_in, self.pause)
        MainWindow.setTabOrder(self.pause, self.play)
        self.Zoom_in.clicked.connect(lambda:self.opensignal())
        self.zoom_out.clicked.connect(lambda:self.band1())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Zoom_in.setShortcut(_translate("MainWindow", "+"))
        self.zoom_out.setShortcut(_translate("MainWindow", "-"))
        self.clear.setShortcut(_translate("MainWindow", "Esc"))
        self.pause.setShortcut(_translate("MainWindow", "Shift+Space"))
        self.play.setShortcut(_translate("MainWindow", "Space"))
        self.right.setShortcut(_translate("MainWindow", "Shift+Right"))
        self.left.setShortcut(_translate("MainWindow", "Shift+Left"))
        self.sec.setText(_translate("MainWindow", "<html><head/><body><p>0</p></body></html>"))
        self.equalizer.setShortcut(_translate("MainWindow", "E"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">60 Hz</p></body></html>"))
        self.veq1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">0</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">170 Hz</p></body></html>"))
        self.veq2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">0</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">310 Hz</p></body></html>"))
        self.veq3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">0</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">600 Hz</p></body></html>"))
        self.veq4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">0</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">1 KHz</p></body></html>"))
        self.veq5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">0</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">3 KHz</p></body></html>"))
        self.veq6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">0</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">6 kHz</p></body></html>"))
        self.veq7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">0</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">12 KHz</p></body></html>"))
        self.veq8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">0</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">14 KHz</p></body></html>"))
        self.veq9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">0</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">16 KHz</p></body></html>"))
        self.veq10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">0</span></p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; color:#aa0000;\">Audio Input</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; color:#00557f;\">Audio Output</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Palette 1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Palette 2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Palette 3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Palette 4"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Palette 5"))
        self.menuFile.setTitle(_translate("MainWindow", "Media"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuSignal_tools.setTitle(_translate("MainWindow", "Signal tools"))
        self.menuSpectrogram.setTitle(_translate("MainWindow", "Spectrogram"))
        self.menuPlayBack.setTitle(_translate("MainWindow", "PlayBack"))
        self.actionsiganl_1.setText(_translate("MainWindow", "siganl-1"))
        self.actionsiganl_1.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.actionsignal_2.setText(_translate("MainWindow", "signal-2"))
        self.actionsignal_2.setShortcut(_translate("MainWindow", "Ctrl+2"))
        self.actionsignal_3.setText(_translate("MainWindow", "signal-3"))
        self.actionsignal_3.setShortcut(_translate("MainWindow", "Ctrl+3"))
        self.actionzoom_in.setText(_translate("MainWindow", "zoom-in"))
        self.actionzoom_in.setShortcut(_translate("MainWindow", "+"))
        self.actionzoom_out.setText(_translate("MainWindow", "zoom-out"))
        self.actionzoom_out.setShortcut(_translate("MainWindow", "-"))
        self.actionscroll_left.setText(_translate("MainWindow", "scroll-left"))
        self.actionscroll_left.setShortcut(_translate("MainWindow", "Shift+Left"))
        self.actionscroll_right.setText(_translate("MainWindow", "scroll-right"))
        self.actionscroll_right.setShortcut(_translate("MainWindow", "Shift+Right"))
        self.actionsavs_as_pdf.setText(_translate("MainWindow", "savs as pdf"))
        self.actionsavs_as_pdf.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionEqualizer.setText(_translate("MainWindow", "Equalizer "))
        self.actionEqualizer.setShortcut(_translate("MainWindow", "E"))
        self.actionPlay.setText(_translate("MainWindow", "Play"))
        self.actionPlay.setShortcut(_translate("MainWindow", "Space"))
        self.actionStop.setText(_translate("MainWindow", "Stop"))
        self.actionStop.setShortcut(_translate("MainWindow", "Shift+Space"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setToolTip(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionColor_Pallette_2.setText(_translate("MainWindow", "Color Palette 1"))
        self.actionColor_Pallette_2.setShortcut(_translate("MainWindow", "S, 1"))
        self.actionColor_Pallette_3.setText(_translate("MainWindow", "Color Pallette 2"))
        self.actionColor_Pallette_3.setShortcut(_translate("MainWindow", "S, 2"))
        self.actionColor_Pallette_4.setText(_translate("MainWindow", "Color Palette 3"))
        self.actionColor_Pallette_4.setShortcut(_translate("MainWindow", "S, 3"))
        self.actionColor_Palette_4.setText(_translate("MainWindow", "Color Palette 4"))
        self.actionColor_Palette_4.setShortcut(_translate("MainWindow", "S, 4"))
        self.actionColor_Palette_5.setText(_translate("MainWindow", "Color Palette 5"))
        self.actionColor_Palette_5.setShortcut(_translate("MainWindow", "S, 5"))

        self.actionOpen.triggered.connect(lambda:self.opensignal())
        self.spect.clicked.connect(lambda:self.spectro())
        self.save.clicked.connect(lambda:self.band1())
        self.equalizers[0].valueChanged.connect(lambda:self.Fourier(0))
        self.equalizers[1].valueChanged.connect(lambda:self.Fourier(1))
        self.equalizers[2].valueChanged.connect(lambda:self.Fourier(2))
        self.equalizers[3].valueChanged.connect(lambda:self.Fourier(3))
          
    
    def readsignal(self):
        self.fname=QtGui.QFileDialog.getOpenFileName(self,' txt or CSV or xls',"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)")
        self.path=self.fname[0]
        self.data,self.fs = librosa.load(os.path.basename(self.path),sr = None, mono = True,offset = 0.0,duration = None)

    def opensignal(self):
        self.readsignal()
        self.dataline= self.signal_3.plot(self.data)
    

    def Fourier(self,index):
        
        self.gain.append(self.equalizers[index].value())
        self.ft = abs(scipy.fft.rfft(self.data)) #the y axis of fft plot (amplitudes)
        self.freqs = scipy.fft.rfftfreq(len(self.ft), (1.0/self.fs)) #the x axis of fft plot (frequencies)
        self.phase = np.angle(scipy.fft.rfft(self.data))
        self.comp = scipy.fft.rfft(self.data) 
        print(self.comp.shape)
        index1= list(self.freqs).index(0*max(self.freqs)/10)
        index2=list(self.freqs).index(1*max(self.freqs)/10)
        for i in range(index1+(index*5000),index2+(index*5000)):
            self.ft[i]*=self.gain[index%10]
            self.comp[i] = self.ft[i]*(math.cos(self.phase[i]))+self.ft[i]*(math.sin(self.phase[i]))*1j
        
        self.m =scipy.fft.irfft(self.comp)
        print(self.m.shape)
        self.signal_1.plot(self.m , name="mode2")
        
      

    # def spectro(self):

    #     plt.specgram(self.data, Fs= 250 )
    #     plt.savefig('spectro.png', dpi=300, bbox_inches='tight')
    #     self.spectro_1.setPixmap(QtGui.QPixmap('spectro.png'))

    # def Fourier(self):
    #     before=[]
    #     gain= self.eq1.value()
    #     self.ft = abs(scipy.fft.rfft(self.data)) #the y axis of fft plot (amplitudes)
    #     self.freqs = scipy.fft.rfftfreq(len(self.ft), (1.0/self.fs)) #the x axis of fft plot (frequencies)
    #     self.phase = np.angle(scipy.fft.rfft(self.data))
    #     self.comp = scipy.fft.rfft(self.data) 
        
    #     index1= list(self.freqs).index(0*max(self.freqs)/10)
    #     index2=list(self.freqs).index(2*max(self.freqs)/10)
    #     for i in range(index1,index2):
    #         self.ft[i]*=gain
    #         self.comp[i] = self.ft[i]*(math.cos(self.phase[i]))+self.ft[i]*(math.sin(self.phase[i]))*1j
        
    #     self.m =scipy.fft.irfft(self.comp)
    #     print(self.m.shape)
    #     self.signal_1.plot(self.m)
    #     #wavfile.write('tes2.wav', self.fs, self.m)

    # def Fourier2(self):
    #     # self.Fourier()
    #     gain2= self.eq2.value()
    #     self.ft = abs(scipy.fft.rfft(self.data)) #the y axis of fft plot (amplitudes)
    #     self.freqs = scipy.fft.rfftfreq(len(self.ft), (1.0/self.fs)) #the x axis of fft plot (frequencies)
    #     self.phase = np.angle(scipy.fft.rfft(self.data))
    #     self.comp = scipy.fft.rfft(self.data) 
    #     index2=int(list(self.freqs).index(2*max(self.freqs)/10))

    #     for i in range(index2,index2+(5000)):
    #         self.ft[i]*=gain2
    #         self.comp[i] = self.ft[i]*(math.cos(self.phase[i]))+self.ft[i]*(math.sin(self.phase[i]))*1j
        
    #     self.m =scipy.fft.irfft(self.comp)
    #     self.signal_1.plot(self.m)
    #     #wavfile.write('tes2.wav', self.fs, self.m)

    # def Fourier3(self):
    #     # self.Fourier2()
    #     gain3= self.eq3.value()
    #     self.ft = abs(scipy.fft.rfft(self.data)) #the y axis of fft plot (amplitudes)
    #     self.freqs = scipy.fft.rfftfreq(len(self.ft), (1.0/self.fs)) #the x axis of fft plot (frequencies)
    #     self.comp = scipy.fft.rfft(self.data) 
    #     index2=int(list(self.freqs).index(2*max(self.freqs)/10))

    #     for i in range(index2+(5000),index2+(10000)):
    #         self.ft[i]*=self.eq3.value()
    #         self.comp[i] = self.ft[i]*(math.cos(self.phase[i]))+self.ft[i]*(math.sin(self.phase[i]))*1j
        
    #     self.m =scipy.fft.irfft(self.comp)
    #     self.signal_1.plot(self.m)
    #     # wavfile.write('tes3.wav', self.fs, self.m)

    # def Fourier4(self):
    #     # self.Fourier3()
    #     gain4= self.eq4.value()
    #     self.ft = abs(scipy.fft.rfft(self.data)) #the y axis of fft plot (amplitudes)
    #     self.freqs = scipy.fft.rfftfreq(len(self.ft), (1.0/self.fs)) #the x axis of fft plot (frequencies)
    #     self.phase = np.angle(scipy.fft.rfft(self.data))
    #     self.comp = scipy.fft.rfft(self.data) 
    #     index2=int(list(self.freqs).index(2*max(self.freqs)/10))

    #     for i in range(index2+(10000),index2+(15000)):
    #         self.ft[i]*=gain4
    #         self.comp[i] = self.ft[i]*(math.cos(self.phase[i]))+self.ft[i]*(math.sin(self.phase[i]))*1j
        
    #     self.m =scipy.fft.irfft(self.comp)
    #     self.signal_1.plot(self.m)
    #     # wavfile.write('tes3.wav', self.fs, self.m)


    # def Fourier5(self):
    #     # self.Fourier4()
    #     gain5= self.eq5.value()
    #     self.ft = abs(scipy.fft.rfft(self.data)) #the y axis of fft plot (amplitudes)
    #     self.freqs = scipy.fft.rfftfreq(len(self.ft), (1.0/self.fs)) #the x axis of fft plot (frequencies)
    #     self.phase = np.angle(scipy.fft.rfft(self.data))
    #     self.comp = scipy.fft.rfft(self.data) 
    #     index2=int(list(self.freqs).index(2*max(self.freqs)/10))

    #     for i in range(index2+(15000),index2+(20000)):
    #         self.ft[i]*=self.eq5.value()
    #         self.comp[i] = self.ft[i]*(math.cos(self.phase[i]))+self.ft[i]*(math.sin(self.phase[i]))*1j
        
    #     self.m =scipy.fft.irfft(self.comp)
    #     self.signal_1.plot(self.m)
    #     print("5")
    #     # wavfile.write('tes3.wav', self.fs, self.m)

    # def Fourier6(self):
    #     # self.Fourier5()
    #     gain6= self.eq6.value()
    #     self.ft = abs(scipy.fft.rfft(self.data)) #the y axis of fft plot (amplitudes)
    #     self.freqs = scipy.fft.rfftfreq(len(self.ft), (1.0/self.fs)) #the x axis of fft plot (frequencies)
    #     self.phase = np.angle(scipy.fft.rfft(self.data))
    #     self.comp = scipy.fft.rfft(self.data) 
    #     index2=int(list(self.freqs).index(2*max(self.freqs)/10))

    #     for i in range(index2+(20000),index2+(25000)):
    #         self.ft[i]*=self.eq6.value()
    #         self.comp[i] = self.ft[i]*(math.cos(self.phase[i]))+self.ft[i]*(math.sin(self.phase[i]))*1j
        
    #     self.m =scipy.fft.irfft(self.comp)
    #     self.signal_1.plot(self.m)
    #     # wavfile.write('tes3.wav', self.fs, self.m)

    # def Fourier7(self):
    #     # self.Fourier6()
    #     gain7= self.eq7.value()
    #     self.ft = abs(scipy.fft.rfft(self.data)) #the y axis of fft plot (amplitudes)
    #     self.freqs = scipy.fft.rfftfreq(len(self.ft), (1.0/self.fs)) #the x axis of fft plot (frequencies)
    #     self.phase = np.angle(scipy.fft.rfft(self.data))
    #     self.comp = scipy.fft.rfft(self.data) 
    #     index2=int(list(self.freqs).index(2*max(self.freqs)/10))

    #     for i in range(index2+(25000),index2+(30000)):
    #         self.ft[i]*=self.eq7.value()
    #         self.comp[i] = self.ft[i]*(math.cos(self.phase[i]))+self.ft[i]*(math.sin(self.phase[i]))*1j
        
    #     self.m =scipy.fft.irfft(self.comp)
    #     self.signal_1.plot(self.m)
    #     # wavfile.write('tes3.wav', self.fs, self.m)

    # def Fourier8(self):
    #     # self.Fourier7()
    #     gain8= self.eq8.value()
    #     self.ft = abs(scipy.fft.rfft(self.data)) #the y axis of fft plot (amplitudes)
    #     self.freqs = scipy.fft.rfftfreq(len(self.ft), (1.0/self.fs)) #the x axis of fft plot (frequencies)
    #     self.phase = np.angle(scipy.fft.rfft(self.data))
    #     self.comp = scipy.fft.rfft(self.data) 
    #     index2=int(list(self.freqs).index(2*max(self.freqs)/10))

    #     for i in range(index2+(30000),index2+(35000)):
    #         self.ft[i]*=self.eq8.value()
    #         self.comp[i] = self.ft[i]*(math.cos(self.phase[i]))+self.ft[i]*(math.sin(self.phase[i]))*1j
        
    #     self.m =scipy.fft.irfft(self.comp)
    #     self.signal_1.plot(self.m)

    #     # wavfile.write('tes3.wav', self.fs, self.m)


    # def Fourier9(self):
    #     # self.Fourier8()
    #     gain9= self.eq9.value()
    #     self.ft = abs(scipy.fft.rfft(self.data)) #the y axis of fft plot (amplitudes)
    #     self.freqs = scipy.fft.rfftfreq(len(self.ft), (1.0/self.fs)) #the x axis of fft plot (frequencies)
    #     self.phase = np.angle(scipy.fft.rfft(self.data))
    #     self.comp = scipy.fft.rfft(self.data) 
    #     index2=int(list(self.freqs).index(2*max(self.freqs)/10))

    #     for i in range(index2+(35000),index2+(40000)):
    #         self.ft[i]*=self.eq9.value()
    #         self.comp[i] = self.ft[i]*(math.cos(self.phase[i]))+self.ft[i]*(math.sin(self.phase[i]))*1j
        
    #     self.m =scipy.fft.irfft(self.comp)
    #     self.signal_1.plot(self.m)
    #     # wavfile.write('tes3.wav', self.fs, self.m)


    # def Fourier10(self):
    #     # self.Fourier9()
    #     gain10= self.eq10.value()
    #     self.ft = abs(scipy.fft.rfft(self.data)) #the y axis of fft plot (amplitudes)
    #     self.freqs = scipy.fft.rfftfreq(len(self.ft), (1.0/self.fs)) #the x axis of fft plot (frequencies)
    #     self.phase = np.angle(scipy.fft.rfft(self.data))
    #     self.comp = scipy.fft.rfft(self.data) 
    #     index2=int(list(self.freqs).index(2*max(self.freqs)/10))

    #     for i in range(index2+(40000),index2+(45000)):
    #         self.ft[i]*=self.eq10.value()
    #         self.comp[i] = self.ft[i]*(math.cos(self.phase[i]))+self.ft[i]*(math.sin(self.phase[i]))*1j
        
    #     self.m =scipy.fft.irfft(self.comp)
    #     self.signal_1.plot(self.m)
    #     # wavfile.write('tes3.wav', self.fs, self.m)


    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
