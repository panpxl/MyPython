#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cmath

from Tools.scripts.treesync import raw_input

num = int(raw_input("请输入一个数字: "))
num_sqrt = cmath.sqrt(num)
print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))