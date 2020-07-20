# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import math

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.t1 = QtWidgets.QLineEdit(self.centralwidget)
        self.t1.setObjectName("t1")
        self.gridLayout.addWidget(self.t1, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.t2 = QtWidgets.QLineEdit(self.centralwidget)
        self.t2.setObjectName("t2")
        self.gridLayout.addWidget(self.t2, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSquare = QtWidgets.QAction(MainWindow)
        self.actionSquare.setObjectName("actionSquare")
        self.actionCube = QtWidgets.QAction(MainWindow)
        self.actionCube.setObjectName("actionCube")
        self.actionSqrRoot = QtWidgets.QAction(MainWindow)
        self.actionSqrRoot.setObjectName("actionSqrRoot")
        self.actionCube_Roor = QtWidgets.QAction(MainWindow)
        self.actionCube_Roor.setObjectName("actionCube_Roor")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionSquare)
        self.menuFile.addAction(self.actionCube)
        self.menuFile.addAction(self.actionSqrRoot)
        self.menuFile.addAction(self.actionCube_Roor)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuFile.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.menuFile.triggered[QtWidgets.QAction].connect(self.menufunction)       #as a Event Handler triggred signal emitted by the file menu!!!

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Number"))
        self.label_2.setText(_translate("MainWindow", "Result"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSquare.setText(_translate("MainWindow", "Square"))
        self.actionSquare.setShortcut(_translate("MainWindow", "Alt+S"))
        self.actionCube.setText(_translate("MainWindow", "Cube"))
        self.actionSqrRoot.setText(_translate("MainWindow", "SqrRoot"))
        self.actionCube_Roor.setText(_translate("MainWindow", "Cube Roor"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        
    def menufunction(self, action):     #Added menu functionality method!!!
        txt=(action.text())
        no=int(self.t1.text())
        print(txt, no)
        if txt=='Square':
            self.t2.setText(str(no*no))
        if txt=='Cube':
            self.t2.setText(str(no*no*no))
        if txt=='SqrRoot':
            self.t2.setText(str(math.sqrt(no)))
        if txt=='Cube Roor':
            self.t2.setText(str(math.pow(no, 1/3)))
            
            
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

