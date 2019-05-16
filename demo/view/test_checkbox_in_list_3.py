# -*- coding: utf-8 -*-
# Created by #chuyong, on 2019/5/13.
# Copyright (c) 2019 3KWan.
# Description :

import cgitb
from sys import argv
from PyQt5.Qt import *
from ctypes import *
cgitb.enable(format='text')  # 解决pyqt5异常只要进入事件循环,程序就崩溃,而没有任何提示

from PyQt5.QtCore import QItemSelectionModel, QModelIndex, QPoint, QEvent, Qt

"""
*VAR* 可以定义一个变量
*ARRAY* 可输入一个数组
*PARAM* 可变长度参数
*END* 光标结束符号
用的时候，把*号换成美元符号。
"""

class TestUi(QWidget):
    def __init__(self):
        super(TestUi, self).__init__()
        self.resize(300, 400)

        self.listWidget = QListWidget(self)

        self.widget = QWidget()
        self.hbox = QHBoxLayout()
        self.hbox.setContentsMargins(0, 0, 0, 0)
        self.b = QCheckBox('测试1')
        self.b1 = QCheckBox('测试2')
        self.hbox.addWidget(self.b)
        self.hbox.addWidget(self.b1)
        self.widget.setLayout(self.hbox)

        self.widget2 = QWidget()
        self.hbox2 = QHBoxLayout()
        self.hbox2.setContentsMargins(0, 0, 0, 0)
        self.b2 = QCheckBox('测试3')
        self.b3 = QCheckBox('测试4')
        self.hbox2.addWidget(self.b2)
        self.hbox2.addWidget(self.b3)
        self.widget2.setLayout(self.hbox2)

        self.item = QListWidgetItem(self.listWidget)
        self.item2 = QListWidgetItem(self.listWidget)
        self.listWidget.setItemWidget(self.item, self.widget)
        self.listWidget.setItemWidget(self.item2, self.widget2)

        self.b.toggled.connect(self.fn)
        self.b1.toggled.connect(self.fn)
        self.b2.toggled.connect(self.fn)
        self.b3.toggled.connect(self.fn)

    def fn(self, isChecked):
        mEvnPress = QMouseEvent(QEvent.MouseButtonPress, QPoint(0, 0), Qt.RightButton, Qt.RightButton, Qt.NoModifier)
        QApplication.sendEvent(self.sender(), mEvnPress)
        if isChecked:
            print(f"行号:{self.listWidget.currentIndex().row()}    【{self.listWidget.focusWidget().text()}】被选中")
        else:
            print(f"行号:{self.listWidget.currentIndex().row()}    【{self.listWidget.focusWidget().text()}】被取消选中")



        # a = self.sender().mapToParent(self.sender().pos())
        # QApplication.postEvent(self.sender().parent(), mEvnPress)

        # if self.sender() in [self.b, self.b1]:
        #     # self.a.setCurrentItem(self.item)
        #     # self.a.setCurrentIndex(self.a.currentIndex())
        # else:
        #     QApplication.sendEvent(self.sender(), mEvnPress)
        #     # self.a.setCurrentItem(self.item2)
        #     # self.a.setCurrentIndex(self.a.currentIndex())


class Input(QInputDialog):
    def __init__(self):
        super(Input, self).__init__()
        self.setOkButtonText('确定')

    def showEvent(self, *args, **kwargs):
        return


if __name__ == '__main__':
    app = QApplication(argv)
    window = TestUi()  # 实例化主窗口
    window.show()
    exit(app.exec_())


