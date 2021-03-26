# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from pyqtgraph import PlotWidget ,PlotItem
import os
import pathlib
import pyqtgraph as pg 
import pandas as pd
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1108, 906)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.Signal1 = QtWidgets.QPushButton(self.centralwidget)
        self.Signal1.setGeometry(QtCore.QRect(30, 10, 171, 49))
        self.Signal1.setStyleSheet("background-color:rgb(255, 255, 255);\n" "font: 10pt \"Arial\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:/Course/python DSP/Biomedical-Signal_Viewer/looza/find.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Signal1.setIcon(icon)
        self.Signal1.setIconSize(QtCore.QSize(40, 40))
        self.Signal1.setObjectName("Signal1")

        self.Signal2 = QtWidgets.QPushButton(self.centralwidget)
        self.Signal2.setGeometry(QtCore.QRect(212, 10, 171, 49))
        self.Signal2.setStyleSheet("background-color:rgb(255, 255, 255);\n""font: 10pt \"Arial\";")
        self.Signal2.setIcon(icon)
        self.Signal2.setIconSize(QtCore.QSize(40, 40))
        self.Signal2.setObjectName("Signal2")

        self.Signal3 = QtWidgets.QPushButton(self.centralwidget)
        self.Signal3.setGeometry(QtCore.QRect(395, 10, 171, 49))
        self.Signal3.setStyleSheet("background-color:rgb(255, 255, 255);\n""font: 10pt \"Arial\";")
        self.Signal3.setIcon(icon)
        self.Signal3.setIconSize(QtCore.QSize(40, 40))
        self.Signal3.setObjectName("Signal3")

        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(580, 10, 53, 49))
        self.save.setStyleSheet("background-color:rgb(255, 255, 255);\n""font: 10pt \"Arial\";")
        self.save.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("F:/Course/python DSP/Biomedical-Signal_Viewer/looza/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save.setIcon(icon6)
        self.save.setIconSize(QtCore.QSize(40, 40))
        self.save.setObjectName("save")

        self.hide1 = QtWidgets.QCheckBox(self.centralwidget)
        self.hide1.setGeometry(QtCore.QRect(30, 80, 261, 25))
        self.hide1.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.hide1.setObjectName("hide1")
        self.play1 = QtWidgets.QPushButton(self.centralwidget)
        self.play1.setGeometry(QtCore.QRect(20, 120, 71, 33))
        self.play1.setStyleSheet("background-color:rgb(216, 216, 216)")
        self.play1.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("F:/Course/python DSP/Biomedical-Signal_Viewer/looza/play.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play1.setIcon(icon5)
        self.play1.setIconSize(QtCore.QSize(30, 30))
        self.play1.setShortcut("Toggle Media Play/Pause, Media Play")
        self.play1.setObjectName("play1")
        self.pause1 = QtWidgets.QPushButton(self.centralwidget)
        self.pause1.setGeometry(QtCore.QRect(20, 159, 71, 33))
        self.pause1.setStyleSheet("background-color:rgb(216, 216, 216)\n""")
        self.pause1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("F:/Course/python DSP/Biomedical-Signal_Viewer/looza/pause.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause1.setIcon(icon1)
        self.pause1.setIconSize(QtCore.QSize(30, 30))
        self.pause1.setObjectName("pause1")
        self.stop1 = QtWidgets.QPushButton(self.centralwidget)
        self.stop1.setGeometry(QtCore.QRect(20, 198, 71, 34))
        self.stop1.setStyleSheet("background-color:rgb(216, 216, 216)")
        self.stop1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("F:/Course/python DSP/Biomedical-Signal_Viewer/looza/stop.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop1.setIcon(icon2)
        self.stop1.setIconSize(QtCore.QSize(30, 30))
        self.stop1.setObjectName("stop1")
        self.zoomin1 = QtWidgets.QToolButton(self.centralwidget)
        self.zoomin1.setGeometry(QtCore.QRect(20, 238, 71, 34))
        self.zoomin1.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("F:/Course/python DSP/Biomedical-Signal_Viewer/looza/+.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomin1.setIcon(icon4)
        self.zoomin1.setIconSize(QtCore.QSize(30, 30))
        self.zoomin1.setShortcut("Ctrl+=")
        self.zoomin1.setObjectName("zoomin1")
        self.zoomout1 = QtWidgets.QToolButton(self.centralwidget)
        self.zoomout1.setGeometry(QtCore.QRect(20, 278, 71, 33))
        self.zoomout1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("F:/Course/python DSP/Biomedical-Signal_Viewer/looza/-.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomout1.setIcon(icon3)
        self.zoomout1.setIconSize(QtCore.QSize(30, 30))
        self.zoomout1.setShortcut("Ctrl+-")
        self.zoomout1.setObjectName("zoomout1")

        self.viewspect_1 = QtWidgets.QGraphicsView(self.centralwidget)
        self.viewspect_1.setGeometry(QtCore.QRect(570, 120, 471, 192))
        self.viewspect_1.setObjectName("viewspect_1")

        self.Viewsig_1 = PlotWidget(self.centralwidget)
        self.Viewsig_1.setGeometry(QtCore.QRect(100, 120, 461, 192))
        self.Viewsig_1.setStyleSheet("background-color:rgb(0, 0, 0);")
        self.Viewsig_1.setRubberBandSelectionMode(QtCore.Qt.IntersectsItemBoundingRect)
        self.Viewsig_1.setObjectName("Viewsig_1")
        self.Viewsig_1.plotItem.showGrid(x=True, y=True )
        self.Viewsig_1.plotItem.setMenuEnabled(False)



        self.hide2 = QtWidgets.QCheckBox(self.centralwidget)
        self.hide2.setGeometry(QtCore.QRect(30, 330, 261, 25))
        self.hide2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.hide2.setObjectName("hide2")
        self.play2 = QtWidgets.QPushButton(self.centralwidget)
        self.play2.setGeometry(QtCore.QRect(20, 370, 71, 33))
        self.play2.setStyleSheet("background-color:rgb(216, 216, 216)")
        self.play2.setText("")
        self.play2.setIcon(icon5)
        self.play2.setIconSize(QtCore.QSize(30, 30))
        self.play2.setShortcut("Toggle Media Play/Pause, Media Play")
        self.play2.setObjectName("play2")
        self.pause2 = QtWidgets.QPushButton(self.centralwidget)
        self.pause2.setGeometry(QtCore.QRect(20, 409, 71, 33))
        self.pause2.setStyleSheet("background-color:rgb(216, 216, 216)\n""")
        self.pause2.setText("")
        self.pause2.setIcon(icon1)
        self.pause2.setIconSize(QtCore.QSize(30, 30))
        self.pause2.setObjectName("pause2")
        self.stop2 = QtWidgets.QPushButton(self.centralwidget)
        self.stop2.setGeometry(QtCore.QRect(20, 448, 71, 34))
        self.stop2.setStyleSheet("background-color:rgb(216, 216, 216)")
        self.stop2.setText("")
        self.stop2.setIcon(icon2)
        self.stop2.setIconSize(QtCore.QSize(30, 30))
        self.stop2.setObjectName("stop2")
        self.zoomin2 = QtWidgets.QToolButton(self.centralwidget)
        self.zoomin2.setGeometry(QtCore.QRect(20, 488, 71, 34))
        self.zoomin2.setText("")
        self.zoomin2.setIcon(icon4)
        self.zoomin2.setIconSize(QtCore.QSize(30, 30))
        self.zoomin2.setShortcut("Ctrl+=")
        self.zoomin2.setObjectName("zoomin2")
        self.zoomout2 = QtWidgets.QToolButton(self.centralwidget)
        self.zoomout2.setGeometry(QtCore.QRect(20, 528, 71, 33))
        self.zoomout2.setText("")
        self.zoomout2.setIcon(icon3)
        self.zoomout2.setIconSize(QtCore.QSize(30, 30))
        self.zoomout2.setShortcut("Ctrl+-")
        self.zoomout2.setObjectName("zoomout2")
        
        self.viewspect_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.viewspect_2.setGeometry(QtCore.QRect(570, 370, 471, 192))
        self.viewspect_2.setObjectName("viewspect_2")
        
        self.Viewsig_2 = PlotWidget(self.centralwidget)
        self.Viewsig_2.setGeometry(QtCore.QRect(100, 370, 461, 192))
        self.Viewsig_2.setStyleSheet("background-color:rgb(0, 0, 0);")
        self.Viewsig_2.setRubberBandSelectionMode(QtCore.Qt.IntersectsItemBoundingRect)
        self.Viewsig_2.setObjectName("Viewsig_2")
        self.Viewsig_2.plotItem.showGrid(x=True, y=True )
        self.Viewsig_2.plotItem.setMenuEnabled(False)

        self.hide3 = QtWidgets.QCheckBox(self.centralwidget)
        self.hide3.setGeometry(QtCore.QRect(30, 590, 261, 25))
        self.hide3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.hide3.setObjectName("hide3")
        self.play3 = QtWidgets.QPushButton(self.centralwidget)
        self.play3.setGeometry(QtCore.QRect(20, 630, 71, 33))
        self.play3.setStyleSheet("background-color:rgb(216, 216, 216)")
        self.play3.setText("")
        self.play3.setIcon(icon5)
        self.play3.setIconSize(QtCore.QSize(30, 30))
        self.play3.setShortcut("Toggle Media Play/Pause, Media Play")
        self.play3.setObjectName("play3")
        self.pause3 = QtWidgets.QPushButton(self.centralwidget)
        self.pause3.setGeometry(QtCore.QRect(20, 669, 71, 33))
        self.pause3.setStyleSheet("background-color:rgb(216, 216, 216)\n""")
        self.pause3.setText("")
        self.pause3.setIcon(icon1)
        self.pause3.setIconSize(QtCore.QSize(30, 30))
        self.pause3.setObjectName("pause3")

        self.stop3 = QtWidgets.QPushButton(self.centralwidget)
        self.stop3.setGeometry(QtCore.QRect(20, 708, 71, 34))
        self.stop3.setStyleSheet("background-color:rgb(216, 216, 216)")
        self.stop3.setText("")
        self.stop3.setIcon(icon2)
        self.stop3.setIconSize(QtCore.QSize(30, 30))
        self.stop3.setObjectName("stop3")

        self.zoomin3 = QtWidgets.QToolButton(self.centralwidget)
        self.zoomin3.setGeometry(QtCore.QRect(20, 748, 71, 34))
        self.zoomin3.setText("")
        self.zoomin3.setIcon(icon4)
        self.zoomin3.setIconSize(QtCore.QSize(30, 30))
        self.zoomin3.setShortcut("Ctrl+=")
        self.zoomin3.setObjectName("zoomin3")
        self.zoomout3 = QtWidgets.QToolButton(self.centralwidget)
        self.zoomout3.setGeometry(QtCore.QRect(20, 788, 71, 33))
        self.zoomout3.setText("")
        self.zoomout3.setIcon(icon3)
        self.zoomout3.setIconSize(QtCore.QSize(30, 30))
        self.zoomout3.setShortcut("Ctrl+-")
        self.zoomout3.setObjectName("zoomout3")

        self.viewspect_3 = QtWidgets.QGraphicsView(self.centralwidget)
        self.viewspect_3.setGeometry(QtCore.QRect(570, 630, 471, 192))
        self.viewspect_3.setObjectName("viewspect_3")

        self.Viewsig_3 = PlotWidget(self.centralwidget)
        self.Viewsig_3.setGeometry(QtCore.QRect(100, 630, 461, 192))
        self.Viewsig_3.setStyleSheet("background-color:rgb(0, 0, 0);")
        self.Viewsig_3.setRubberBandSelectionMode(QtCore.Qt.IntersectsItemBoundingRect)
        self.Viewsig_3.setObjectName("Viewsig_3")
        self.Viewsig_3.plotItem.showGrid(x=True, y=True )
        self.Viewsig_3.plotItem.setMenuEnabled(False)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ######----- Buttons actions -----######
        # self.buttonname.clicked.connect(lambda:self.functionname())
        self.Signal1.clicked.connect(lambda:self.opensignal1())

        #######----reading function ---#######
    def readsignal1(self):
        self.fname1=QtGui.QFileDialog.getOpenFileName(self,'open only txt file',os.getenv('home'),"text(*.txt")
        path=self.fname1[0]
        self.data1=np.genfromtxt(path,delimiter=',')
        self.x1= self.data1[: , 0]
        self.y1 =self.data1[: , 1] 
        self.x1= list(self.x1[:])
        self.y1= list(self.y1[:])


    #######----Buttons functions -----############
    def opensignal1(self):
        self.readsignal1()
        self.pen = pg.mkPen(color=(255, 0, 0))
        self.data_line1 =  self.Viewsig_1.plot( self.x1,self.y1, pen=self.pen)
        self.Viewsig_1.plotItem.setLimits(xMin =0, xMax=12 , yMin =-0.6, yMax=0.6)
        



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Signal1.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.Signal1.setText(_translate("MainWindow", "Signal 1"))
        self.Signal1.setShortcut(_translate("MainWindow", "Toggle Media Play/Pause, Media Play"))
        self.Signal2.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.Signal2.setText(_translate("MainWindow", "Signal 2"))
        self.Signal2.setShortcut(_translate("MainWindow", "Space"))
        self.Signal3.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.Signal3.setText(_translate("MainWindow", "Signal 3"))
        self.Signal3.setShortcut(_translate("MainWindow", "Esc"))
        self.pause1.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.stop1.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.play1.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.hide2.setText(_translate("MainWindow", "Hide signal_2"))
        self.hide3.setText(_translate("MainWindow", "Hide signal_3"))
        self.save.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.save.setShortcut(_translate("MainWindow", "Esc"))
        self.hide1.setText(_translate("MainWindow", "Hide signal_1 "))
        self.stop2.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.play2.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.pause2.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.stop3.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.play3.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.pause3.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
