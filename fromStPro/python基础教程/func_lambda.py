# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:58:50 2019

匿名函数，即lambda关键字定义的函数，一般只有一次或几次，即“一次性”函数
@author: tangpeng
"""

f = lambda x,y: x+y # 将匿名函数赋值给一个变量，参数：x,y
print(f(2,3))
print(f(7,10))

# 对2个数的平方和，只使用一次
print((lambda x,y : x**2 + y**2)(3,4))
