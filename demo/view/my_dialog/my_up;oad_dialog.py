# -*- coding: utf-8 -*-
# Created by #chuyong, on 2019/5/20.
# Copyright (c) 2019 3KWan.
# Description :

import sys
import cgitb
import time

from PyQt5.QtCore import QThread, pyqtSignal, pyqtProperty
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QHBoxLayout, QPushButton, QProgressBar, QLabel

cgitb.enable(format='text')  # 解决PyQt5异常只要进入事件循环,程序就崩溃,而没有任何提示


class UploadThread(QThread):
    """  上传文件子线程 """

    # 自定义信号，携带自定义参数（上传测试成功包体信号）
    upload_package = pyqtSignal(int, str)

    def __init__(self):
        """  线程初始化，初始化前端需要展示的参数数据 """
        super(UploadThread, self).__init__()
        self.value_ = 0
        self.text_ = ""

    # 进度条数值
    @property
    def value(self):
        return self.value_

    @value.setter
    def value(self, value):
        self.value_ = value

    # 进度条对应的打包信息
    @property
    def text(self):
        return self.text_

    @text.setter
    def text(self, value):
        self.text_ = value

    def run(self):
        while self.value <= 100:
            time.sleep(1)
            # 每隔一秒发送一次自定义信号，用于发射上传的进度和信息，更新前端UI
            self.upload_package.emit(self.value, self.text)
            # self.value += 1
            print(self.value)


class InterFaceSetValue(object):
    """  提供给model层的接口 """

    # 定义全局变量，用于静态方法的封装，静态方法可以保证只会存在一个实例，这样就可以复用当前的实例，从而保证实例属性不变
    global upload_thread
    # 创建上传线程对象
    upload_thread = UploadThread()

    def __init__(self):
        super().__init__()

    # 提供给model操作的静态方法，用于设置上传进度情况
    @staticmethod
    def upload(value: int, text: str) -> None:
        upload_thread.value = value
        upload_thread.text = text

    # view层窗口，上传线程的信号绑定的槽函数（供窗口那边调用，静态方法，保证有且仅有一个实例）
    @staticmethod
    def do_start_upload():
        upload_thread.start(100)

    # 获取接口的upload_thread实例，供窗口那边调用，而后进行相关操作
    @staticmethod
    def get_upload_thread():
        return upload_thread


class MyProgress(QWidget):
    """  进度条窗口 """

    def __init__(self):
        super(MyProgress, self).__init__()

        self.resize(400, 300)

        h_box = QHBoxLayout(self)

        self.progressbar = QProgressBar()
        self.progressbar.setMinimum(0)
        self.progressbar.setMaximum(100)
        self.progressbar.setFixedSize(300, 10)

        self.btn_start = QPushButton("Start")
        # 窗口按钮绑定上传接口处定义的槽函数
        self.btn_start.clicked.connect(InterFaceSetValue.do_start_upload)
        self.label = QLabel("测试")

        h_box.addWidget(self.progressbar)
        h_box.addWidget(self.label)
        h_box.addWidget(self.btn_start)

        # 上传进程中的自定义信号绑定槽函数（用于上传进度UI）
        InterFaceSetValue.get_upload_thread().upload_package.connect(self.start_upload)

    # 更新上传进度槽函数
    def start_upload(self, value, text):
        self.progressbar.setValue(value)
        self.label.setText(text)


class CallUpload(QThread):

    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(101):
            time.sleep(1)
            InterFaceSetValue.upload(i, "这是标签{0}".format(i))


class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()

        h_box = QHBoxLayout(self)

        self.btn = QPushButton("测试")
        self.btn.clicked.connect(self.show_dialog)

        h_box.addWidget(self.btn)

    def show_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("这是一个对话框")

        h_box = QHBoxLayout(dialog)
        progress_bar = MyProgress()
        h_box.addWidget(progress_bar)

        dialog.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    call = CallUpload()
    call.start()
    ui.show()
    sys.exit(app.exec_())


