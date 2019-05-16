import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QListWidgetItem, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit
from ui.test.test_add_widget2 import Ui_Form


class Window(QWidget, Ui_Form):

    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)

        v_box = QVBoxLayout()

        self.list_widget = QListWidget()
        v_box.addWidget(self.list_widget)

        for i in range(10):
            self.list_widget.insertItem(i, 'hello:{0}'.format(i))

        self.widget.setLayout(v_box)

        # h_box = QHBoxLayout()
        # self.name_ley = QLabel('product_id')
        # self.name_value = QLabel('123456')
        # h_box.addWidget(self.name_ley)
        # h_box.addWidget(self.name_value)

        grid_layout = QGridLayout()
        self.name_ley = QLabel('product_id')
        self.name_value = QLabel('123456')
        self.name_add = QLabel('ok')
        self.name_add2 = QLineEdit()
        self.name_add3 = QLabel('ok')
        grid_layout.addWidget(self.name_ley, 0, 0, 1, 1)
        # grid_layout.addWidget(self.name_value, 0, 1, 1, 1)
        # grid_layout.addWidget(self.name_add, 0, 2, 1, 1)
        grid_layout.addWidget(self.name_add2, 0, 1, 1, 2)
        # grid_layout.addWidget(self.name_add3, 0, 4, 1, 1)
        self.widget_2.setLayout(grid_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())
