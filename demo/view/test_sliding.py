import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QLabel
from ui.test_change_widget2 import Ui_Form

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


class Window(QWidget, Ui_Form):

    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.stackedWidget.slideInPrev)
        self.pushButton_2.clicked.connect(self.stackedWidget.slideInNext)

        v_box = QVBoxLayout()
        self.list_widget = QListWidget()

        self.list_widget.clicked.connect(self.switch_to_page)

        v_box.addWidget(self.list_widget)

        for i in range(len(data)):
            item = QListWidgetItem('name:{0}'.format(data[i]['name']), self.list_widget)
            self.list_widget.insertItem(i, item)

        self.lists.setLayout(v_box)

        # list_widget.currentRowChanged.connect(self.stackedWidget_2.setCurrentIndex)
        #
        # for i in range(len(data)):
        #     self.stackedWidget_2.addWidget(QLabel('{0}'.format(i)))

    def switch_to_page(self):
        item = self.list_widget.currentItem()
        row = self.list_widget.indexFromItem(item).row()
        # self.stackedWidget.slideInWgt(self.page_2, 4)
        self.stackedWidget.setCurrentWidget(self.page_2)
        self.label_20.setText(data[row]['name'])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())
