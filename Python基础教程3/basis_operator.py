# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 13:33:57 2019
运算符
@author: tangpeng
"""
a = 1
b = 1
c = 2
print(a == b)   # 判断 值是否相等
print(a == c)   # 判断 值是否不相等
print(a is b)   # 判断 地址(id)是否相同。a,b是指向同一个常量的引用，故id相同
print(a is not b)   # 判断 地址(id)是否不同
print(id(a))
print(id(b))
print(id(1))
print(id(c))
print(id(2))


c1 = complex(1,2) 
c2 = complex(1,2)
print(c1 is c2) # c1 c2指向的是不同的对象，故其id不同
print(c1 is not c2) # 
print(id(c1))
print(id(c2))

print(2 ** 3)   # 与下行相等
print(pow(2,3))

