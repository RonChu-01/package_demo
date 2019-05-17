# -*- coding: utf-8 -*-
# Created by #chuyong, on 2019/5/15.
# Copyright (c) 2019 3KWan.
# Description : 测试复选框全选

"""
1、测试复选框全选；
2、测试在list中复选框全选；
3、测试全选左边list选项，将左边全选的内容添加进右边的list中
4、测试左右列表关联（主要是删除）
"""

import sys
import cgitb

from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QListWidget, \
    QListWidgetItem, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import QSize, QEvent, QPoint, Qt
from PyQt5.QtGui import QMouseEvent

cgitb.enable(format="text")


class Window(QWidget):
    """  主窗口 """

    def __init__(self):
        super(Window, self).__init__()

        self.resize(1200, 800)

        # 整体水平布局
        h_box = QHBoxLayout(self)

        # 左侧列表布局
        left_v_box = QVBoxLayout()
        self.left_list = QListWidget()
        left_v_box.addWidget(self.left_list)
        # 全选按钮
        self.check_all = QCheckBox("全选", objectName="checked_all")
        left_v_box.addWidget(self.check_all)

        # 右侧列表布局
        right_v_box = QVBoxLayout()
        self.right_list = QListWidget()
        right_v_box.addWidget(self.right_list)

        # 将左右布局添加进主布局中
        h_box.addLayout(left_v_box)
        h_box.addLayout(right_v_box)

        # 左侧列表数据填充（自定义控件填充 ）
        for i in range(10):
            left_item = QListWidgetItem(self.left_list)
            left_item.setSizeHint(QSize(0, 50))
            # 注意，这里是通过循环动态生成自定义控件，这里传参相当于是存在多个实例属性
            left_widget = LeftItemWidget(left_item, self.check_all, self.left_list)
            print(left_widget.checkbox)
            self.left_list.setItemWidget(left_item, left_widget)


# 全局变量，由于自定义控件每次实例化会产生不同的实例属性，所以，目前是采用全局变量解决这个问题
checked_count = 0


class LeftItemWidget(QWidget):
    """  自定义列表item控件，用于插入自定义控件
         自定义控件时，注意区分实例属性和类属性
         相关内容需要对应各自的实例，否则无法进行操作
    """

    def __init__(self, item, check_all, *args, **kwargs):
        """
        自定义控件初始化
        :param item: 注意这里的item是实例属性，由上面初始化时传递，每个item对应不同实例
        :param check_all: 注意这里的check_all是实例属性，由上面初始化时传递，每个check_all对应不同实例，
        有多少个实例就有多少个实例属性
        :param args:
        :param kwargs:
        """
        super(LeftItemWidget, self).__init__(*args, **kwargs)
        self.item_ = item  # 实例属性，不同实例拥有不同的实例属性，虽然名字是相同的
        self.check_ = check_all  # 实例属性，不同实例拥有不同的实例属性，虽然名字是相同的
        self.list_ = args[0]
        # 每实例化一次，获取当前的item所在的行
        row = self.list_.indexFromItem(self.item_).row()

        h_box = QHBoxLayout(self)
        self.checkbox = QCheckBox("选项{0}".format(row))
        self.label = QLabel("这是第{0}标签".format(row))
        h_box.addWidget(self.checkbox)
        h_box.addWidget(self.label)

        self.checkbox.stateChanged.connect(self.state_changed)
        # 绑定clicked事件，防止当因为其它因素导致复选框状态发生改变时而进行相关操作
        self.check_.clicked.connect(self.all_state_changed)

    def state_changed(self, state):
        """
        复选框被选中信号响应槽函数
        :return:
        """
        # 声明当前checked_count变量为全局变量，用于在局部汇总引用
        global checked_count

        event = QMouseEvent(QEvent.MouseButtonPress, QPoint(0, 0), Qt.RightButton, Qt.RightButton, Qt.NoModifier)
        QApplication.sendEvent(self.sender(), event)

        if state == Qt.Checked:
            checked_count += 1

        elif state == Qt.Unchecked:
            checked_count -= 1

        # 上方的复选框与下方的全选按钮通过选中数量进行关联
        if checked_count == self.list_.count():
            self.check_.setChecked(True)
        else:
            self.check_.setChecked(False)

    def all_state_changed(self):
        """
        全选按钮槽函数
        这个方法会被执行 n次（实例化的个数），因为每实例化一次就会传递一个check_all对象，这里实例化了10次，
        顾有10个check_all对象，每个对象都绑定了信号/槽，顾stateChanged触发时会执行10次，这里的每个check_all
        只对应一个checkbox即实例化时的checkbox，顾这里想全选需循环获取不同的checkbox
        :return:
        """

        # 获取当前复选框状态
        # 注意这里的self.check_是实例化的时候传进来的，这里实际上是存在10个实例属性self.check_，
        # 顾点击的时候会从上往下，依次获取self.check_对应的checkbox，从而一个一个的改变复选框状态.......
        state = self.check_.checkState()

        if state == Qt.Checked:
            for index in range(self.list_.count()):
                # 通过self.list_.itemWidget(self.list_.item(index)).checkbox一层一层找，直到找到checkbox
                # self.list_.itemWidget(self.list_.item(index))： 通过index找到对应的checkbox，然后判断其状态
                check_box = self.list_.itemWidget(self.list_.item(index)).checkbox
                check_box.setChecked(True)

        elif state == Qt.Unchecked:
            # 注意，这里的self.checkbox是实例属性，当我们循环创建自定义控件时会同时创建多个实例，
            # 从而存在多个self.checkbox实例属性
            # 这里的self.checkbox 是上面选中全选框时，会依次将self.check_对应的checkbox对象添加进来
            # 也就是10个，所以，这里设置取消状态时，不需要迭代了......
            self.checkbox.setChecked(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())


