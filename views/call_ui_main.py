import sys
import json
from PyQt5.QtWidgets import *
from ui.ui_main_window_v8 import Ui_Form
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSignal

data = [
    {'name': 'apple', 'icon': '../image/login/apple.png'},
    {'name': 'banana', 'icon': '../image/login/banana.png'},
    {'name': 'circle', 'icon': '../image/login/circle.png'},
    {'name': 'exit', 'icon': '../image/login/exit.png'},
    {'name': 'fly', 'icon': '../image/login/fly.png'},
    {'name': 'knife', 'icon': '../image/login/knife.png'},
    {'name': 'passwd', 'icon': '../image/login/passwd.png'},
    {'name': 'quit', 'icon': '../image/login/quit.png'},
    {'name': 'sword', 'icon': '../image/login/sword.png'},
    {'name': 'user', 'icon': '../image/login/user.png'},
]


class ItemWidget(QWidget):

    def __init__(self, item, text, icon, *args, **kwargs):
        super(ItemWidget, self).__init__(*args, **kwargs)
        self.item_ = item
        self.item_.setIcon(QIcon(icon))
        self.item_.setText(text)


class MainWindow(QMainWindow, Ui_Form):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.listWidget.clicked.connect(self.do_something)

        for i in range(len(data)):
            self.item_ = QListWidgetItem(self.listWidget)
            self.widget_ = ItemWidget(self.item_,
                                      'item: {0}'.format(data[i]['name']),
                                      '{0}'.format(data[i]['icon']),
                                      self.listWidget)

            self.listWidget.setItemWidget(self.item_, self.widget_)

    def do_something(self):
        item = self.listWidget.currentItem()
        row = self.listWidget.indexFromItem(item).row()
        name = data[row]['name']
        icon_path = data[row]['icon']


class ProjectInfo(QWidget):
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())


