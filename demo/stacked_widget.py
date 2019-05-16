import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QListWidget, QStackedWidget, QListWidgetItem, QLabel

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


class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()

        h_box = QHBoxLayout()
        self.list_widget = QListWidget()
        self.stack_widget = QStackedWidget()

        h_box.addWidget(self.list_widget)
        h_box.addWidget(self.stack_widget)

        self.list_widget.currentRowChanged.connect(self.stack_widget.setCurrentIndex)

        for i in range(10):
            item = QListWidgetItem('hello: {}'.format(i), self.list_widget)
            self.list_widget.insertItem(i, item)

        for i in range(len(data)):
            name = QLabel('{0}'.format(data[i]['name']), self)
            self.stack_widget.addWidget(name)

        self.setLayout(h_box)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())
