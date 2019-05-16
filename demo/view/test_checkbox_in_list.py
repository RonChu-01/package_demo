# -*- coding: utf-8 -*-
# Created by #chuyong, on 2019/5/13.
# Copyright (c) 2019 3KWan.
# Description :

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QListWidgetItem, QListWidget, QCheckBox
from PyQt5.QtCore import Qt


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
            self.widget = QCheckBox("您选择了第{0}行".format(i))
            self.widget.stateChanged.connect(self.state_changed)
            self.app_list.setItemWidget(self.item, self.widget)

        self.app_list.itemClicked.connect(self.item_clicked)

    def state_changed(self, state):
        """
        checkbox选中/取消槽函数
        :param state:
        :return:
        """
        if state == Qt.Checked:
            # item = self.app_list.currentItem()
            # row = self.app_list.indexFromItem(item).row()
            row = self.app_list.currentRow()
            print("您选择了第{0}行".format(row))
        elif state == Qt.Unchecked:
            row = self.app_list.currentRow()
            print("您取消选择了第{0}行".format(row))

    def item_clicked(self, item):
        """
        listitem点击槽函数
        :param item:
        :return:

        QListWidget.item()。使用它可以循环列表项并获得这样的检查状态
        for index in xrange(listWidget.count()):
            check_box = listWidget.itemWidget(listWidget.item(index))
            state = check_box.checkState()
        """
        # row = self.app_list.indexFromItem(item).row()
        # print("您选择了第{0}行".format(row))

        # 获取当前选中的item包含的checkbox
        check_box = self.app_list.itemWidget(item)
        # 判断当前item的checkbox是否被选中
        state = check_box.checkState()

        # 通过判断当前checkbox选中状态，设置当前选中的item包含的checkbox的状态
        if state == Qt.Checked:
            check_box.setChecked(Qt.Unchecked)
        elif state == Qt.Unchecked:
            check_box.setChecked(Qt.Checked)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())
