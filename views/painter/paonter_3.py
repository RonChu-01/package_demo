import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtGui import QPainter, QPen, QBrush, QPainterPath, QPalette, QFont, QColor
from PyQt5.QtCore import QRect, QPoint, Qt, QTimer, pyqtProperty, QSize


class CircleProgressBar(QWidget):

    def __init__(self, *args, **kwargs):
        super(CircleProgressBar, self).__init__(*args, **kwargs)
        self._timer = QTimer(self, timeout=self.update)
        self._timer.start(100)

    def paintEvent(self, event):

        rect = QRect(100, 100, 200, 200)

        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setPen(Qt.gray)
        painter.setFont(QFont("Arial", 30))
        painter.drawText(rect, Qt.AlignCenter, "loading")

        # color = QColor(Qt.gray)
        #
        # for i in range(11):
        #     color.setAlphaF(1.0 * i / 10)
        #     painter.setPen(color)
        #     painter.drawEllipse(rect)

        color = QColor(Qt.gray)

        path = QPainterPath()

        path.addEllipse(100, 100, 200, 200)
        path.addEllipse(105, 105, 190, 190)
        path.setFillRule(Qt.OddEvenFill)

        for i in range(11):

            color.setAlphaF(1.0 * i / 10)
            painter.setBrush(color)
            painter.drawPath(path)

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

    # def sizeHint(self) -> QSize:
    #     return QSize(200, 200)


class Window(QWidget):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        v_box = QVBoxLayout()
        v_box.addWidget(CircleProgressBar(self))
        self.setLayout(v_box)
        self.setGeometry(400, 400, 400, 400)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())
