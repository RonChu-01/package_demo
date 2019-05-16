#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018年9月4日
@author: Irony
@site: https://pyqt5.com , https://github.com/892768447
@email: 892768447@qq.com
@file: 界面美化.圆形进度条.CircleProgressBar
@description:
"""
from PyQt5.QtCore import QSize, pyqtProperty, QTimer, Qt, QRect
from PyQt5.QtGui import QColor, QPainter, QFont, QPainterPath
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt5.QtGui import QMovie


class Window(QWidget):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        layout = QHBoxLayout(self)
        self.git = QMovie('loading.gif')
        self.label = QLabel()
        self.label.setMovie(self.git)
        self.git.start()
        layout.addWidget(self.label)
        self.setGeometry(300, 300, 300, 300)

        # self.label.hide()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
