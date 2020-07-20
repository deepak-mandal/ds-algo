# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chkbox.ui'
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
        self.rb1 = QtWidgets.QCheckBox(Form)
        self.rb1.setObjectName("rb1")
        self.horizontalLayout.addWidget(self.rb1)
        self.rb2 = QtWidgets.QCheckBox(Form)
        self.rb2.setObjectName("rb2")
        self.horizontalLayout.addWidget(self.rb2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.rb1.stateChanged.connect(self.checkstate)      #Connecting state changed signal of both checkboxes to this* method
        self.rb2.stateChanged.connect(self.checkstate)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.rb1.setText(_translate("Form", "CB1"))
        self.rb2.setText(_translate("Form", "CB2"))
        
        
    def checkstate(self):       #Event Handling!!!
        state1='UnChecked'
        state2='UnChecked'
        if self.rb1.isChecked()==True:
            state1='Checked'
        else:
            state1='UnChecked'
        if self.rb2.isChecked()==True:
            state2='Checked'
        else:
            state2='Unchecked'
        self.t1.setText('cb1 is {} cb2 is {} '.format(state1, state2))
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

