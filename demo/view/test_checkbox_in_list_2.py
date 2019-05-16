# -*- coding: utf-8 -*-
# Created by #chuyong, on 2019/5/13.
# Copyright (c) 2019 3KWan.
# Description :

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, \
    QListWidgetItem, QListWidget, QCheckBox, QHBoxLayout
from PyQt5.QtCore import Qt, QSize, QEvent


class Window(QWidget):
    """ 测试listitem添加自定义checkbox控件选中问题 """

    def __init__(self):
        super(Window, self).__init__()

        v_box = QVBoxLayout(self)
        # self.label = QLabel("hello")
        self.app_list = QListWidget()
        v_box.addWidget(self.app_list)

        # for i in range(5):
        #     item = QListWidgetItem(self.app_list)
        #     widget = QCheckBox("您选择了第{0}行".format(i))
        #     widget.stateChanged.connect(self.state_changed)
        #     self.app_list.setItemWidget(item, widget)

        for i in range(5):
            self.item = QListWidgetItem(self.app_list)
            self.item.setSizeHint(QSize(0, 50))
            # self.widget = QCheckBox("您选择了第{0}行".format(i))
            self.widget = ItemWidget("这是自定义checkbox{0}".format(i), self.item, self.app_list)
            self.app_list.setItemWidget(self.item, self.widget)

        # for i in range(self.app_list.count()):
        #     item = self.app_list.item(i)
        #     print(item)

        # self.app_list.itemClicked.connect(self.item_clicked)

    # def item_clicked(self, item):
    #     """
    #     listitem点击槽函数
    #     :param item:
    #     :return:
    #
    #     QListWidget.item()。使用它可以循环列表项并获得这样的检查状态
    #     for index in xrange(listWidget.count()):
    #         check_box = listWidget.itemWidget(listWidget.item(index))
    #         state = check_box.checkState()
    #     """
    #     # row = self.app_list.indexFromItem(item).row()
    #     # print("您选择了第{0}行".format(row))
    #
    #     # 获取当前选中的item包含的checkbox
    #     check_box = self.app_list.itemWidget(item)
    #     # 判断当前item的checkbox是否被选中
    #     state = check_box.checkState()
    #
    #     # 通过判断当前checkbox选中状态，设置当前选中的item包含的checkbox的状态
    #     if state == Qt.Checked:
    #         check_box.setChecked(Qt.Unchecked)
    #     elif state == Qt.Unchecked:
    #         check_box.setChecked(Qt.Checked)


class ItemWidget(QWidget):

    def __init__(self, text, item, *args, **kwargs):
        super(QWidget, self).__init__(*args, **kwargs)

        self.items = []
        data = {
            "row": 0,
            'item': None
        }

        self.item_ = item

        h_box = QHBoxLayout(self)
        self.check_box = QCheckBox(text)
        # self.check_box.setCheckable(False)
        h_box.addWidget(self.check_box)

        # 获取传入的QListWidget对象，app_list
        self.list_ = args[0]

        self.check_box.stateChanged.connect(self.state_changed)

        # 设置为checkbox设置objectname用于标识是哪一行的checkbox被点击
        self.check_box.setObjectName("{0}".format(self.list_.indexFromItem(self.item_).row()))

        data["row"] = self.list_.indexFromItem(self.item_).row()
        data["item"] = self.item_
        self.items.append(data)

        # print(self.list_.indexFromItem(self.item_).row())

    def state_changed(self, state):
        """
        checkbox选中/取消槽函数
        :param state:
        :return:
        self.app_list.setCurrentItem()
        self.app_list.setCurrentIndex()
        """
        # print(self.sender())

        checkbox_index = self.check_box.objectName()

        if state == Qt.Checked:
            row = int(checkbox_index)
            if row == self.items[0]["row"]:
                item = self.items[0]["item"]
                self.list_.setCurrentItem(item)

        elif state == Qt.Unchecked:
            row = self.list_.currentRow()
            print("您取消选择了第{0}行".format(row))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())
