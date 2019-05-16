# -*- coding: utf-8 -*-
# Created by #chuyong, on 2019/5/15.
# Copyright (c) 2019 3KWan.
# Description :


class TestAdd(object):

    def __init__(self):
        self.number = 0

    def add(self):
        self.number += 1
        print(self.number)


test_ = TestAdd()

for i in range(5):
    test_.add()
