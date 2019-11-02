#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 11:10:06 2019

@author: tangpeng

日期类datetime与timestamp、str之间的转换
"""

import pytz
print(pytz.all_timezones) # 所有时区

"""
1. 获取当前日期和时间
"""
from datetime import datetime # 从datetime模块导入datetime类
now = datetime.now() # 返回 datetime 对象，包含日期和时间
print(now)
print(type(now))

"""
 2. 获取指定日期和时间 --> 生成datetime对象
"""
dt = datetime(2019,11,11,11,11) # 无法指定秒数
print(dt)

"""
3. datetime转换为timestamp
1970年1月1日 00:00:00 称为epoch time
timestamp是相对于epoch time的秒数。1970年以前的时间timestamp为负数。
全球各地的计算机在任意时刻的timestamp（数值）都是完全相同的。
timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。

"""
print(dt.timestamp())

"""
4. timestamp转换为datetime
timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。
默认转换是在timestamp和本地时间做转换。
"""
t = 1429417200.0
dt = datetime.fromtimestamp(t)
print(dt,dt.tzinfo)
# timestamp也可以直接被转换到UTC标准时区的时间
utc_dt = datetime.utcfromtimestamp(t)
print(utc_dt,utc_dt.tzinfo) # UTC时间，即格林威治标准时间

"""
5. str转换为datetime
把`str`转换为`datetime`。转换方法是通过`datetime.strptime()`实现，需要一个日期和时间的格式化字符串
"""
cday = datetime.strptime("2015-06-01 18:19:59","%Y-%m-%d %H:%M:%S")
print(cday) # 注意转换后的datetime是没有时区信息的

"""
6. datetime转换为str
转换方法是通过`strftime()`实现的，**同样需要一个日期和时间的格式化字符串**
"""
now = datetime.now()
print(now.strftime("%a, %b %d %H:%M")) 

"""
7. datetime加减
datetime加减可以直接用`+`和`-`运算符，不过需要导入`timedelta`这个类
"""
from datetime import timedelta
now = datetime.now()
print(now)
print(now+timedelta(hours=10))
print(now-timedelta(days=1))
print(now+timedelta(days=2,hours=1,seconds=22))

"""
8. 本地时间转换为UTC时间
本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。
一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，
除非强行给datetime设置一个时区
"""
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
now = datetime.now()
print(now) # 所有datetime默认都是没有时区的
print(now.timestamp())

dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00。如果系统时间就是UTC+8那么timestamp不变，若是其他时区则会改变
print(dt) # xxx +08:00
print(dt.timestamp())

"""
9. 时区转换
先通过utcnow()拿到当前的UTC时间，然后强制设置时区，再转换为任意时区的时间。
利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。
"""
utc_dt = datetime.utcnow() # 虽然是utc的时间，但是不会带有时区标识
print(utc_dt)
utc_dt = utc_dt.replace(tzinfo=timezone.utc) # 添加时区标识
print(utc_dt)
# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8))) # 时间是北京时间，同时还有时区标识
print(bj_dt)
# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# astimezone()将bj_dt转换时区为东京时间
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))

"""
注：datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。
"""

"""
练习
假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：
"""
import re
def to_timestamp(dt_str, tz_str):
    print("===================")
    dt = datetime.strptime(dt_str,"%Y-%m-%d %H:%M:%S")
    
    regx = r'UTC(\+|\-)([0-9]|0[0-9]|1[0-9]|2[0-3]):(\d{2})'
    infos = re.match(regx,tz_str).groups()
    flag = infos[0]
    hour = infos[1]
    minute = infos[2]
    
    utc_x = timezone(timedelta(hours = int(hour) if flag == "+" else -int(hour)))
    dt = dt.replace(tzinfo=utc_x)
    dt = dt + timedelta(minutes=int(minute))
    print(dt)
    return dt.timestamp()
    

# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')