# -*- coding: utf-8 -*-
# Created by #chuyong, on 2019/5/20.
# Copyright (c) 2019 3KWan.
# Description :

import sys
import time

from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QHBoxLayout, QPushButton, QVBoxLayout
from PyQt5.QtCore import QThread, pyqtSignal


class UploadData(object):

    def __init__(self):
        super().__init__()
        self._value = 0

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class UploadThread(QThread):

    upload_package = pyqtSignal(int)

    def __init__(self):
        super(UploadThread, self).__init__()
        self.upload_data = UploadData()
        # self.value = 0

    def run(self):
        while self.upload_data.value <= 100:
            time.sleep(1)
            self.upload_package.emit(self.value)
            self.upload_data.value = self.upload_data.value
            print(self.upload_data.value)


class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()

        self.resize(400, 300)

        self.upload_thread = UploadThread()
        self.upload_thread.upload_package.connect(self.start_upload)

        h_box = QHBoxLayout(self)

        self.progressbar = QProgressBar()
        self.progressbar.setMinimum(0)
        self.progressbar.setMaximum(100)
        self.progressbar.setFixedSize(300, 10)

        self.btn_start = QPushButton("Start")
        self.btn_start.clicked.connect(self.do_start_upload)

        h_box.addWidget(self.progressbar)
        h_box.addWidget(self.btn_start)

    def start_upload(self, value):
        self.progressbar.setValue(value)

    def do_start_upload(self):
        self.upload_thread.start(100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())




