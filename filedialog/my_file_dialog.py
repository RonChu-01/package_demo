# -*- coding: utf-8 -*-
# Created by #chuyong, on 2019/8/1.
# Copyright (c) 2019 3KWan.
# Description :
import os
import cgitb

from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QHBoxLayout, QPushButton

cgitb.enable(format='text')  # 解决PyQt5异常只要进入事件循环,程序就崩溃,而没有任何提示

class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()
        h_box = QHBoxLayout(self)
        self.btn = QPushButton("打开文件")
        h_box.addWidget(self.btn)
        self.btn.clicked.connect(self.do_open_file_dialog)
        self.cwd = os.getcwd()
        self.target_file_path = "D:\\fask\\output\\魅族测试Test\\3k_majia"

    def do_open_file_dialog(self):
        os.system("explorer.exe {}".format(self.target_file_path))


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())


