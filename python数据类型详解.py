#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime

oneday = datetime.timedelta(days=1)
# 今天，2014-03-21
today = datetime.date.today()
# 昨天，2014-03-20
yesterday = datetime.date.today() - oneday
# 明天，2014-03-22
tomorrow = datetime.date.today() + oneday
# 获取今天零点的时间，2014-03-21 00:00:00
today_zero_time = datetime.datetime.strftime(today, '%Y-%m-%d %H:%M:%S')

# 0:00:00.001000
print(datetime.timedelta(milliseconds=1))  # 1毫秒
# 0:00:01
print(datetime.timedelta(seconds=1))  # 1秒
# 0:01:00
print(datetime.timedelta(minutes=1))  # 1分钟
# 1:00:00
print(datetime.timedelta(hours=1))  # 1小时
# 1 day, 0:00:00
print(datetime.timedelta(days=1))  # 1天
# 7 days, 0:00:00
print(datetime.timedelta(weeks=1))
