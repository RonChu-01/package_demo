import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLCDNumber, QPushButton


def setTime():
  global sec
  sec += 1
   # LED显示数字+1
  lcdNumber.display(sec)

def work():
    #每秒计数
   timer.start(1000)
   # 开始一次非常耗时的计算
   # 这里用一个2 000 000 000次的循环来模拟
   for i in range(200000000):
      pass
      timer.stop()


if __name__ == "__main__":
  app = QApplication(sys.argv)
  top = QWidget()
  top.resize(300, 120)
  # 垂直布局类
  layout = QVBoxLayout(top)
   # 添加控件
  lcdNumber = QLCDNumber()
  layout.addWidget(lcdNumber)
  button = QPushButton("测试")
  layout.addWidget(button)
  timer = QTimer()
  # 每次计时结束，触发setTime
  timer.timeout.connect(setTime)
  # 连接测试按钮和槽函数
  button.clicked.connect(work)
  top.show()
  sys.exit(app.exec_())
