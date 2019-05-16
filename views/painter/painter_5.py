from circularprogressbar import QRoundProgressBar
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5 import QtCore
from time import sleep
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout


class TstWidget(QWidget):
    def __init__(self):
        super(type(self), self).__init__()

        self.bar = QRoundProgressBar()
        self.bar.setFixedSize(300, 300)

        self.bar.setDataPenWidth(3)
        self.bar.setOutlinePenWidth(3)
        self.bar.setDecimals(1)
        self.bar.setFormat('%v | %p %')
        # self.bar.resetFormat()
        self.bar.setNullPosition(90)
        self.bar.setBarStyle(QRoundProgressBar.StyleDonut)
        self.bar.setDataColors([(0., QtGui.QColor.fromRgb(255,0,0)), (0.5, QtGui.QColor.fromRgb(255,255,0)), (1., QtGui.QColor.fromRgb(0,255,0))])
        self.bar.setMaximun(100)
        self.bar.setMinimun(0)
        self.bar.setRange(0, 100)
        self.bar.setValue(0)

        button = QPushButton("Start", self)

        button.clicked.connect(self.on_start)

        lay = QVBoxLayout()
        lay.addWidget(button)
        lay.addWidget(self.bar)
        self.setLayout(lay)

        self.myLongTask = TaskThread()
        self.myLongTask.notifyProgress.connect(self.on_progress)

    def on_start(self):
        self.myLongTask.start()

    def on_progress(self, i):
        self.bar.setValue(i)


class TaskThread(QtCore.QThread):
   notifyProgress = QtCore.pyqtSignal(int)

   def run(self):
       for i in range(101):
           self.notifyProgress.emit(i)
           sleep(0.1)


def main():

    app = QApplication(sys.argv)
    ex = TstWidget()
    ex.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
