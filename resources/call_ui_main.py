# -*- coding: utf-8 -*-
# Created by #chuyong, on 2019/5/8.
# Copyright (c) 2019 3KWan.
# Description :

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import pyqtSignal
from ui_main import Main_Ui_Form
from ui_stack_page import Stack_Ui_Form


class Window(QWidget, Main_Ui_Form):

    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)

        stack = Stack()

        h_box = QHBoxLayout()
        h_box.addWidget(stack)
        self.widget_7.setLayout(h_box)

        # 下一页按钮绑定点击事件
        self.pushButton.clicked.connect(stack.stackedWidget.slideInNext)
        # 上一页按钮绑定点击事件
        self.pushButton_2.clicked.connect(stack.stackedWidget.slideInPrev)


class Stack(QWidget, Stack_Ui_Form):

    # 切换页面信号
    # switch_page_signal = pyqtSignal(object)

    def __init__(self):
        super(Stack, self).__init__()
        self.setupUi(self)

        v_box = QVBoxLayout()
        v_box.addWidget(QPushButton('6'))
        self.page_6.setLayout(v_box)

        v_box2 = QVBoxLayout()
        v_box2.addWidget(QPushButton('7'))
        self.page_7.setLayout(v_box2)

        v_box3 = QVBoxLayout()
        v_box3.addWidget(QPushButton('8'))
        self.page_8.setLayout(v_box3)

        v_box4 = QVBoxLayout()
        v_box4.addWidget(QPushButton('9'))
        self.page_9.setLayout(v_box4)

        self.pushButton_unpack.clicked.connect(lambda: self.switch_page(self.page_6))
        self.pushButton_success.clicked.connect(lambda: self.switch_page(self.page_7))
        self.pushButton_test.clicked.connect(lambda: self.switch_page(self.page_8))
        self.pushButton_fail.clicked.connect(lambda: self.switch_page(self.page_9))

    def switch_page(self, value):
        self.stackedWidget_2.setCurrentWidget(value)

    #     self.switch_page_signal.connect(self.switch_page_signal_call)
    #
    #     self.pushButton_unpack.clicked.connect(self.switch)
    #
    #     self.pushButton_success.clicked.connect(self.switch_to_page)
    #
    # def switch_to_page(self):
    #     self.stackedWidget_2.setCurrentWidget(self.page_7)
    #
    # def switch_page_signal_call(self, value):
    #     self.stackedWidget_2.setCurrentWidget(value)
    #
    # def switch(self):
    #     self.switch_page_signal.emit(self.page_6)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())



