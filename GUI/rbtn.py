# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rbtn.ui'
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
        self.t1 = QtWidgets.QLineEdit(Form)
        self.t1.setObjectName("t1")
        self.verticalLayout.addWidget(self.t1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.rb1 = QtWidgets.QRadioButton(Form)
        self.rb1.setObjectName("rb1")
        self.horizontalLayout.addWidget(self.rb1)
        self.rb2 = QtWidgets.QRadioButton(Form)
        self.rb2.setObjectName("rb2")
        self.horizontalLayout.addWidget(self.rb2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.rb1.toggled.connect(self.checkstate)       #connection of checkstate method!!!
        self.rb2.toggled.connect(self.checkstate)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.rb1.setText(_translate("Form", "RB1"))
        self.rb2.setText(_translate("Form", "RB2"))
        
        
    def checkstate(self):       #Event handling!!!
        state1='OFF'
        state2='OFF'
        if self.rb1.isChecked()==True:
            state1='ON'
        else:
            state1='OFF'
        if self.rb2.isChecked()==True:
            state2='ON'
        else:
            state2='OFF'
        self.t1.setText('Button1 is {} Button2 is {}'.format(state1, state2))
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

