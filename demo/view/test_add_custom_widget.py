import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from ui.base_window import Base_Ui_Form
from ui.first_plus import First_Ui_Form
from ui.second_plus import Sencond_Ui_Form


class Window(QWidget, Base_Ui_Form):

    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)

        first = First()
        second = Second()

        v_box = QVBoxLayout()
        v_box.addWidget(first)

        self.widget.setLayout(v_box)

        h_box = QHBoxLayout()
        h_box.addWidget(second)

        self.widget_2.setLayout(h_box)


class First(QWidget, First_Ui_Form):

    def __init__(self):
        super(First, self).__init__()
        self.setupUi(self)


class Second(QWidget, Sencond_Ui_Form):

    def __init__(self):
        super(Second, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())
