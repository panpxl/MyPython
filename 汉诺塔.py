#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input('输入n：'))


def move(n, a, b, c, num=[0]):
    if n == 0:
        pass
    else:
        move(n - 1, a, c, b)
        num[0] = num[0] + 1
        print('%s、%s --> %s' % (num[0], a, c))
        move(n - 1, b, a, c)


move(n, 'A', 'B', 'C')


def hanoi(n, x, y, z):
    if n == 1:
        print(x, '-->', z)
    else:
        hanoi(n - 1, x, z, y)  # 将前n-1个盘子从x移动到y上
        hanoi(1, x, y, z)  # 将最底下的最后一个盘子从x移动到z上
        hanoi(n - 1, y, x, z)  # 将y上的n-1个盘子移动到z上


n = int(input('请输入汉诺塔的层数：'))
hanoi(n, 'x', 'y', 'z')
