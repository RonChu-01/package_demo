# -*- coding: utf-8 -*-
# Author:chuyong
# CreateTime:2019/5/5 17:37

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt


class MyLabel(QLabel):

    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        self.setText('Lorem Ipsum')

    def mouseReleaseEvent(self, event):
        print('Label clicked!')


class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()
        # self.label = MyLabel()
        # h_box = QHBoxLayout()
        # h_box.addWidget(self.label)
        # self.setLayout(h_box)

        self.label = QLabel()

        # 去掉超链接下划线
        self.label.setText('''<style> a {text-decoration: none} </style> 
        <a href='http://stackoverflow.com'>stackoverflow</a>''')

        # self.label.setText('''stackoverflow''')

        self.label.setOpenExternalLinks(True)  # 使用这句话就会不会触发linkActivated信号

        h_box = QHBoxLayout()
        h_box.addWidget(self.label)
        self.setLayout(h_box)

        # self.label.linkActivated.connect(self.do_something)

    def do_something(self):
        self.label.setText('''
        <style> a {text-decoration: none} </style>
        <a style='color: red;' href='http://stackoverflow.com'>stackoverflow</a>
        ''')
        print('hello')
        # self.label.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())



