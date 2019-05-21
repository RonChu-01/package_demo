# -*- coding: utf-8 -*-
# Created by #chuyong, on 2019/5/20.
# Copyright (c) 2019 3KWan.
# Description :

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QProgressBar, QProgressDialog, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        h_box = QHBoxLayout(self)

        self.btn = QPushButton("上传")
        self.btn.clicked.connect(self.do_upload)

        h_box.addWidget(self.btn)

    def do_upload(self):
        progress = QProgressDialog(self)
        progress.setWindowTitle("请稍后")
        progress.setLabelText("正在上传")
        progress.setMinimumDuration(5)
        progress.setWindowModality(Qt.WindowModal)
        progress.setRange(0, 100)

        for i in range(101):
            progress.setValue(i)
        else:
            progress.setValue(100)

        progress.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())



