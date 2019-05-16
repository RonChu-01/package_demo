import sys
from time import sleep
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QProgressBar, QPushButton
from PyQt5.QtCore import QThread, pyqtSignal


class ProgressBar():
    pass


class Single(QThread):

    countChange = pyqtSignal(int)

    def run(self):
        count = 0
        while count < TIME_LIMIT:
            count += 1
            sleep(1)
            self.countChange.emit(count)


TIME_LIMIT = 100


class Action(QDialog):

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Progress Bar')
        self.progress = QProgressBar(self)
        self.progress.setGeometry(0, 0, 300, 25)
        self.progress.setMaximum(100)
        self.button = QPushButton('Start', self)
        self.button.move(0, 30)

        self.button.clicked.connect(self.do_something)

    def do_something(self):
        self.single = Single()
        self.single.countChange.connect(self.on_count_changed)
        self.single.start()

    def on_count_changed(self, value):
        self.progress.setValue(value)


class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # ui = Window()
    # ui.show()
    ui = Action()
    ui.show()
    sys.exit(app.exec_())
