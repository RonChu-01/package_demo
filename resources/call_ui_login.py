# -*- coding: utf-8 -*-
# Author:chuyong
# CreateTime:2019/5/5 19:54

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog
from ui_login import Ui_Form
from PyQt5.QtCore import Qt


class Window(QDialog, Ui_Form):

    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint)

        self.widget_4.setStyleSheet('background-color: white;')
        self.widget_5.setStyleSheet('background-color: white;')

        self.lineEdit.setStyleSheet(
            'border-width:0;'
            'border-style:outset')

        self.lineEdit_2.setStyleSheet(
            'border-width:0;'
            'border-style:outset')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())




