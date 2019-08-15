# -*- coding: utf-8 -*-
# Created by #chuyong, on 2019/8/2.
# Copyright (c) 2019 3KWan.
# Description :

import os
import logging

from logging import handlers

logging.basicConfig(format="%(asctime)s - %(module)s[line:%(lineno)d] - %(funcName)s - %(thread)d - %(levelname)s: %(message)s",
                    level=logging.DEBUG)

logging.info("hello")

# current_path = os.getcwd()
#
# file = open(os.path.join(current_path, "test.txt"), "w")
# file.close()
