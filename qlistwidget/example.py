# -*- coding: utf-8 -*-
# Created by #chuyong, on 2019/8/14.
# Copyright (c) 2019 3KWan.
# Description :
import queue
from queue import Queue
import cgitb

from PyQt5.QtCore import QSize, pyqtSignal, Qt
from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QListWidget, QVBoxLayout

from qlistwidget.ui.ui_main import Main_Ui_Form
from qlistwidget.ui.ui_first_item import First_Ui_Form
from qlistwidget.ui.ui_second_item import Second_Ui_Form

cgitb.enable(format="text")


class FirstItemWidget(QWidget, First_Ui_Form):
    """  第一个列表item_widget """

    del_item = pyqtSignal(object)  # 删除信号
    check_item = pyqtSignal(object, object, str)  # 勾选复选框

    def __init__(self, item, text, *args, **kwargs):
        super(FirstItemWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.item = item
        self.text = str(text)
        self.lb_no.setText("咸鱼{0}号".format(str(text)))
        self.btn_del.clicked.connect(self.do_delete_item)
        self.cbx.stateChanged.connect(self.do_check_item)

    def do_delete_item(self):
        """
        删除item
        :return:
        """
        # 发射删除信号，携带当前item信息
        self.del_item.emit(self.item)

    def do_check_item(self, state):
        """
        勾选item
        :return:
        """
        self.check_item.emit(self.item, state, self.text)


class SecondItemWidget(QWidget, Second_Ui_Form):
    """  第二个列表item_widget """

    def __init__(self, item, text, *args, **kwargs):
        super(SecondItemWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.item = item
        self.text = text
        self.label.setText(str(text))


class Window(QWidget, Main_Ui_Form):
    """  主页 """

    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.init()

        self.index_ = 0  # list计数
        self.select_item_info = Queue()  # 第一个列表已选择item
        self.second_list_info = Queue()  # 保存第一个列表勾选内容用于生成第二个列表

        v_box = QVBoxLayout(self.wdt_content)
        self.first_list = QListWidget(self)
        v_box.addWidget(self.first_list)

        v_box_second = QVBoxLayout(self.second_wdt_content)
        self.second_list = QListWidget(self)
        v_box_second.addWidget(self.second_list)

    def init(self):
        self.btn_first.clicked.connect(self.do_switch_page)
        self.btn_second.clicked.connect(self.do_switch_page)
        self.btn_three.clicked.connect(self.do_switch_page)
        self.btn_add.clicked.connect(self.do_init_first_list)
        self.btn_clear.clicked.connect(self.do_clear_first_list)
        self.first_btn_choose.clicked.connect(self.do_pass_select_item)
        self.btn_second.clicked.connect(self.do_init_second_list)

    def do_init_second_list(self):
        """
        初始化第二个列表
        :return:
        """

        if self.second_list_info.qsize() == 0:
            return

        try:
            for i in range(self.second_list_info.qsize()):
                # 无等待取值，队列为空时，抛出异常
                item_, text = self.second_list_info.get_nowait()  # 元组拆包
                item = QListWidgetItem(self.second_list)
                item.setSizeHint(QSize(0, 60))
                widget = SecondItemWidget(item, text)
                self.second_list.setItemWidget(item, widget)
        except queue.Empty as e:
            pass

    def do_pass_select_item(self):
        """
        第一个列表点击通过按钮
        :return:
        """
        if self.select_item_info.qsize() == 0:
            return

        for i in range(self.select_item_info.qsize()):
            # 队列为空，会阻塞
            item, text = self.select_item_info.get()
            self.second_list_info.put((item, text))
            index = self.first_list.indexFromItem(item).row()
            self.first_list.takeItem(index)
            self.first_list.removeItemWidget(item)
            del item

        if self.first_list.count() == 0:
            self.index_ = 0

    def do_init_first_list(self):
        """
        初始化第一个列表
        :return:
        """
        item = QListWidgetItem(self.first_list)
        item.setSizeHint(QSize(0, 60))
        widget = FirstItemWidget(item, "{0}".format(self.index_))
        # item删除信号绑定槽函数（通过信号和槽无需知道当前点击的是哪一行，信号携带item信息）)
        widget.del_item.connect(self.do_del_item)
        widget.check_item.connect(self.do_select_item)
        self.first_list.setItemWidget(item, widget)
        self.index_ += 1

    def do_select_item(self, item, state, text):
        """
        选择复选框
        :param item:
        :param state:
        :param text:
        :return:
        删除item，可以点击的时候保存item信息再执行删除，不用for循环？
        """
        index = self.first_list.indexFromItem(item).row()
        if state == Qt.Checked:
            self.select_item_info.put((item, text))
        elif state == Qt.Unchecked:
            # 队列为空，会阻塞
            self.select_item_info.get()

    def do_del_item(self, item):
        """
        删除item槽函数
        :return:
        """
        index = self.first_list.indexFromItem(item).row()  # 获取item所在位置
        # Removes and returns the item from the given row in the list widget; otherwise returns None .
        item_ = self.first_list.takeItem(index)  # 删除item
        self.first_list.removeItemWidget(item_)  # 删除widget
        del item_

        # 列表为空置零计数
        if self.first_list.count() == 0:
            self.index_ = 0

    def do_clear_first_list(self):
        """
        清空第一个列表
        :return:
        """
        self.first_list.clear()
        self.index_ = 0  # 恢复计数，注意存在类似的参数在使用完毕后都要执行清空或恢复操作

    def do_switch_page(self):
        """
        切换页面
        :return:
        """
        object_name = self.sender().objectName()
        if object_name == "btn_first":
            self.stackedWidget.setCurrentWidget(self.first)
        elif object_name == "btn_second":
            self.stackedWidget.setCurrentWidget(self.second)
        elif object_name == "btn_three":
            self.stackedWidget.setCurrentWidget(self.three)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())
