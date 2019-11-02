#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:26:08 2019

@author: tangpeng

err.py:用于调试测试的模块
"""

import pdb

s = '0'
n = int(s)
pdb.set_trace() # 相当于断点。程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行：
print(10 / n)