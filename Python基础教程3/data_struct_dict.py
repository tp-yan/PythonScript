# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 21:10:29 2019
数据结构之列表：字典dict
字典：保存key-value值对，元素(key,value)值对，是无序存放的。
key要求是不可变的，故tuple可作为key
@author: tangpeng
"""


# 创建一个字典
d = {1:10,2:20,"a":12,5:"hello"}    # 数字依旧是数字作为key
print(d)

d1 = dict(a=1,b=2,c=3)  # 字符都转为字符串作为key
print(d1)

# 将元素是二元列表(只含2个元素的列表)的列表转换为字典，列表也可以换成元组
d2 = dict([['a',12],[15,'a4'],['hrl','rt']])
d3 = dict([('a',12),(15,'a4'),('hrl','rt')])
print(d2)
print(d3)

# 获取元素
print(d[1])
print(d['a'])
print(d.get(5))

# 对字典的部分操作
dc = d.copy()
print(dc)
dc.clear()  # 清除字典
print(dc)

print(d.items())    # 返回字典的项列表
print(d.keys())
print(d.values())
d.pop(1)    # 弹出 key=1的项
print(d)