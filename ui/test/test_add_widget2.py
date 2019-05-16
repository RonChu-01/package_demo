# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_add_widget2.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(711, 624)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(90, 80, 200, 400))
        self.widget.setMinimumSize(QtCore.QSize(200, 400))
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(310, 80, 300, 400))
        self.widget_2.setMinimumSize(QtCore.QSize(300, 400))
        self.widget_2.setObjectName("widget_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


