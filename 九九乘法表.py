#!/usr/bin/env python3
# -*- coding: utf-8 -*-

for i in range(1, 10):
    for j in range(1, i + 1):
        print('{}x{}={}\t'.format(i, j, i * j), end='')
    print()