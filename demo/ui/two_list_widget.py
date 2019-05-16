# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'two_list_widget.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(815, 474)
        self.left_widget = QtWidgets.QWidget(Form)
        self.left_widget.setGeometry(QtCore.QRect(30, 20, 211, 431))
        self.left_widget.setObjectName("left_widget")
        self.right_widget = QtWidgets.QWidget(Form)
        self.right_widget.setGeometry(QtCore.QRect(310, 20, 481, 431))
        self.right_widget.setObjectName("right_widget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


