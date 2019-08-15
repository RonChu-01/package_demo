# -*- coding: utf-8 -*-
# Created by #chuyong, on 2019/7/1.
# Copyright (c) 2019 3KWan.
# Description :
import cgitb
import sys

from PyQt5.QtCore import QSize, QEvent, QPoint, Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem, QCheckBox, QLabel

from application.view.main.ui_list_switch_demo import Ui_Form

cgitb.enable(format='text')  # 解决PyQt5异常只要进入事件循环,程序就崩溃,而没有任何提示


class ItemWidget(QWidget):

    def __init__(self, item, text, *args, **kwargs):
        super(ItemWidget, self).__init__(*args, **kwargs)
        self.item = item
        h_box = QHBoxLayout(self)
        self.check_box = QCheckBox(text)
        h_box.addWidget(self.check_box)

        # self.check_box.checkState()


class Window(QWidget, Ui_Form):

    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)

        self.params_ = []
        self.checked_params = []
        self.list_1_index = []

        v_box_1 = QVBoxLayout(self.widget)
        self.list_1 = QListWidget()
        v_box_1.addWidget(self.list_1)
        self.init_list_1()

        v_box_2 = QVBoxLayout(self.widget_2)
        self.list_2 = QListWidget()
        v_box_2.addWidget(self.list_2)

        # 通过测试
        self.pushButton_2.clicked.connect(self.do_pass)

    def init_list_1(self):
        for i in range(5):
            item = QListWidgetItem(self.list_1)
            item.setSizeHint(QSize(0, 40))
            param = "条目{0}".format(i)
            self.params_.append(param)
            widget = ItemWidget(item, param, self.list_1)
            widget.check_box.stateChanged.connect(self.do_state_change)
            self.list_1.setItemWidget(item, widget)

    def do_state_change(self, state):
        # 自定义鼠标点击事件----用于处理选中checkbox时同时选中checkbox所在list中的当前行
        event = QMouseEvent(QEvent.MouseButtonPress, QPoint(0, 0), Qt.RightButton, Qt.RightButton, Qt.NoModifier)
        # 发送事件
        QApplication.sendEvent(self.sender(), event)

        row = self.list_1.currentRow()
        param = self.params_[row]

        # 存储索引和参数的关系，用于删除的时候重新排序
        data = {
            "index": row,
        }

        if state == Qt.Checked:
            self.checked_params.append(param)
            self.list_1_index.append(data)
        elif state == Qt.Unchecked:
            self.checked_params.remove(param)
            self.list_1_index.remove(data)

    def do_pass(self):

        self.del_check(self.list_1.count())

    def del_check(self, count):
        if count < 1:
            return

        for index in range(count):
            check_box = self.list_1.itemWidget(self.list_1.item(index)).check_box
            state = check_box.checkState()
            if state == Qt.Checked:
                item = self.list_1.takeItem(index)
                self.list_1.removeItemWidget(item)
                del item
                return self.del_check(count - 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())
