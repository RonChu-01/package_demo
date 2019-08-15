# -*- coding: utf-8 -*-
# Created by #chuyong, on 2019/5/30.
# Copyright (c) 2019 3KWan.
# Description :

import sys
import cgitb

from PyQt5.QtCore import QSize, QEvent, QObject
from PyQt5.QtGui import QWheelEvent, QCloseEvent
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem, QLabel, \
    QLineEdit, QListView, QAbstractItemView, QAbstractScrollArea
from PyQt5 import QtGui

cgitb.enable(format="text")


class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("测试滚动条事件")
        self.resize(300, 200)

        v_box = QVBoxLayout(self)
        self.list_ = QListWidget()
        v_box.addWidget(self.list_)

        # self.installEventFilter(self)
        # self.list_.installEventFilter(self)
        # 过滤掉滚动条的滚动事件
        self.list_.verticalScrollBar().installEventFilter(self)

        for i in range(20):
            item_ = QListWidgetItem(self.list_)
            item_.setSizeHint(QSize(0, 40))
            widget_ = QWidget(self.list_)

            list_item_h_box = QHBoxLayout()

            label = QLabel("hello：{0}".format(i))
            edit = QLineEdit()

            list_item_h_box.addWidget(label)
            list_item_h_box.addWidget(edit)
            widget_.setLayout(list_item_h_box)
            self.list_.setItemWidget(item_, widget_)

    # def event(self, event):
    #     """
    #
    #     :param event:
    #     :return:
    #     """
    #     if event.type() == QEvent.Wheel:
    #         print("1")
    #
    #     return QWidget.event(self, event)

    # def event(self, event: QEvent):
    #     """
    #     :param event:
    #     :return:
    #     """
    #     if event.type() == QEvent.Wheel:
    #         return False
    #     return super(Window, self).event(event)

    def closeEvent(self, event: QCloseEvent):
        """

        :param event:
        :return:
        """
        event.ignore()
    #
    # def wheelEvent(self, event):
    #     """
    #     重写滚动条事件
    #     :param event:
    #     :return:
    #     """
    #     # num_degrees = event.angleDelta() / 8
    #     # num_steps = num_degrees / 15
    #     #
    #     # angle_y = num_degrees.y()
    #     #
    #     # if angle_y > 0:
    #
    #     event.accept()

    def eventFilter(self, obj, event):
        """

        :param obj:
        :param event:
        :return:
        """
        if event.type() == QEvent.Wheel:
            return True
        elif event.type() == QtGui.QWheelEvent.Wheel:
            return True
        return super(Window, self).eventFilter(obj, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())


