# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first_plus.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class First_Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(339, 118)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 321, 101))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.project_idLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.project_idLabel.setObjectName("project_idLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.project_idLabel)
        self.project_idLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.project_idLineEdit.setObjectName("project_idLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.project_idLineEdit)
        self.game_idLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.game_idLabel.setObjectName("game_idLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.game_idLabel)
        self.game_idLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.game_idLineEdit.setObjectName("game_idLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.game_idLineEdit)
        self.nameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.valuesLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.valuesLabel.setObjectName("valuesLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.valuesLabel)
        self.valuesLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.valuesLineEdit.setObjectName("valuesLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.valuesLineEdit)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.project_idLabel.setText(_translate("Form", "project_id"))
        self.game_idLabel.setText(_translate("Form", "game_id"))
        self.nameLabel.setText(_translate("Form", "name"))
        self.valuesLabel.setText(_translate("Form", "values"))


