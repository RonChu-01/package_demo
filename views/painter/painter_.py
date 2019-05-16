# -*- coding: utf-8 -*-

"""
    【简介】
    钟表
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

sed = [QPoint(0, -90), QPoint(2, 0), QPoint(0, 8), QPoint(-2, 0)]  # 四个坐标点均为逻辑坐标系中的点
minute = [QPoint(0, -70), QPoint(3, 0), QPoint(0, 8), QPoint(-3, 0)]  # 四个坐标点均为逻辑坐标系中的点
hour = [QPoint(0, -50), QPoint(3, 0), QPoint(0, 8), QPoint(-3, 0)]  # 四个坐标点均为逻辑坐标系中的点


class Clock(QWidget):
    def __init__(self, parent=None):
        super(Clock, self).__init__(parent)
        self.setWindowTitle("Clock")
        # self.resize(300, 300)
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.update)  # 计时每秒刷新一次，每次刷新触发一次paintEvent
        self.clockFont = QFont('宋体', 10)
        self.setFont(self.clockFont)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)  # 消除锯齿
        side = min(self.width(), self.height())
        # print(side)
        painter.setViewport((self.width() - side) / 2, (self.height() - side) / 2, side,
                            side)  # 设置视窗矩形区域device coordinate system
        painter.setWindow(0, 0, 200, 200)  # logical coordinate system.
        painter.begin(self)
        # 自定义的绘画方法
        self.draw(painter)
        painter.end()

    def draw(self, qp):
        thickPen = QPen(Qt.black, 1.5, Qt.SolidLine)
        thinPen = QPen(Qt.black, 0.5, Qt.SolidLine)

        time = QTime().currentTime()
        qp.translate(100, 100)  # 逻辑坐标系原点切换至新的坐标
        # 秒针设置
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setBrush(Qt.red)
        qp.setPen(Qt.red)
        qp.save()
        qp.rotate(6.0 * time.second())
        qp.drawConvexPolygon(QPolygon(sed))  # 画出秒针
        qp.restore()
        # 分针设置
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setBrush(Qt.blue)
        qp.setPen(Qt.blue)
        qp.save()
        qp.rotate(6.0 * (time.minute() + time.second() / 60.0))
        qp.drawConvexPolygon(QPolygon(minute))
        qp.restore()
        # 时针设置
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setBrush(Qt.black)
        qp.setPen(Qt.black)
        qp.save()
        qp.rotate(30.0 * (time.hour() + time.minute() / 60.0))
        qp.drawConvexPolygon(QPolygon(hour))
        qp.restore()
        # 刻度线及时间标注
        for i in range(1, 61):
            qp.save()
            qp.rotate(6 * i)
            if i % 5 == 0:
                qp.setPen(thickPen)
                qp.drawLine(0, -98, 0, -82)  # 逻辑坐标系中的坐标
                qp.drawText(-20, -82, 40, 40, Qt.AlignTop | Qt.AlignHCenter, str(int(i / 5)))
            else:
                qp.setPen(thinPen)
                qp.drawLine(0, -98, 0, -88)
            qp.restore()

        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Clock()
    demo.show()
    sys.exit(app.exec_())
