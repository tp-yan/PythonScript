# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 10:55:41 2019

@author: cv
"""

"""
偏函数：`functools.partial`的作用就是，把一个函数的某些参数给固定住（也就是传入默认值），返回一个新的函数，调用这个新函数会更简单。
"""

"""
`int()`函数还提供额外的`base`参数，默认值为`10`。如果传入`base`参数，就可以做N进制的转换：
假设要转换大量的二进制字符串，每次都传入`int(x, base=2)`非常麻烦，于是，可以定义一个`int2()`的函数，默认把`base=2`传进去：
"""
def int2(x, base=2):
    return int(x, base)

# `functools.partial`可以帮助我们创建一个偏函数，不需要自己定义`int2()`:
import functools
int2 = functools.partial(int,base=2)
print(int2('1000000'))

# 在调用偏函数时也传入其他值：
print(int2('21',base=8))
