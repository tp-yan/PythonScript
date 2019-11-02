#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 10:57:28 2019

@author: tangpeng

操作文件和目录练习
1. 利用os模块编写一个能实现dir -l输出的程序。

"""
import os
from datetime import datetime

pwd = os.path.abspath(".")
print('     Size    Last Modified   Name')
print('------------------------------------------------------------')
for f in os.listdir(pwd):
    msize = os.path.getsize(f)
    # os.path.getmtime(f):返回最近文件修改时间（浮点型秒数）
    mdatetime = datetime.fromtimestamp(os.path.getmtime(f)) # 返回datetime对象
    format_time = mdatetime.strftime("%Y-%m-%d %H:%M")
    flag = "/" if os.path.isdir(f) else "" # 添加目录标志
    print("%10d %s %s%s" %(msize,format_time,f,flag))
    