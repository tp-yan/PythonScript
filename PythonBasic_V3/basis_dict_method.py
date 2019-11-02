# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 23:27:43 2019

字典之字典方法
@author: 10841
"""

# 1.clear：清空字典对象/变量 指向的区域,不返回值
d = {}
d['name'] = 'Gumby'
d.clear()
print(d)

x = {}
y = x
x['key'] = 'value'
print(y)
x = {}
print(y)

x = {}
y = x   # x,y都只是指向同一内存空间的变量
x['key'] = 'value'
x.clear()
print(y)

# 2.copy:浅拷贝,当替换副本中的值时，原件不受影响，修改时对原件有影响，说明只复制了引用，而没有开辟新的内存空间
x = {'username':'admin','machines':['foo','bar','baz']}
y = x.copy()
y['username'] = 'lmk'
y['machines'] = []  # 相当于y中的 'machines'指向了新的内存区域
#y['machines'].remove('bar')
print(x)
print(y)

# 深拷贝：模块copy中的 deepcopy函数
from copy import deepcopy
d = {}
d['name'] = ['Alice','Bell']
c = d.copy()
dc = deepcopy(d)    # 深拷贝：开辟了新内存
d['name'].append('Curry')
print(d)
print(c)
print(dc)

# 3.fromkeys:创建只含key，值为None的字典
print({}.fromkeys(['name','age']))  # 调用空字典的方法
print(type(dict))
print(dict.fromkeys(['name','age'])) # fromkeys应该是dict的类方法
print(dict.fromkeys(['name','age'],['unknown','zxc'])) # 指定所有key的默认value

 # 4.get:返回key的value
print(d.get('name'))
print(d.get('age',23))  # 不存在时，返回指定值

# 5.items:返回包含字典所有项的list
d = {'title':'Python web site','uri':'http://www.python.org','spam':0}
it = d.items()
print(d.items())    
print(type(d.items()))    # 返回一个叫字典视图的类，可迭代
print(len(d.items()))
print(('title','python') in d.items())

# 字典视图始终是底层字典的反映，即是实时的
print(('spam',0) in it)
d['spam'] += 1
print(('spam',1) in it)
print(('spam',0) in it)
print(it)

# 6.keys:返回key组成的字典视图
print(d.keys())
# 7.pop：删除(key,value),并返回value‘
print(d.pop('spam'))
print(d)

# 8.popitem:随机删除一个项，返回删除项，可用于逐个删除并处理字典项
print(d.popitem())
print(d.popitem())

# 9.setdefault:与get类似，但若key不存在则添加该项
print(d.setdefault('name','N/A'))
d['name'] = 'Tom'
print(d.setdefault('name','N/A'))

# 10.update:使用一个字典的项去更新另一个字典，若key不存在则添加该项，存在则更新
d = {'title':'Python web site','uri':'http://www.python.org','spam':0}
x = {'spam':10,'title':'scrapy','name':'Tom'}
d.update(x)
print(d)
# update与dict函数的参数是一样的，可以是：一个映射，关键字参数，key-value组成的序列

# 11.values:由value组成的字典视图
vdi = d.values()
print(vdi)
d['age'] = 33
print(vdi)
