# -*- coding: utf-8 -*-
# Author:chuyong
# CreateTime:2019/5/6 10:11

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton


class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('内置信号和槽实例')
        self.resize(350, 50)
        btn = QPushButton('关闭', self)
        btn.clicked.connect(self.close)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())





