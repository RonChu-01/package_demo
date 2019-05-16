# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_stack_page.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from SlidingStackedWidget import SlidingStackedWidget


class Stack_Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(873, 505)
        self.stackedWidget = SlidingStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 0, 860, 500))
        self.stackedWidget.setMinimumSize(QtCore.QSize(860, 500))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.layoutWidget = QtWidgets.QWidget(self.page)
        self.layoutWidget.setGeometry(QtCore.QRect(300, 60, 248, 14))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_point_1 = QtWidgets.QLabel(self.layoutWidget)
        self.label_point_1.setObjectName("label_point_1")
        self.horizontalLayout.addWidget(self.label_point_1)
        self.label_point_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_point_2.setObjectName("label_point_2")
        self.horizontalLayout.addWidget(self.label_point_2)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.page_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 110, 771, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(30)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_dl_pk = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_dl_pk.setObjectName("pushButton_dl_pk")
        self.gridLayout.addWidget(self.pushButton_dl_pk, 1, 4, 1, 1)
        self.label_game_status_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_game_status_2.setObjectName("label_game_status_2")
        self.gridLayout.addWidget(self.label_game_status_2, 0, 2, 1, 1)
        self.label_pk_addr_point = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_pk_addr_point.setText("")
        self.label_pk_addr_point.setPixmap(QtGui.QPixmap(":/img/star.png"))
        self.label_pk_addr_point.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pk_addr_point.setObjectName("label_pk_addr_point")
        self.gridLayout.addWidget(self.label_pk_addr_point, 1, 1, 1, 1)
        self.lineEdit_output_addr = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_output_addr.setObjectName("lineEdit_output_addr")
        self.gridLayout.addWidget(self.lineEdit_output_addr, 2, 2, 1, 1)
        self.label_output_name = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_output_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_output_name.setObjectName("label_output_name")
        self.gridLayout.addWidget(self.label_output_name, 4, 0, 1, 1)
        self.lineEdit_pk_addr = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_pk_addr.setObjectName("lineEdit_pk_addr")
        self.gridLayout.addWidget(self.lineEdit_pk_addr, 1, 2, 1, 1)
        self.label_pk_addr = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_pk_addr.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pk_addr.setObjectName("label_pk_addr")
        self.gridLayout.addWidget(self.label_pk_addr, 1, 0, 1, 1)
        self.pushButton_chose_pk = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_chose_pk.setObjectName("pushButton_chose_pk")
        self.gridLayout.addWidget(self.pushButton_chose_pk, 1, 3, 1, 1)
        self.label_game_status = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_game_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_game_status.setObjectName("label_game_status")
        self.gridLayout.addWidget(self.label_game_status, 0, 0, 1, 1)
        self.lineEdit_sign = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_sign.setObjectName("lineEdit_sign")
        self.gridLayout.addWidget(self.lineEdit_sign, 3, 2, 1, 1)
        self.pushButton_output_addr = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_output_addr.setObjectName("pushButton_output_addr")
        self.gridLayout.addWidget(self.pushButton_output_addr, 2, 3, 1, 1)
        self.label_sign = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_sign.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sign.setObjectName("label_sign")
        self.gridLayout.addWidget(self.label_sign, 3, 0, 1, 1)
        self.pushButton_sign = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_sign.setObjectName("pushButton_sign")
        self.gridLayout.addWidget(self.pushButton_sign, 3, 3, 1, 1)
        self.label_output_addr = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_output_addr.setAlignment(QtCore.Qt.AlignCenter)
        self.label_output_addr.setObjectName("label_output_addr")
        self.gridLayout.addWidget(self.label_output_addr, 2, 0, 1, 1)
        self.lineEdit_output_name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_output_name.setObjectName("lineEdit_output_name")
        self.gridLayout.addWidget(self.lineEdit_output_name, 4, 2, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.layoutWidget1 = QtWidgets.QWidget(self.page_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 20, 812, 468))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_channel_tab = QtWidgets.QWidget(self.layoutWidget1)
        self.widget_channel_tab.setMinimumSize(QtCore.QSize(800, 50))
        self.widget_channel_tab.setObjectName("widget_channel_tab")
        self.label_select_1 = QtWidgets.QLabel(self.widget_channel_tab)
        self.label_select_1.setGeometry(QtCore.QRect(307, 18, 16, 16))
        self.label_select_1.setText("")
        self.label_select_1.setPixmap(QtGui.QPixmap(":/img/yixuan.png"))
        self.label_select_1.setObjectName("label_select_1")
        self.label_select_2 = QtWidgets.QLabel(self.widget_channel_tab)
        self.label_select_2.setGeometry(QtCore.QRect(329, 18, 96, 16))
        self.label_select_2.setObjectName("label_select_2")
        self.label_select_3 = QtWidgets.QLabel(self.widget_channel_tab)
        self.label_select_3.setGeometry(QtCore.QRect(431, 18, 16, 16))
        self.label_select_3.setObjectName("label_select_3")
        self.label_not_available_1 = QtWidgets.QLabel(self.widget_channel_tab)
        self.label_not_available_1.setGeometry(QtCore.QRect(140, 20, 16, 16))
        self.label_not_available_1.setText("")
        self.label_not_available_1.setPixmap(QtGui.QPixmap(":/img/weipeizhi.png"))
        self.label_not_available_1.setObjectName("label_not_available_1")
        self.label_not_available_2 = QtWidgets.QLabel(self.widget_channel_tab)
        self.label_not_available_2.setGeometry(QtCore.QRect(162, 20, 72, 16))
        self.label_not_available_2.setObjectName("label_not_available_2")
        self.label_not_available_3 = QtWidgets.QLabel(self.widget_channel_tab)
        self.label_not_available_3.setGeometry(QtCore.QRect(240, 20, 18, 16))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_not_available_3.setFont(font)
        self.label_not_available_3.setObjectName("label_not_available_3")
        self.label_available_1 = QtWidgets.QLabel(self.widget_channel_tab)
        self.label_available_1.setGeometry(QtCore.QRect(23, 20, 16, 16))
        self.label_available_1.setText("")
        self.label_available_1.setPixmap(QtGui.QPixmap(":/img/kexuan.png"))
        self.label_available_1.setObjectName("label_available_1")
        self.label_available_2 = QtWidgets.QLabel(self.widget_channel_tab)
        self.label_available_2.setGeometry(QtCore.QRect(45, 20, 31, 16))
        self.label_available_2.setObjectName("label_available_2")
        self.label_available_3 = QtWidgets.QLabel(self.widget_channel_tab)
        self.label_available_3.setGeometry(QtCore.QRect(87, 20, 16, 16))
        self.label_available_3.setObjectName("label_available_3")
        self.verticalLayout_2.addWidget(self.widget_channel_tab)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_channel_list = QtWidgets.QWidget(self.layoutWidget1)
        self.widget_channel_list.setMinimumSize(QtCore.QSize(240, 360))
        self.widget_channel_list.setObjectName("widget_channel_list")
        self.verticalLayout.addWidget(self.widget_channel_list)
        self.widget_select_all = QtWidgets.QWidget(self.layoutWidget1)
        self.widget_select_all.setMinimumSize(QtCore.QSize(240, 40))
        self.widget_select_all.setObjectName("widget_select_all")
        self.checkBox = QtWidgets.QCheckBox(self.widget_select_all)
        self.checkBox.setGeometry(QtCore.QRect(20, 10, 71, 21))
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.widget_select_all)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.widget_select_channel_list = QtWidgets.QWidget(self.layoutWidget1)
        self.widget_select_channel_list.setMinimumSize(QtCore.QSize(560, 400))
        self.widget_select_channel_list.setObjectName("widget_select_channel_list")
        self.horizontalLayout_6.addWidget(self.widget_select_channel_list)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.widget = QtWidgets.QWidget(self.page_4)
        self.widget.setGeometry(QtCore.QRect(30, 30, 802, 438))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_unpack_tab = QtWidgets.QWidget(self.widget)
        self.widget_unpack_tab.setMinimumSize(QtCore.QSize(800, 40))
        self.widget_unpack_tab.setObjectName("widget_unpack_tab")
        self.pushButton_unpack = QtWidgets.QPushButton(self.widget_unpack_tab)
        self.pushButton_unpack.setGeometry(QtCore.QRect(10, 10, 90, 21))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/chubaozhong.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_unpack.setIcon(icon)
        self.pushButton_unpack.setObjectName("pushButton_unpack")
        self.pushButton_success = QtWidgets.QPushButton(self.widget_unpack_tab)
        self.pushButton_success.setGeometry(QtCore.QRect(120, 10, 90, 21))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/成功.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_success.setIcon(icon1)
        self.pushButton_success.setObjectName("pushButton_success")
        self.pushButton_test = QtWidgets.QPushButton(self.widget_unpack_tab)
        self.pushButton_test.setGeometry(QtCore.QRect(230, 10, 90, 21))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/07-大拇指.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_test.setIcon(icon2)
        self.pushButton_test.setObjectName("pushButton_test")
        self.pushButton_fail = QtWidgets.QPushButton(self.widget_unpack_tab)
        self.pushButton_fail.setGeometry(QtCore.QRect(340, 10, 90, 21))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/weipeizhi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_fail.setIcon(icon3)
        self.pushButton_fail.setObjectName("pushButton_fail")
        self.verticalLayout_3.addWidget(self.widget_unpack_tab)
        self.stackedWidget_2 = SlidingStackedWidget(self.widget)
        self.stackedWidget_2.setMinimumSize(QtCore.QSize(800, 390))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.stackedWidget_2.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.stackedWidget_2.addWidget(self.page_7)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.stackedWidget_2.addWidget(self.page_8)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.stackedWidget_2.addWidget(self.page_9)
        self.verticalLayout_3.addWidget(self.stackedWidget_2)
        self.stackedWidget.addWidget(self.page_4)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_point_1.setText(_translate("Form", "您当前没有可以打包的游戏点击"))
        self.label_point_2.setText(_translate("Form", "创建游戏"))
        self.pushButton_dl_pk.setText(_translate("Form", "下载母包"))
        self.label_game_status_2.setText(_translate("Form", "已上线"))
        self.label_output_name.setText(_translate("Form", "输出文件名"))
        self.label_pk_addr.setText(_translate("Form", "母包地址"))
        self.pushButton_chose_pk.setText(_translate("Form", "选择母包"))
        self.label_game_status.setText(_translate("Form", "游戏状态"))
        self.pushButton_output_addr.setText(_translate("Form", "存放路径"))
        self.label_sign.setText(_translate("Form", "签名证书"))
        self.pushButton_sign.setText(_translate("Form", "签名证书"))
        self.label_output_addr.setText(_translate("Form", "输出路径"))
        self.label_select_2.setText(_translate("Form", "已选择打包渠道："))
        self.label_select_3.setText(_translate("Form", "0"))
        self.label_not_available_2.setText(_translate("Form", "未配置渠道："))
        self.label_not_available_3.setText(_translate("Form", "926"))
        self.label_available_2.setText(_translate("Form", "可用："))
        self.label_available_3.setText(_translate("Form", "0"))
        self.checkBox.setText(_translate("Form", "全选"))
        self.pushButton_unpack.setText(_translate("Form", "出包中（0）"))
        self.pushButton_success.setText(_translate("Form", "成功（0）"))
        self.pushButton_test.setText(_translate("Form", "已测试（0）"))
        self.pushButton_fail.setText(_translate("Form", "失败（0）"))


import stack_page_rc