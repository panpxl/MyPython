#!/usr/bin/env python3
# -*- coding: utf-8 -*-

names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
d['Adam']=67
print(d)
print('Thomas' in d)
print(d.get('Thomas',-1))
print(d)
d.pop('Bob')
print(d)
