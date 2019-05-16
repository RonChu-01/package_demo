# -*- coding: utf-8 -*-
# Created by #chuyong, on 2019/5/15.
# Copyright (c) 2019 3KWan.
# Description : PyQt5事件传递分析和信号解析
"""
启动应用---->事件产生---->QApplication事件处理器---->QWidget事件处理器---->具体事件
"""

import sys

from PyQt5.QtCore import QObject, QEvent
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget


class App(QApplication):
    """  自定义App类，通过继承QApplication，查看事件信息（通常用于调试使用） """

    def notify(self, object_: QObject, event_: QEvent) -> bool:  # python3新特性，类型注解
        """
        所有的时间都是在QApplication中的notify方法中进行处理
        :param object_: 对象类型（参数类型注解为QObject类型）
        :param event_: 事件类型（参数类型注解为QEvent类型）
        :return: -> bool 返回值类型注解为bool类型
        """
        # if object_.inherits("QPushButton"):
        #     if event_.type() == QEvent.MouseButtonPress:
        #         print(object_)
        #         print(event_)

        # print(object_)
        # print(event_)

        # 调用父类方法
        super().notify(object_, event_)
        # 返回False表示：不阻拦事件，将事件信息继续向下传递；如果返回True表示消费事件
        return True


class MyButton(QPushButton):
    """  自定义button """

    def event(self, event_: QEvent):
        """
        复写按钮事件函数
        :param event_:
        :return:
        """
        # 根据事件类型进行分发
        if event_.type() == QEvent.MouseButtonPress:
            print(event_)

        return super().event(event_)

    def mousePressEvent(self, event_: QEvent):
        print("鼠标按下了")
        # 调用父类的mousePressEvent方法，用于发射事件
        return super().mousePressEvent(event_)


class Window(QWidget):
    """  主窗口 """

    def __init__(self):
        super().__init__()
        self.resize(600, 350)
        self.setup_ui()

    def setup_ui(self):
        btn = MyButton(self)
        btn.setText("我的按钮")
        btn.move(100, 100)
        btn.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        print("按钮点击信号槽函数被调用")


if __name__ == "__main__":
    app = App(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())





