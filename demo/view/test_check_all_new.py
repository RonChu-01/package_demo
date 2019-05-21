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
    QListWidgetItem, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QSize, QEvent, QPoint, Qt, pyqtSignal
from PyQt5.QtGui import QMouseEvent

cgitb.enable(format="text")


class Window(QWidget):
    """  主窗口 """

    def __init__(self):
        super(Window, self).__init__()

        self.resize(1000, 600)

        # 左侧列表复选框选中状态计数
        self.checked_count = 0

        # 左右列表对应关系
        self.left_to_right = []

        # 全局水平布局
        h_box = QHBoxLayout(self)

        # 左侧列表布局
        left_v_box = QVBoxLayout()
        self.left_list = QListWidget()
        left_v_box.addWidget(self.left_list)

        # 右侧列表布局
        right_v_box = QVBoxLayout()
        self.right_list = QListWidget()
        self.right_item = None
        self.right_widget = None
        right_v_box.addWidget(self.right_list)
        # self.btn_set_text = QPushButton("设置")
        # right_v_box.addWidget(self.btn_set_text)
        # 按钮绑定触发自定义控件发射自定义信号槽函数
        # self.btn_set_text.clicked.connect(self.do_set_label_text)

        # 将左右布局加入主布局中
        h_box.addLayout(left_v_box)
        h_box.addLayout(right_v_box)

        # 全选按钮
        self.check_all = QCheckBox("全选", objectName="checked_all")
        # 这里使用clicked信号不使用stateChanged信号是防止误动作
        self.check_all.clicked.connect(self.check_all_state_changed)

        # self.check_all.checkState()

        left_v_box.addWidget(self.check_all)

        # self.left_list.indexFromItem()

        for i in range(10):
            self.left_item = QListWidgetItem(self.left_list)
            self.left_item.setSizeHint(QSize(0, 50))
            # 注意，这里是通过循环动态生成自定义控件，这里传参相当于是存在多个实例属性
            self.left_widget = LeftItemWidget(self.left_item, self.left_list)
            self.left_widget.checkbox.stateChanged.connect(self.check_state_changed)
            self.left_list.setItemWidget(self.left_item, self.left_widget)

    def check_state_changed(self, state):
        """
        复选框槽函数
        :param state:
        :return:
        """
        # 发送自定义事件，解决复选框选中无法选中当前行的问题
        # 注意一个问题，这里的事件一定要放在槽函数的最前面执行，否则会出现行选中紊乱错误（获取当前行时会报错）
        event = QMouseEvent(QEvent.MouseButtonPress, QPoint(0, 0), Qt.RightButton, Qt.RightButton, Qt.NoModifier)
        QApplication.sendEvent(self.sender(), event)

        # for index in range(self.left_list.count()):
        #     check_box = self.left_list.itemWidget(self.left_list.item(index)).checkbox
        #     if self.sender() == check_box:
        #         self.left_list.item(index).setCheckState(True)
        #         print(self.left_list.item(index))
        #         print(index)

        result = {
            "left_row": 0,
            "right_row": 0
        }

        row = self.left_list.currentRow()
        result["left_row"] = row

        right_list_count = self.right_list.count()

        # 勾选左侧复选框，右侧列表添加对应的内容
        if state == Qt.Checked:
            # 列表复选框选中状态计数
            self.checked_count += 1

            result["right_row"] = right_list_count - 1
            self.left_to_right.append(result)

            # 通过选中左侧复选框动态给右侧列表添加控件
            self.right_item = QListWidgetItem(self.right_list)
            self.right_item.setSizeHint(QSize(0, 50))
            # self.right_widget = QLabel("这是对应左侧第{0}个选项的数据".format(self.left_list.currentRow()))
            # self.right_widget = RightItemWidget(self.right_item, self.right_list)
            self.right_widget = RightItemWidget(self.right_item, self.right_list)
            # 初始化自定义控件的同时，自定义信号绑定槽函数
            self.right_widget.itemDelete.connect(self.do_delete_item)
            # self.right_widget.setLabelText.connect(self.set_label_text)
            self.right_list.setItemWidget(self.right_item, self.right_widget)

            result["right_row"] += 1

        elif state == Qt.Unchecked:
            # 列表复选框选中状态计数
            self.checked_count -= 1

            for i in self.left_to_right:
                if row == i["left_row"]:
                    index = i["right_row"]
                    # 通过index获取所在item，takeItem删除
                    item = self.right_list.takeItem(index)
                    # 删除左侧选择待删除渠道对应的右侧元素
                    self.right_list.removeItemWidget(item)
                    del item

                    # 移除results中已经删除的对应关系
                    self.left_to_right.pop(index)
                    # 删除后，右侧列表索引-1
                    result["right_row"] -= 1

            # 对右侧列表重新进行排序
            # 将右侧列表的索引重新赋值，对应右边的列表索引
            # 注意，左边的列表的索引是固定的，右边的是动态生成
            for j, k in enumerate(self.left_to_right):
                k["right_row"] = j

        if self.checked_count == self.left_list.count():
            self.check_all.setChecked(True)
        else:
            self.check_all.setChecked(False)

    def check_all_state_changed(self):
        """
        全选按钮槽函数
        :return:
        """
        state = self.check_all.checkState()

        if state == Qt.Checked:
            # self.right_list.clear()
            for index in range(self.left_list.count()):
                check_box = self.left_list.itemWidget(self.left_list.item(index)).checkbox
                check_box.setChecked(True)

        elif state == Qt.Unchecked:
            for index in range(self.left_list.count()):
                check_box = self.left_list.itemWidget(self.left_list.item(index)).checkbox
                check_box.setChecked(False)

    def do_delete_item(self, item):
        """
        自定义删除信号槽函数
        :param item: 接收自定义控件定义的自定义删除信号发射过来携带的参数
        :return:
        """
        # 通过自定义控件中自定义信号发射的信号携带的item找到事件源控件所在的行
        row = self.right_list.indexFromItem(item).row()

        # 循环遍历左右列表对应关系，通过右边的row反找出对应的左边的列表控件，然后执行点击操作
        for i in self.left_to_right:
            if row == i["right_row"]:
                left_index = i["left_row"]
                left_check_box = self.left_list.itemWidget(self.left_list.item(left_index)).checkbox
                # 由于之前的checkbox绑定的是点击信号，顾这里通过item找到index，执行点击操作，相关逻辑还是走之前的逻辑
                left_check_box.click()

    # def set_label_text(self, item, label):
    #     right_row = self.right_list.indexFromItem(item).row()
    #     for i in self.left_to_right:
    #         if right_row == i["right_row"]:
    #             left_row = i["left_row"]
    #             label.setText("这是右边列表第{0}项对应的内容".format(left_row))

    # def do_set_label_text(self):
    #     """
    #     触发自定义事件自定义信号，发射信号槽函数
    #     :return:
    #     """
    #     self.right_widget.do_set_label_text()


