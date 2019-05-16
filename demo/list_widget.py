import os
import sys
import cgitb
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ItemWidget(QWidget):

    itemDelete = pyqtSignal(QListWidgetItem)

    def __init__(self, icon, text, item, *args, **kwargs):
        """

        :param icon:
        :param text:
        :param item:
        :param args:
        :param kwargs:
        """
        super(ItemWidget, self).__init__(*args, **kwargs)
        self.item_ = item
        self.item_.setIcon(QIcon(icon))

        h_box = QHBoxLayout(self)
        h_box.setContentsMargins(0, 0, 0, 0)
        h_box.addWidget(QLineEdit(text, self))
        h_box.addWidget(QPushButton('x', self, clicked=self.do_delete_item))

    def do_delete_item(self):
        self.itemDelete.emit(self.item_)


# 一个窗口类
class Window(QWidget):

    # 初始化窗口
    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        super(Window, self).__init__()

        # 创建一个布局容器
        layout = QVBoxLayout(self)

        # 创建一个QListWidget对象容器
        self.listWidget = QListWidget()

        # 将QListWidget对象容器添加进布局容器中
        layout.addWidget(self.listWidget)

        # 创建一个QListWidgetItem对象容器，分别添加icon、文字并添加进listWidget容器中
        # self.item = QListWidgetItem(QIcon('fly.png'), 'hello', self.listWidget)
        # self.listWidget.insertItem(1, self.item)

        # file_path = os.path.join(os.path.dirname(__file__))

        for i in range(5):

            self.item = QListWidgetItem(self.listWidget)

            self.widget = ItemWidget('../image/login/fly.png', 'item: {0}'.format(i), self.item, self.listWidget)

            self.widget.itemDelete.connect(self.do_delete_item)

            self.listWidget.setItemWidget(self.item, self.widget)

    def do_delete_item(self, item):
        """

        :param item:
        :return:
        """
        row = self.listWidget.indexFromItem(item).row()
        item_ = self.listWidget.takeItem(row)
        self.listWidget.removeItemWidget(item_)
        del item_


if __name__ == '__main__':
    sys.excepthook = cgitb.enable(1, None, 5, 'text')
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())



