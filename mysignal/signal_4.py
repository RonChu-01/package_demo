# -*- coding: utf-8 -*-
# Author:chuyong
# CreateTime:2019/5/6 10:11

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton
from PyQt5.QtCore import pyqtSignal


class Window(QWidget):

    # 自定义信号，不带参数
    btn_click_signal = pyqtSignal()

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('内置信号和槽实例')
        self.resize(350, 50)
        btn = QPushButton('关闭', self)

        # 连接信号与槽函数
        btn.clicked.connect(self.btn_clicked)

        # 接收信号，连接到槽函数
        self.btn_click_signal.connect(self.close)

    def btn_clicked(self):
        self.btn_click_signal.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())





