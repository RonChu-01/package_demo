# -*- coding: utf-8 -*-
# Author:chuyong
# CreateTime:2019/5/6 10:11

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton
from PyQt5.QtCore import pyqtSignal


class Window(QWidget):

    # 声明无参数的信号
    signal_1 = pyqtSignal()

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('内置信号和槽实例')
        self.resize(350, 50)

        self.signal_1.connect(self.signal_1_call)

        self.signal_1.emit()

    def signal_1_call(self):
        print('signal_1 emit')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())





