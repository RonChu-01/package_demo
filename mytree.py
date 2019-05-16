# -*- coding: utf-8 -*-
# Author:chuyong
# CreateTime:2019/5/6 16:25
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QFrame, QHBoxLayout, \
    QLabel, QPushButton

from ui_unpack import UuPack_Ui_Form
from ui_unpack_item import UnPack_Item_Ui_Form


StyleSheet = """
#unpack::item{
    height: 65px;
}
"""


class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()

        self.resize(700, 350)

        v_box = QVBoxLayout()

        self.tree = QTreeWidget(objectName='unpack')

        # 设置列数(注意这里是需要插入自定义控件，顾只设置一列，否则会遮挡，显示不全)
        self.tree.setColumnCount(1)

        # 影藏表头
        self.tree.setHeaderHidden(True)

        # 通过Qss设置item高度，其它方式貌似不行
        self.tree.setStyleSheet(StyleSheet)

        v_box.addWidget(self.tree)

        self.setLayout(v_box)

        # 设置QTreeWidget控件间距
        self.tree.setIndentation(0)

        # 设置树形控件头部标题
        # self.tree.setHeaderLabels(['key', 'value'])

        # 根节点
        # root = QTreeWidgetItem(self.tree)
        # root.setText(0, 'root')
        # root.setText(1, '0')

        # 添加自定义根节点控件
        self.root = QTreeWidgetItem()
        self.tree.addTopLevelItem(self.root)
        # 这里通过setItemWidget可添加自定义控件
        # btn = QPushButton('hello')

        # 自定义控件初始化
        unpack = UnPack()

        # 添加自定义控件至首行
        self.tree.setItemWidget(self.root, 0, unpack)

        # btn.clicked.connect(self.on_clicked)

        unpack.pushButton.clicked.connect(self.on_clicked)

        # 子节点1
        child = QTreeWidgetItem(self.root)
        child.setDisabled(True)
        # 这里通过setItemWidget可添加自定义控件
        unpack_item_1 = UnPackItem()
        self.tree.setItemWidget(child, 0, unpack_item_1)
        # 设置子项高度（不然会按默认的样式大小）
        child.setSizeHint(0, QSize(40, 40))

        # 子节点1
        child2 = QTreeWidgetItem(self.root)
        child2.setDisabled(True)
        # 这里通过setItemWidget可添加自定义控件
        unpack_item_2 = UnPackItem()
        self.tree.setItemWidget(child2, 0, unpack_item_2)
        child2.setSizeHint(0, QSize(40, 40))

    # 伸展/折叠槽函数
    def on_clicked(self):
        """toggle expand/collapse of section by clicking
        """
        if self.root.isExpanded():
            self.root.setExpanded(False)
        else:
            self.root.setExpanded(True)


class UnPack(QWidget, UuPack_Ui_Form):

    def __init__(self):
        super(UnPack, self).__init__()
        self.setupUi(self)


class UnPackItem(QWidget, UnPack_Item_Ui_Form):

    def __init__(self):
        super(UnPackItem, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())

