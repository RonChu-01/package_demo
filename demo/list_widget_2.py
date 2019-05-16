import sys
import json
from PyQt5.QtWidgets import *
from ui.list_widget2 import Ui_Form
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSignal


class MainWindow(QMainWindow, Ui_Form):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())


