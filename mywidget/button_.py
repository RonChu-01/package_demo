import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout


StyleSheet = """
#my_btn {
    background-color: red;
    border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: beige;
    font: bold 14px;
    min-width: 10em;
    padding: 6px;
}

#my_btn:pressed {
    background-color: rgb(224, 0, 0);
    border-style: inset;
}

"""


class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()
        h_box = QHBoxLayout()
        btn = QPushButton('样式', objectName='my_btn')
        h_box.addWidget(btn)
        self.setGeometry(300, 300, 300, 300)
        self.setLayout(h_box)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(StyleSheet)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())