class LeftItemWidget(QWidget):
    """  自定义列表item控件，用于插入自定义控件
         自定义控件时，注意区分实例属性和类属性
         相关内容需要对应各自的实例，否则无法进行操作
    """

    def __init__(self, item, *args, **kwargs):
        """
        自定义控件初始化
        :param item: 注意这里的item是实例属性，由上面初始化时传递，每个item对应不同实例
        有多少个实例就有多少个实例属性
        :param args:
        :param kwargs:
        """
        super(LeftItemWidget, self).__init__(*args, **kwargs)
        self.item_ = item  # 实例属性，不同实例拥有不同的实例属性，虽然名字是相同的
        # self.check_ = check_all  # 实例属性，不同实例拥有不同的实例属性，虽然名字是相同的
        self.list_ = args[0]
        # 每实例化一次，获取当前的item所在的行
        row = self.list_.indexFromItem(self.item_).row()

        h_box = QHBoxLayout(self)
        self.checkbox = QCheckBox("选项{0}".format(row))
        self.label = QLabel("这是第{0}标签".format(row))
        h_box.addWidget(self.checkbox)
        h_box.addWidget(self.label)

#
# class RightItemWidget(QWidget):
#     """  右侧列表自定义item """
#
#     # 自定义控件，自定义删除信号
#     itemDelete = pyqtSignal(QListWidgetItem)
#
#     def __init__(self, item, *args, **kwargs):
#         super(RightItemWidget, self).__init__(*args, **kwargs)
#
#         self.item_ = item
#         self.list_ = args[0]
#
#         h_box = QHBoxLayout(self)
#         self.label = QLabel("这是右边列表第{0}项内容".format(self.list_.indexFromItem(self.item_).row()))
#         self.button = QPushButton("X")
#         # 删除按钮绑定自定义槽函数，用于发射删除信号
#         self.button.clicked.connect(self.do_delete_item)
#         h_box.addWidget(self.label)
#         h_box.addWidget(self.button)
#
#     def do_delete_item(self):
#         """
#         自定义控件，删除按钮槽函数，用于发射自定义删除信号，携带self.item_参数，方便上层函数执行相应的操作
#         :return:
#         """
#         self.itemDelete.emit(self.item_)

