# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_first_item.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class First_Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(760, 60)
        self.cbx = QtWidgets.QCheckBox(Form)
        self.cbx.setGeometry(QtCore.QRect(20, 15, 60, 30))
        self.cbx.setObjectName("cbx")
        self.lb_no = QtWidgets.QLabel(Form)
        self.lb_no.setGeometry(QtCore.QRect(110, 10, 71, 41))
        self.lb_no.setObjectName("lb_no")
        self.lb_content = QtWidgets.QLabel(Form)
        self.lb_content.setGeometry(QtCore.QRect(220, 10, 151, 41))
        self.lb_content.setObjectName("lb_content")
        self.btn_del = QtWidgets.QPushButton(Form)
        self.btn_del.setGeometry(QtCore.QRect(660, 20, 75, 23))
        self.btn_del.setObjectName("btn_del")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.cbx.setText(_translate("Form", "选我"))
        self.lb_no.setText(_translate("Form", "咸鱼1号"))
        self.lb_content.setText(_translate("Form", "这是一条有梦想的咸鱼"))
        self.btn_del.setText(_translate("Form", "干掉"))


