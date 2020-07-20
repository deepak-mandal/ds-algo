# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'List.ui'
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
        self.list1 = QtWidgets.QListWidget(Form)
        self.list1.setObjectName("list1")
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list1.addItem(item)
        self.horizontalLayout.addWidget(self.list1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.list2 = QtWidgets.QListWidget(Form)
        self.list2.setObjectName("list2")
        self.horizontalLayout.addWidget(self.list2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.list1.itemDoubleClicked.connect(self.removelist1)      #used as a event handlers!!!
        self.list2.itemDoubleClicked.connect(self.removelist2)
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        __sortingEnabled = self.list1.isSortingEnabled()
        self.list1.setSortingEnabled(False)
        item = self.list1.item(0)
        item.setText(_translate("Form", "Kohli"))
        item = self.list1.item(1)
        item.setText(_translate("Form", "Dhoni"))
        item = self.list1.item(2)
        item.setText(_translate("Form", "Rohit"))
        item = self.list1.item(3)
        item.setText(_translate("Form", "Rahane"))
        item = self.list1.item(4)
        item.setText(_translate("Form", "Bhuvaneshwar"))
        item = self.list1.item(5)
        item.setText(_translate("Form", "Ashwin"))
        item = self.list1.item(6)
        item.setText(_translate("Form", "Jadaja"))
        self.list1.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("Form", "Available Player"))
        self.label.setText(_translate("Form", "Selected Player"))
        
    def removelist1(self, item):        #Event Handling!!!
        self.list1.takeItem(self.list1.row(item))
        self.list2.addItem(item.text())
        
    def removelist2(self, item):        #Event Handling!!!
        self.list2.takeItem(self.list2.row(item))
        self.list1.addItem(item.text())
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