#
# class RightItemWidget(QWidget):
#     """  右侧列表自定义item """
#
#     # 自定义控件，自定义删除信号
#     itemDelete = pyqtSignal(QListWidgetItem)
#
#     setLabelText = pyqtSignal(QListWidgetItem, QLabel)
#
#     def __init__(self, item, *args, **kwargs):
#         super(RightItemWidget, self).__init__(*args, **kwargs)
#
#         self.item_ = item
#         self.list_ = args[0]
#
#         h_box = QHBoxLayout(self)
#         self.label = QLabel("这是右边列表第{0}项对应的内容".format(""))
#         # self.label.setText()
#         self.button = QPushButton("X")
#         # 删除按钮绑定自定义槽函数，用于发射删除信号
#         self.button.clicked.connect(self.do_delete_item)
#         self.button2 = QPushButton("设置")
#         self.button2.clicked.connect(self.do_set_label_text)
#         h_box.addWidget(self.label)
#         h_box.addWidget(self.button)
#         h_box.addWidget(self.button2)
#
#     def do_delete_item(self):
#         """
#         自定义控件，删除按钮槽函数，用于发射自定义删除信号，携带self.item_参数，方便上层函数执行相应的操作
#         :return:
#         """
#         self.itemDelete.emit(self.item_)
#
#     def do_set_label_text(self):
#         self.setLabelText.emit(self.item_, self.label)
#


class RightItemWidget(QWidget):
    """  右侧列表自定义item """

    # 自定义控件，自定义删除信号
    itemDelete = pyqtSignal(QListWidgetItem)

    # setLabelText = pyqtSignal(QListWidgetItem, QLabel)

    def __init__(self, item, *args, **kwargs):
        super(RightItemWidget, self).__init__(*args, **kwargs)

        self.item_ = item
        self.list_ = args[0]

        t_h_box = QHBoxLayout(self)
        # self.label = QLabel("这是左边边列表第{0}项对应的内容".format(""))
        # self.label = QLabel("这是右边列表第{0}项".format(self.list_.indexFromItem(self.item_).row()))
        self.label = QLabel("右边列表项")
        # self.label.setText()
        self.button = QPushButton("X")
        # 删除按钮绑定自定义槽函数，用于发射删除信号
        self.button.clicked.connect(self.do_delete_item)
        t_h_box.addWidget(self.label)
        t_h_box.addWidget(self.button)

        # print(self.left_to_right_)

        # self.setLabelText.emit(self.item_, self.label)

    def do_delete_item(self):
        """
        自定义控件，删除按钮槽函数，用于发射自定义删除信号，携带self.item_参数，方便上层函数执行相应的操作
        :return:
        """
        self.itemDelete.emit(self.item_)

    # def do_set_label_text(self):
    #     self.setLabelText.emit(self.item_, self.label)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())


