# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'combo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.t1 = QtWidgets.QLineEdit(Form)
        self.t1.setObjectName("t1")
        self.horizontalLayout.addWidget(self.t1)
        self.b1 = QtWidgets.QPushButton(Form)
        self.b1.setObjectName("b1")
        self.horizontalLayout.addWidget(self.b1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.combo1 = QtWidgets.QComboBox(Form)
        self.combo1.setObjectName("combo1")
        self.combo1.addItem("")
        self.combo1.addItem("")
        self.combo1.addItem("")
        self.combo1.addItem("")
        self.combo1.addItem("")
        self.horizontalLayout_2.addWidget(self.combo1)
        self.b2 = QtWidgets.QPushButton(Form)
        self.b2.setObjectName("b2")
        self.horizontalLayout_2.addWidget(self.b2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.t2 = QtWidgets.QLineEdit(Form)
        self.t2.setObjectName("t2")
        self.verticalLayout.addWidget(self.t2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.b2.clicked.connect(self.rmitem)        #methods as Signals for clicked signal of b2&b1 btn 
        self.b1.clicked.connect(self.additem)
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.b1.setText(_translate("Form", "Add"))
        self.combo1.setItemText(0, _translate("Form", "C"))
        self.combo1.setItemText(1, _translate("Form", "C++"))
        self.combo1.setItemText(2, _translate("Form", "Java"))
        self.combo1.setItemText(3, _translate("Form", "Python"))
        self.combo1.setItemText(4, _translate("Form", "Fortran"))
        self.b2.setText(_translate("Form", "Remove"))
        
    def rmitem(self):       #Event Handling!!!
        indx=self.combo1.currentIndex()
        item=self.combo1.currentText()
        self.t2.setText(item+' is removed from combo box')
        self.combo1.removeItem(indx)
        
    def additem(self):          #Event Handling!!!
        self.combo1.addItem(self.t1.text())
        self.t2.setText(self.t1.text()+' is added to combo box')
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

