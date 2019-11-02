# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 23:55:40 2019

@author: tangpeng
"""

# 请用匿名函数改造下面的代码：
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))

print(L)

L = list(filter(lambda x: x%2==1, range(1, 20)))

print(L)

# 匿名函数作为返回值
def build(x, y):
    return lambda: x * x + y * y

print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))