# -*- coding: utf-8 -*-
# Created by #chuyong, on 2019/5/20.
# Copyright (c) 2019 3KWan.
# Description : 测试View层与Model层交互，View层需要什么数据，就提供相应的接口

import sys
import time
import cgitb

from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QHBoxLayout, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import QThread, pyqtSignal

cgitb.enable(format='text')  # 解决PyQt5异常只要进入事件循环,程序就崩溃,而没有任何提示


class UploadThread(QThread):

    upload_package = pyqtSignal(int, str)

    def __init__(self):
        super(UploadThread, self).__init__()
        self.value_ = 0
        self.text_ = ""

    @property
    def value(self):
        return self.value_

    @value.setter
    def value(self, value):
        self.value_ = value

    @property
    def text(self):
        return self.text_

    @text.setter
    def text(self, value):
        self.text_ = value

    def run(self):
        while self.value <= 100:
            time.sleep(1)
            self.upload_package.emit(self.value, self.text)
            print(self.value)


class Window(QWidget):

    global upload_thread
    upload_thread = UploadThread()

    def __init__(self):
        super(Window, self).__init__()

        self.resize(400, 300)

        h_box = QHBoxLayout(self)

        self.progressbar = QProgressBar()
        self.progressbar.setMinimum(0)
        self.progressbar.setMaximum(100)
        self.progressbar.setFixedSize(300, 10)

        self.btn_start = QPushButton("Start")
        self.btn_start.clicked.connect(self.do_start_upload)
        self.label = QLabel("测试")

        h_box.addWidget(self.progressbar)
        h_box.addWidget(self.label)
        h_box.addWidget(self.btn_start)

        upload_thread.upload_package.connect(self.start_upload)

    @staticmethod
    def upload(value, text):
        upload_thread.value = value
        upload_thread.text = text

    def start_upload(self, value, text):
        self.progressbar.setValue(value)
        self.label.setText(text)

    @staticmethod
    def do_start_upload():
        upload_thread.start(100)


class CallUpload(QThread):

    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(101):
            time.sleep(1)
            Window.upload(i, "这是标签{0}".format(i))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    call = CallUpload()
    call.start()
    ui.show()
    sys.exit(app.exec_())




