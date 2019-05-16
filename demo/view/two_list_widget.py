import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QCheckBox
from ui.two_list_widget import Ui_Form
from PyQt5.QtCore import Qt, QSize


class Window(QWidget, Ui_Form):

    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)

        left_v_box = QVBoxLayout(self.left_widget)

        self.left_list_widget = QListWidget()
        left_v_box.addWidget(self.left_list_widget)

        # self.left_list_widget.clicked.connect(self.right_add_widget)

        # self.left_widget.setLayout(left_v_box)

        for i in range(10):

            self.item = QListWidgetItem(self.left_list_widget)
            self.item.setSizeHint(QSize(40, 40))
            self.cb_widget = QCheckBox('hello: {0}'.format(i), self.left_list_widget)
            self.cb_widget.id_ = i

            self.cb_widget.stateChanged.connect(self.right_add_widget)

            self.left_list_widget.setItemWidget(self.item, self.cb_widget)

        # 右边列表和左边列表对应关系
        self.result = []

        """
        -------------------------------------------
        """

        right_v_box = QVBoxLayout()

        self.right_list_widget = QListWidget()
        right_v_box.addWidget(self.right_list_widget)

        self.right_widget.setLayout(right_v_box)

    def right_add_widget(self, state):

        # 左边list行数索引，右边list动态添加控件数量/索引
        index_l = {
            'row': 0,
            'count': -1
        }

        item = self.left_list_widget.currentItem()
        row = self.left_list_widget.indexFromItem(item).row()

        print(row)

        # 当前点击item索引
        index_l['row'] = row

        if state == Qt.Checked:

            # 左边列表元素索引对应右边元素索引
            rlw_count = self.right_list_widget.count()
            # 右边元素索引为当前数量-1
            index_l['count'] = rlw_count - 1

            self.result.append(index_l)

            item1 = QListWidgetItem('hello: {0}'.format(row), self.right_list_widget)
            self.right_list_widget.insertItem(row, item1)

            # 右边元素数量加一
            index_l['count'] += 1

        if state == Qt.Unchecked:

            item2 = self.left_list_widget.currentItem()
            row2 = self.left_list_widget.indexFromItem(item2).row()

            rlw_count = self.right_list_widget.count()

            # 循环遍历，通过左边的item的索引查询右边列表对应的索引/控件
            for i in self.result:

                # if self.result.count(i['count']) > 1:
                #     self.result.count(i['count'])

                if i['row'] == row2:
                    index_ = i['count']

                    item_ = self.right_list_widget.takeItem(index_)

                    self.right_list_widget.removeItemWidget(item_)
                    del item_

                    index_l['count'] = rlw_count

                    self.result.pop(index_)

                    index_l['count'] -= 1

            # 对列表重新进行排序
            # 将右侧列表的索引重新赋值，对应右边的列表索引
            # 注意，左边的列表的索引是固定的，右边的是动态生成
            for j, k in enumerate(self.result):
                k['count'] = j

        print(self.result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())



