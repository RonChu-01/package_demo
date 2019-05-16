import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from demo.ui.test_change_widget import Ui_Form
from demo.ui.first_page import First_Ui_Form
from demo.ui.second_page import Second_Ui_Form


class Window(QWidget, Ui_Form):

    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.stackedWidget.slideInPrev)
        self.pushButton_2.clicked.connect(self.stackedWidget.slideInNext)

        # for i in range(5):
        #     self.label = QLabel('hello:{0}'.format(i))
        #     self.stackedWidget.addWidget(self.label)


class FirstPage(QWidget, First_Ui_Form):

    def __init__(self):
        super(FirstPage, self).__init__()
        self.setupUi()


class SecondPage(QWidget, Second_Ui_Form):

    def __init__(self):
        super(SecondPage, self).__init__()
        self.setupUi()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())

