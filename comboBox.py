# -*- coding: utf-8 -*-
# Created by #chuyong, on 2019/5/8.
# Copyright (c) 2019 3KWan.
# Description :


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.lb1 = QLabel('黑客帝国', self)

        combo = QComboBox(self)
        combo.addItem('黑客帝国')
        combo.addItem('指环王')
        combo.addItem('复仇车联盟')
        combo.addItem('阿凡达')
        combo.addItem('X战警')

        combo.move(50, 50)
        self.lb1.move(50, 150)

        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('组合框')
        self.show()

    def onActivated(self, text):
        self.lb1.setText(text)
        self.lb1.adjustSize()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())



