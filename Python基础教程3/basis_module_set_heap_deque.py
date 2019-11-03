# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 12:40:38 2019

标准库之集合、堆、双端队列
@author: 10841
"""

# 1.集合：用于去除重复元素，成员资格检查，只能包含不可变的元素
print(set(range(10))) # 用可迭代对象创建集合
print({1,2,3,4,5,1}) # 自动去除重复元素
print(type(set())) # 空集合
# 集合的操作
a = {1,2,3}
b = {2,3,4}
# 1.1 并
print(a.union(b))
print(a | b)
# 1.2 交
print(a & b)
print(a.intersection(b))
c = a & b
# 1.3 父子集
print(c.issubset(a))
print(b.issuperset(c))
# 1.4 差
print(a.difference(b))
print(a-b)
# 1.5 对称差：返回两个集合中不重复的元素集合
print(a.symmetric_difference(b))
print(a ^ b)
# 1.6 副本
print(a.copy is a)
a.add(10)
a.remove(2)
print(a)

# 1.7 frozenset：表示不可变的集合，用于集合的嵌套
a.add(frozenset(b))
print(a)

# 2.堆：优先队列，默认小顶堆。堆对象必须使用列表表示，没有专门的堆数据结构
from heapq import * # 该模块只有几个操作堆的函数，这些函数必须用在已是堆的列表上
from random import shuffle

data = list(range(10))
shuffle(data)
print(data)
heap = []
for n in data:
    heappush(heap,n) # 
print(heap)
heappush(heap,0.5)
print(heap)

print(heappop(heap)) # 弹出堆顶(最小)元素，即第一个元素
print(heappop(heap))
print(heappop(heap))

heap2 = list(range(10))
shuffle(heap2)
heapify(heap2) # 以最少的移动操作 将列表变为堆结构
print(heap2)
heapreplace(heap2,0.5)
print(heap2)

# 3.双端队列
from collections import deque

q = deque(range(5))
print(q)
q.append(5)
q.appendleft(6)
print(q)
q.pop()
q.popleft()
print(q)
q.rotate(3) # 向右循环移位3个元素
print(q)
q.rotate(-1) # 向多循环移位
print(q)




