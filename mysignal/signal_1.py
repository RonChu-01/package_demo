# -*- coding: utf-8 -*-
# Author:chuyong
# CreateTime:2019/5/6 10:11

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton


class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.btn = QPushButton('测试点击按钮', self)
        self.btn.clicked.connect(self.show_msg)

    def show_msg(self):
        QMessageBox.information(self, '信息提示框', 'Ok，弹出测试信息')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())





