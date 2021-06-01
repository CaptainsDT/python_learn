#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 5位数依次打印出个数字

import os
import sys

num = 12345
w = 10000
for i in range(5):
    print(num // w)
    num = num % w
    w = w // 10