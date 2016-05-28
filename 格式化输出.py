#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1.打印字符串

print("1 His name is %s" % "Aviad")

# 2.打印整数

print("2 He is %d years old" % 25)

# 3.打印浮点数

print("3 His height is %f m" % 1.83)

# 4.打印浮点数（指定保留小数点位数）

print("4 His height is %.2f m" % 1.83)

# 5.指定占位符宽度

print("5 Name:%10s Age:%8d Height:%8.2f" % ("Aviad", 25, 1.83))

# 6.指定占位符宽度（左对齐）

print("6 Name:%-10s Age:%-8d Height:%-8.2f" % ("Aviad", 25, 1.83))

# 7.指定占位符（只能用0当占位符？）

print("7 Name:%-10s Age:%08d Height:%08.2f" % ("Aviad", 25, 1.83))

# 8.科学计数法

print(format(0.0015, '.2e'))
