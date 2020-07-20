# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qlineedit.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.t2 = QtWidgets.QLineEdit(Form)
        self.t2.setObjectName("t2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.t2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.t3 = QtWidgets.QLineEdit(Form)
        self.t3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.t3.setObjectName("t3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.t3)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.t4 = QtWidgets.QLineEdit(Form)
        self.t4.setObjectName("t4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.t4)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.t1 = QtWidgets.QLineEdit(Form)
        self.t1.setObjectName("t1")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.t1)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.t1.setValidator(QtGui.QIntValidator())    #added for Integer validation!!!
        
        self.t4.textChanged.connect(self.textchange)    #textchange signal!!!
        
        self.b2.clicked.connect(lambda:self.chkbtn(self.b2))        #for identifying btn!!!
        self.b3.clicked.connect(lambda:self.chkbtn(self.b3))

        


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Input Mask"))
        self.t2.setInputMask(_translate("Form", "+99999999999"))
        self.label_3.setText(_translate("Form", "Password field"))
        self.label_4.setText(_translate("Form", "Text changer"))
        self.label.setText(_translate("Form", "Integer Validator"))
        
        
    def textchange(self, text):     #restrict to only alphabet!!!
        if text.isalpha()==False:
            print('non-alphabet character not allowed')
            self.t4.setText('')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

