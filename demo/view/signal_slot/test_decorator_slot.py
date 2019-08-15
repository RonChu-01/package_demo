# -*- coding: utf-8 -*-
# Created by #chuyong, on 2019/6/3.
# Copyright (c) 2019 3KWan.
# Description :

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
from PyQt5 import QtCore


class Window(QWidget):
    """  测试自定义修饰器信号/槽的用法 """

    def __init__(self):
        super(Window, self).__init__()

        h_box = QHBoxLayout(self)
        self.btn = QPushButton("Start", self)
        self.btn.setObjectName("start")
        h_box.addWidget(self.btn)
        QtCore.QMetaObject.connectSlotsByName(self)

    @QtCore.pyqtSlot()
    def on_start_clicked(self):
        print("Clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())
