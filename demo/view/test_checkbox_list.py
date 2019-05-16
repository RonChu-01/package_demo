# -*- coding: utf-8 -*-
# Created by #chuyong, on 2019/5/10.
# Copyright (c) 2019 3KWan.
# Description :

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem, QCheckBox, QVBoxLayout, QLabel


class Window(QWidget):
    """ 测试listwidgetitem中添加CheckBox，选中问题 """

    def __int__(self):
        super(Window, self).__init__()

        v_box = QVBoxLayout(self)
        self.app_list = QListWidget()
        v_box.addWidget(self.app_list)
        v_box.addWidget(QLabel("hello"))

        # for i in range(5):
        #     item = QListWidgetItem(self.app_list)
        #     widget = QCheckBox("你选择了{0}".format(i), self.app_list)
        #     self.app_list.setItemWidget(item, widget)
        #
        # self.app_list.itemClicked.connect(self.item_clicked)

    def item_clicked(self, item):
        """
        listitem被点击槽函数
        :param item:
        :return:
        """
        row = self.app_list.indexFromItem(item)
        print(row)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())


