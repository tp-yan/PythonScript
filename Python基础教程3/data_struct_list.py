# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:23:03 2019

数据结构之列表：list
list可作为栈和队列来使用
@author: tangpeng
"""

s = [1,2,3,1,5,7,11,22,4,5,6,9,2,3,101]

print(s)
s.extend([88,99,3])   # 末尾拼接另一个list
print(s)

print(s.count(3))   # 统计某个元素个数

s.reverse() # 反序
print(s)

s.sort()    # 默认升序，直接操作list，不会返回副本
print(s)
s.sort(reverse=True)    # 降序
print(s)

print(s.copy()) # 返回副本，等价于 s[:]
print(s[:])
print(s[:-2])
s.clear()   # 清空

# 元组tuple与list基本一样
# 以‘,’隔开的多个变量，其实被组织成元组
a,b = 1,2   # 实际上是 (a,b) = (1,2)
a,b = b,a   # 实际上是 (a,b) = (b,a)

print(zip([1,2],[3,4]))
print(dict(zip([1,2],[3,4])))
print(type(zip([1,2],[3,4])))

