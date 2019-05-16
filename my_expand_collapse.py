# -*- coding: utf-8 -*-
# Author:chuyong
# CreateTime:2019/5/6 16:25
from PyQt5.QtCore import QSize, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QFrame, QHBoxLayout, \
    QLabel, QPushButton, QListWidgetItem, QLineEdit, QListWidget, QCheckBox

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

        # 创建一个QListWidget对象容器
        self.listWidget = QListWidget()

        # 将QListWidget对象容器添加进布局容器中
        v_box.addWidget(self.listWidget)

        self.setLayout(v_box)

        # file_path = os.path.join(os.path.dirname(__file__))

        for i in range(5):
            self.item = QListWidgetItem(self.listWidget)

            self.item.setSizeHint(QSize(65, 65))

            self.widget = ItemWidget(self.item, self.listWidget)

            self.widget.itemDelete.connect(self.do_delete_item)

            self.listWidget.setItemWidget(self.item, self.widget)

    def do_delete_item(self, item):
        """
        :param item:
        :return:
        """
        row = self.listWidget.indexFromItem(item).row()
        item_ = self.listWidget.takeItem(row)
        self.listWidget.removeItemWidget(item_)
        del item_


class UnPack(QWidget, UuPack_Ui_Form):

    def __init__(self):
        super(UnPack, self).__init__()
        self.setupUi(self)


class UnPackItem(QWidget, UnPack_Item_Ui_Form):

    def __init__(self):
        super(UnPackItem, self).__init__()
        self.setupUi(self)


class ItemWidget(QWidget):
    """自定义ItemWidget"""

    itemDelete = pyqtSignal(QListWidgetItem)

    def __init__(self, item, *args, **kwargs):
        """
        :param item:
        :param args:
        :param kwargs:
        """
        super(ItemWidget, self).__init__(*args, **kwargs)
        self.item_ = item
        # self.item_.setIcon(QIcon(icon))

        h_box = QHBoxLayout(self)
        h_box.setContentsMargins(0, 0, 0, 0)

        self.tree = QTreeWidget(objectName='unpack')

        # 设置列数(注意这里是需要插入自定义控件，顾只设置一列，否则会遮挡，显示不全)
        self.tree.setColumnCount(1)

        # 影藏表头
        self.tree.setHeaderHidden(True)

        # 通过Qss设置item高度，其它方式貌似不行
        self.tree.setStyleSheet(StyleSheet)

        # 设置QTreeWidget控件间距
        self.tree.setIndentation(0)

        # 设置双击不可点击，这个属性是qtreeview，https://doc.qt.io/qt-5/qtreeview.html#expandsOnDoubleClick-prop
        self.tree.setExpandsOnDoubleClick(False)

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

        for i in range(2):
            child = QTreeWidgetItem(self.root)
            child.setDisabled(True)
            # 这里通过setItemWidget可添加自定义控件
            unpack_item = UnPackItem()
            self.tree.setItemWidget(child, 0, unpack_item)
            # 设置子项高度（不然会按默认的样式大小）
            child.setSizeHint(0, QSize(40, 40))

        # # 子节点1
        # child = QTreeWidgetItem(self.root)
        # child.setDisabled(True)
        # # 这里通过setItemWidget可添加自定义控件
        # unpack_item_1 = UnPackItem()
        # self.tree.setItemWidget(child, 0, unpack_item_1)
        # # 设置子项高度（不然会按默认的样式大小）
        # child.setSizeHint(0, QSize(40, 40))
        #
        # # 子节点1
        # child2 = QTreeWidgetItem(self.root)
        # child2.setDisabled(True)
        # # 这里通过setItemWidget可添加自定义控件
        # unpack_item_2 = UnPackItem()
        # self.tree.setItemWidget(child2, 0, unpack_item_2)
        # child2.setSizeHint(0, QSize(0, 40))

        h_box.addWidget(self.tree)

    # 伸展/折叠槽函数
    def on_clicked(self):
        """toggle expand/collapse of section by clicking
        """

        # 获取当前控件子节点数量，用于动态设置item高度
        child_count = self.root.childCount()

        if self.root.isExpanded():
            self.root.setExpanded(False)
            # 收缩时，item恢复默认高度
            self.item_.setSizeHint(QSize(0, 65))
        else:
            self.root.setExpanded(True)
            # 根据控件包含子节点数量动态调整控件高度
            y = 65 + child_count * 40
            self.item_.setSizeHint(QSize(0, y))

    def do_delete_item(self):
        self.itemDelete.emit(self.item_)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())

