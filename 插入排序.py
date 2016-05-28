#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

list_data = []
for i in range(20):
    list_data.append(random.randint(0, 1000))
print(list_data)

list_len = len(list_data)
for i in range(1, list_len):
    j = 0
    is_swap = False
    while j < i:
        if list_data[j] > list_data[i]:
            is_swap = True
            break
        j += 1
    if not is_swap:
        continue
    tmp = list_data[i]
    k = i
    while k > j:
        list_data[k] = list_data[k - 1]
        k -= 1
    list_data[k] = tmp
    print("y i=%d,%s" % (i, list_data))
print(list_data)
