import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QListWidget, QListWidgetItem


class ListWidget(QMainWindow):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.setWindowTitle('ListWindows')
        self.list = QListWidget(self)
        self.list.setSortingEnabled(1)

        item = ['OaK', 'Banana', 'Apple', '  Orange', 'Grapes', 'Jayesh']
        listitem = []

        for lst in item:
            listitem.append(QListWidgetItem(lst))

        for i in range(len(listitem)):
            self.list.insertItem(i + 1, listitem[i])
            self.setCentralWidget(self.list)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = ListWidget()
    ui.show()
    sys.exit(app.exec_())
