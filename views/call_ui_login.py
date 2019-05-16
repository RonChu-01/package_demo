import sys
import os
import threading

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from modles.ui_login import Ui_Form
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5 import QtCore
from modles.ui_main_page import Ui_MainWindow
from db.mysql_db_pool import *


# 登录窗口
class LoginPage(QDialog, Ui_Form):

    def __init__(self, parent=None):
        super(LoginPage, self).__init__(parent)
        self.setupUi(self)
        self.custom_style()

    def custom_style(self):

        # 设置窗口固定大小
        self.resize(370, 506)
        self.setFixedSize(370, 506)

        # 去掉标题栏
        self.setWindowFlags(Qt.FramelessWindowHint)

        # 给指定按钮设置icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image/login/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(18, 18))
        # self.pushButton.setAutoRepeatDelay(200)

        # 对指定的pushButton进行样式更改，注意需要指定对应的控件，否则会将所有的QPushButton磊设置
        # self.pushButton.setStyleSheet('QPushButton{border-image: url(quit.png);}')

        # 将按钮边框隐藏
        # self.pushButton.setStyleSheet('QPushButton{border: none;}')
        self.pushButton.setStyleSheet('border: none;')

        # 设置图标
        icon_2 = QtGui.QIcon()
        icon_2.addPixmap(QtGui.QPixmap('../image/login/fly.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon_2)
        self.pushButton_3.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_3.setStyleSheet('border: none')

        # 设置用户图标
        icon_3 = QtGui.QIcon()
        icon_3.addPixmap(QtGui.QPixmap('../image/login/user.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon_3)
        self.pushButton_4.setIconSize(QtCore.QSize(18, 18))
        self.pushButton_4.setStyleSheet('border: none')

        # 用户名输入框设置无边框
        self.lineEdit.setStyleSheet(
            # 'background:transparent;'
            'border-width:0;'
            'border-style:outset'
        )

        # 用户名输入框widget设置背景色为白色
        self.widget_3.setStyleSheet(
            # 'background:transparent;'
            'background-color: white'
        )

        # 设置密码图标
        icon_4 = QtGui.QIcon()
        icon_4.addPixmap(QtGui.QPixmap('image/login/passwd.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon_4)
        self.pushButton_5.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_5.setStyleSheet('border: none')

        # 密码输入框设置无边框
        self.lineEdit_2.setStyleSheet(
            'border-width:0;'
            'border-style:outset'
        )

        # 密码输入框widget设置背景色为白色
        self.widget_4.setStyleSheet(
            'background-color: white;'
        )

        # 底部分割线条
        icon_5 = QtGui.QIcon()
        icon_5.addPixmap(QtGui.QPixmap('image/login/circle.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon_5)
        self.pushButton_6.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_6.setStyleSheet('border: none')

        # 忘记密码、注册、控制台设置下划线
        self.label_2.setText('<u>忘记密码</>')
        self.label_5.setText('<u>注册</u>')
        self.label_6.setText('<u>控制台</u>')

        # 设置注册、控制台标签字体的颜色
        self.label_5.setStyleSheet('color: rgb(90, 170 ,220)')
        self.label_6.setStyleSheet('color: rgb(90, 170 ,220)')

        # 设置登录按钮背景色
        # 设置字体颜色
        self.pushButton_2.setStyleSheet(
            'background-color: rgb(90, 170 ,220);'
            'border: none;'
            'color:white;'
        )

        # 密码输入框设置密码模式
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

        # 绑定关闭事件回调-----------------------------------------------------------------------
        self.pushButton.clicked.connect(self.close)

        # 设置鼠标悬停----变手势图标
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_6.setCursor(QCursor(Qt.PointingHandCursor))

        # 账号密码输入框设置提示信息
        self.lineEdit.setPlaceholderText('请输入账号')
        self.lineEdit_2.setPlaceholderText('请输入密码')

        self.pushButton_2.clicked.connect(self.check_login)

    # 登录逻辑
    # 登录相关校验
    def check_login(self):
        # 如果登录校验通过，跳转至主页面，并设置QDialog为accept

        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        conn = MyPymysqlPool("notdbMysql")

        sql_ = 'SELECT * FROM flask_blog.auth_user WHERE username={0} AND PASSWORD={1}'.format(repr(username), repr(password))
        result_ = conn.getOne(sql_)

        if username == '':
            QMessageBox.warning(self,
                                '警告',
                                '用户名不能为空',
                                QMessageBox.Yes
                                )
            self.lineEdit.setFocus()

        elif password == '':
            QMessageBox.warning(self,
                                '警告',
                                '密码不能为空',
                                QMessageBox.Yes
                                )
            self.lineEdit_2.setFocus()

        elif result_:
            self.save_login_info()
            self.accept()

        else:
            QMessageBox.warning(self,
                                '警告',
                                '用户名或密码错误',
                                QMessageBox.Yes)

    # 以配置文件的形式，保存登录信息至本地
    def save_login_info(self):
        settins = QSettings('configs.ini', QSettings.IniFormat)
        settins.setValue('username', self.lineEdit.text())
        settins.setValue('password', self.lineEdit_2.text())
        settins.setValue('is_remember', self.checkBox.isChecked())


    """
    -------------------------------------
    窗口拖动
    重载鼠标事件方法
    -------------------------------------
    """
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False

    """
    -------------------------------------
    重构 def closeEvent(self, event): 函数
    pyqt点击右上角关闭界面但子线程仍在运行
    关于守护进程这边到时再看看
    -------------------------------------
    """
    def closeEvent(self, event):
        """
        对MainWindow的函数closeEvent进行重构
        退出软件时结束所有进程
        :param event:
        :return:
        """
        reply = QtWidgets.QMessageBox.question(self,
                                               '本程序',
                                               "是否要退出程序？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
            # os._exec(0)

        else:
            event.ignore()

"""
-------------------------------------  主页面  -------------------------------------
"""


class MainPage(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainPage, self).__init__()
        self.setupUi(self)


# 主线程是UI线程
if __name__ == '__main__':

    app = QApplication(sys.argv)

    login_p = LoginPage()

    if login_p.exec_() == QDialog.Accepted:
        main_p = MainPage()
        main_p.show()
        sys.exit(app.exec_())

    # login_p.show()
