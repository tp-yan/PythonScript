#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 13:40:52 2019

@author: tangpeng

collections是Python内建的一个集合模块，提供了许多有用的集合类。
"""

"""
1. namedtuple:（简化类定义）
namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，
并可以用属性而不是索引来引用tuple的某个元素。 
"""
p = (1,2) # 普通元组，看不出来是代表的一个(x,y)坐标
from collections import namedtuple

# 定义坐标点
Point = namedtuple("Point",['x','y']) #定义tuple的子类Point，并规定属性个数和名称。它具备tuple的不变性
p = Point(1,2)
print(p.x)
print(p.y)
print(isinstance(p,Point))
print(isinstance(p,tuple))

# 定义圆
Circle = namedtuple("Circle",['x','y','r'])


"""
2. deque:双向列表，本质还是list
deque 是为了高效实现插入和删除操作的双向列表，适合用于队列和栈.
因为list是线性存储，数据量大的时候，插入和删除效率很低。 
deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
"""
from collections import deque

dq = deque(['a','b','c'])
dq.append('x')
dq.appendleft('y')
print(dq)
print(dq.pop())
print(dq.popleft())

"""
3. defaultdict
使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
"""
from collections import defaultdict
dd = defaultdict(lambda:"N/A") # 默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
dd['key1'] = "abc"
print(dd['key1'])
print(dd['key2'])

"""
4. OrderedDict
使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
如果要保持Key放入的顺序（不是按key来排序的），可以用OrderedDict：
"""
from collections import OrderedDict
d = dict([('a', 1), ('c', 3), ('b', 2)]) # 原始dict
print(d)
od = OrderedDict([('a', 1), ('c', 3), ('b', 2)])
print(od) # OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
print(od.popitem()) # 默认 last=True 弹出最后添加进来的
print(od.popitem(last=False)) # 弹出最早添加进来的

# `OrderedDict`可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
class LastUpdatedOrderedDict(OrderedDict):
    
    def __init__(self,capacity):
        super().__init__()
        self._capacity = capacity
        
    def __setitem__(self,key,value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity: # 已满，弹出最早加入的元素
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey: # 原来的key存在，则覆盖，这里是先删除再添加最后
            del self[key] # 删除原来的key，调用父类方法再添加。可以不删除，调用父类直接覆盖value就行，key的位置不变
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        super().__setitem__(key,value)
        
            
luod = LastUpdatedOrderedDict(3)
luod['key1'] = 'a'
luod['key2'] = 'b'
luod['key3'] = 'c'
print(luod)
luod['key4'] = 'd'
print(luod)
luod['key3'] = 'e'
print(luod)


"""
5. ChainMap
ChainMap可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找。 
什么时候使用ChainMap最合适？举个例子：应用程序往往都需要传入参数，参数可以通过命令行传入，可以通过环境变量传入，还可以有默认参数。 
我们可以用ChainMap实现参数的优先级查找，即先查命令行参数，如果没有传入，再查环境变量，如果没有，就使用默认参数。 
下面的代码演示了如何查找user和color这两个参数：
"""
from collections import ChainMap
import os,argparse

# 构造缺省参数:
defaults = {'color':'red',
            'user':'guest'}
# 构造命令行参数:
parser = argparse.ArgumentParser()
parser.add_argument('-u','--user')
parser.add_argument('-c','--color')
namespace = parser.parse_args()
command_line_args = {k:v for k,v in vars(namespace).items() if v} # 过滤掉空值参数
# 组合成ChainMap:
combined = ChainMap(command_line_args,os.environ,defaults) #实际是一个有序的Dict
# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])



"""
6. Counter:计数器，dict的子类。
"""
from collections import Counter
c = Counter()
for ch in "programming":
    c[ch] = c[ch] + 1
    
print(c)

