# -*- coding: utf-8 -*-
# Author:chuyong
# CreateTime:2019/5/6 10:11

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton, QHBoxLayout
from PyQt5.QtCore import pyqtSignal


class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('内置信号和槽实例')
        self.resize(350, 50)

        h_box = QHBoxLayout()
        self.btn1 = QPushButton('Button 1')
        self.btn2 = QPushButton('Button 2')

        self.btn1.clicked.connect(lambda: self.on_btn_clicked(1))
        self.btn2.clicked.connect(lambda: self.on_btn_clicked(2))

        h_box.addWidget(self.btn1)
        h_box.addWidget(self.btn2)

        self.setLayout(h_box)

    def on_btn_clicked(self, n):
        print('Button {0} 被按下了'.format(n))
        QMessageBox.information(self, '信息提示框', 'Button {0} Clicked'.format(n))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())





