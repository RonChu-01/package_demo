# -*- coding: utf-8 -*-
# Created by #chuyong, on 2019/5/30.
# Copyright (c) 2019 3KWan.
# Description :

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QDialog
from PyQt5.QtCore import pyqtSignal, Qt


class ChildWindow(QDialog):

    pass_params = pyqtSignal(str, str)

    def __init__(self):
        super(ChildWindow, self).__init__()
        self.setWindowTitle("QDialog类型子窗口")
        self.resize(200, 100)

        v_box = QVBoxLayout(self)
        self.widget_name = QWidget()
        self.widget_password = QWidget()
        v_box.addWidget(self.widget_name)
        v_box.addWidget(self.widget_password)

        name_h_box = QHBoxLayout()
        self.label_name = QLabel()
        self.label_name.setText("用户名：")
        self.line_edit_name = QLineEdit()
        name_h_box.addWidget(self.label_name)
        name_h_box.addWidget(self.line_edit_name)

        password_h_box = QHBoxLayout()
        self.label_password = QLabel()
        self.label_password.setText("密码：")
        self.line_edit_password = QLineEdit()
        password_h_box.addWidget(self.label_password)
        password_h_box.addWidget(self.line_edit_password)

        self.widget_name.setLayout(name_h_box)
        self.widget_password.setLayout(password_h_box)

    def closeEvent(self, event):
        name = self.line_edit_name.text()
        password = self.line_edit_password.text()
        self.pass_params.emit(name, password)
        event.accept()


class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("测试窗口传参")
        self.resize(300, 150)

        v_box = QVBoxLayout(self)
        self.widget_name = QWidget()
        self.widget_password = QWidget()
        v_box.addWidget(self.widget_name)
        v_box.addWidget(self.widget_password)

        name_h_box = QHBoxLayout()
        self.label_name = QLabel()
        self.label_name.setText("用户名：")
        self.line_edit_name = QLineEdit()
        name_h_box.addWidget(self.label_name)
        name_h_box.addWidget(self.line_edit_name)

        password_h_box = QHBoxLayout()
        self.label_password = QLabel()
        self.label_password.setText("密码：")
        self.line_edit_password = QLineEdit()
        password_h_box.addWidget(self.label_password)
        password_h_box.addWidget(self.line_edit_password)

        self.widget_name.setLayout(name_h_box)
        self.widget_password.setLayout(password_h_box)

        self.btn_test_1 = QPushButton("测试1")
        v_box.addWidget(self.btn_test_1)

        self.btn_test_1.clicked.connect(self.do_get_child_params)

    def do_get_child_params(self):
        """

        :return:
        """
        dialog = ChildWindow()
        dialog.pass_params.connect(self.show_child_window_params)
        dialog.exec_()
        dialog.show()

    def show_child_window_params(self, name, password):
        """
        :return:
        """
        self.line_edit_name.setText(name)
        self.line_edit_password.setText(password)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())

