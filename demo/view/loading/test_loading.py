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
from PyQt5.QtGui import QColor, QPainter, QFont, QMovie
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QTextEdit, QGridLayout, QPushButton, QMainWindow, QLabel

__Author__ = """By: Irony
QQ: 892768447
Email: 892768447@qq.com"""
__Copyright__ = "Copyright (c) 2018 Irony"
__Version__ = "Version 1.0"


class CircleProgressBar(QWidget):

    Color = QColor(255, 185, 15)  # 圆圈颜色
    Clockwise = True  # 顺时针还是逆时针
    Delta = 36

    def __init__(self, *args, time, color=None, clockwise=True, **kwargs):
        super(CircleProgressBar, self).__init__(*args, **kwargs)
        self.angle = 0
        self.Clockwise = clockwise
        if color:
            self.Color = color
        self._timer = time
        self._timer.timeout.connect(self.update)

    def paintEvent(self, event):
        super(CircleProgressBar, self).paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)
        side = min(self.width(), self.height())
        painter.scale(side / 100.0, side / 100.0)
        painter.rotate(self.angle)
        painter.save()
        painter.setPen(Qt.NoPen)
        color = self.Color.toRgb()

        painter.setFont(QFont("Arial", 30))
        painter.drawText(event.rect(), Qt.AlignCenter, "loading")

        for i in range(11):
            color.setAlphaF(1.0 * i / 10)
            painter.setBrush(color)
            painter.drawEllipse(30, -10, 15, 15)
            painter.rotate(36)
        painter.restore()
        self.angle += self.Delta if self.Clockwise else -self.Delta
        self.angle %= 360

    @pyqtProperty(QColor)
    def color(self) -> QColor:
        return self.Color

    @color.setter
    def color(self, color: QColor):
        if self.Color != color:
            self.Color = color
            self.update()

    @pyqtProperty(bool)
    def clockwise(self) -> bool:
        return self.Clockwise

    @clockwise.setter
    def clockwise(self, clockwise: bool):
        if self.Clockwise != clockwise:
            self.Clockwise = clockwise
            self.update()

    @pyqtProperty(int)
    def delta(self) -> int:
        return self.Delta

    @delta.setter
    def delta(self, delta: int):
        if self.delta != delta:
            self.delta = delta
            self.update()

    def sizeHint(self) -> QSize:
        return QSize(100, 100)


class Loading(QWidget):

    def __init__(self, *args, **kwargs):
        super(Loading, self).__init__(*args, **kwargs)
        layout = QHBoxLayout(self)
        self.git = QMovie('loading.gif')
        self.label = QLabel()
        self.label.setMovie(self.git)
        self.git.start()
        layout.addWidget(self.label)

        self.setGeometry(0, 0, 300, 300)
        # self.label.setAlignment(Qt.AlignCenter)


class Window(QWidget):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        layout = QGridLayout()

        self.editor = QTextEdit()
        self.editor.setPlainText('0123456789'*100)
        self.setGeometry(0, 0, 600, 300)

        layout.addWidget(self.editor, 0, 0, 1, 3)
        self.btn = QPushButton('wait')
        layout.addWidget(self.btn, 1, 1, 1, 1)
        self.setLayout(layout)

        self.timer = QTimer(self)
        self.loading = CircleProgressBar(self, time=self.timer)
        self.loading.resize(100, 100)

        self.loading_text = QLabel(self)
        self.loading_text.setText("loading")
        self.loading_text.setAlignment(Qt.AlignCenter)
        self.loading_text.setStyleSheet("QLabel{color: #FFB90F}")
        self.loading_text.hide()
        self.loading_text.resize(100, 100)

        self.loading.hide()
        self.center_()
        self.btn.clicked.connect(self.do_loading)

    def do_loading(self):
        self.timer.start(100)
        self.loading.show()
        self.loading_text.show()

    # 进度条居中显示
    def center_(self):
        size = self.geometry()
        x = (size.width() - self.loading.width()) / 2
        y = (size.height() - self.loading.height()) / 2
        self.loading.move(x, y)
        self.loading_text.move(x, y)

        # self.loading2 = Loading(self)
        # self.loading2.hide()

    #     self.btn.clicked.connect(self.do_something)
    #
    # def do_something(self):
    #     self.editor.hide()
    #     self.btn.hide()
    #     self.loading2.show()

    # def resizeEvent(self, event):
    #     self.loading.resize(event.size())
    #     event.accept()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
