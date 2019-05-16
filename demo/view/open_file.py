import math
import sys
from time import sleep
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QFileDialog
from PyQt5.QtCore import QRectF, QLineF
from PyQt5.QtGui import QPainter, QImage, QPainterPath, QColor


class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()

    def paintEvent(self, event):

        # rect_angle = QRectF(10.0, 20.0, 80.0, 80.0)
        #
        # rect_angle2 = QRectF(100.0, 100.0, 80.0, 80.0)
        #
        # start_angle = 90 * 16
        # span_angle = -270 * 16

        painter = QPainter(self)

        # painter.drawArc(rect_angle, start_angle, span_angle)
        #
        # painter.drawEllipse(rect_angle2)
        #
        # line = QLineF(10, 80, 90, 10)
        # painter.drawLine(line)

        path = QPainterPath()
        path.moveTo(20, 80)
        path.lineTo(20, 30)
        path.cubicTo(80, 0, 50, 50, 80, 80)
        painter.drawPath(path)

        # self.draw_face(painter)

    def draw_face(self, p):
        path = QPainterPath()
        outdiameter = 376.0
        outre = QRectF(261.0, 30.0, outdiameter, outdiameter)
        outre_right_x = 261 + outdiameter / 2 + outdiameter / 2 / math.sqrt(2)
        outre_right_y = 30 + outdiameter / 2 + outdiameter / 2 / math.sqrt(2)
        path.moveTo(outre_right_x, outre_right_y)
        path.arcTo(outre, -45, 270)
        path.closeSubpath()
        p.setBrush(QColor(156, 214, 239))
        p.drawPath(path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())


