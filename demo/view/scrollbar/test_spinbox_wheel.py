# -*- coding: utf-8 -*-
# Created by #chuyong, on 2019/5/30.
# Copyright (c) 2019 3KWan.
# Description :

import cgitb

from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QApplication, QWidget, QSpinBox, QVBoxLayout

cgitb.enable(format="text")


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.resize(300, 150)
        self.spinbox = QSpinBox()
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.spinbox)
        vbox.addStretch(1)

        self.spinbox.installEventFilter(self)

    def event(self, evt):
        """

        :param evt:
        :return:
        """
        if evt.type() == QEvent.Wheel:
            print("1")
            return False
        return super(Window, self).event(evt)

    # def wheelEvent(self, event):
    #     """
    #     重写滚动条事件
    #     :param event:
    #     :return:
    #     """
    #     num_degrees = event.angleDelta() / 8
    #     num_steps = num_degrees / 15

    # def eventFilter(self, obj, event):
    #     """
    #     过滤掉滚动事件
    #     :param obj:
    #     :param event:
    #     :return:
    #     """
    #     if event.type() == QEvent.Wheel:
    #         return True
    #     return super(Window, self).eventFilter(obj, event)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())


