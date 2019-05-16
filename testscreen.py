# -*- coding: utf-8 -*-
# Created by #chuyong, on 2019/5/8.
# Copyright (c) 2019 3KWan.
# Description :

import time
import os


def screenshot(u):
    cn = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    print(cn)
    dr='d:\img\\'+cn+'pic.png'
    touch=os.popen('adb -s ' + u + ' shell  screencap -p /sdcard/screen.png').read()
    touch=os.popen('adb -s ' + u + ' pull /sdcard/screen.png ' + dr).read()
    touch=os.popen('adb -s ' + u + ' shell rm /sdcard/screen.png').read()
    print("screenshot done")


a = os.popen('adb devices').read()
a = a.replace('\n', '')
a = a.replace('List of devices attached', ' ')
a = a.split('device')[0]
print(a)
screenshot(a)



