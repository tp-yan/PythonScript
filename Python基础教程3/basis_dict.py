# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 17:20:00 2019

字典:以key-value作为元素，也称项Item
key：任何不可变对象，整数、浮点数、字符串、元组
@author: 10841
"""

# 1.创建dict
d = {'Alice':'12345','bob':'00000'}
print(d)
# 使用构造函数dict：传入映射或key-value序列对
items = [('name','Gumby'),('age',42)]
d = dict(items)
print(d)
# 也可使用关键参数创建
d = dict(name='Klai',age=28)
print(d)
d = dict({'Alice':'99999','bob':'00000'}) # 从其他映射如dict创建
print(d)

# 字典常用操作
print(len(d))   # item的个数
d['Tom'] = '777777' # 添加项item, 列表必须使用append等方法添加元素，而不能直接通过索引添加
print(d)
d['Tom'] = '444444' # 更新value
print(d)
del d['Tom'] # 删除item
print(d)
print('Curry' in d) # 检查key是否为d的某个项中
print('Alice' in d)
d[43] = 'Foobar'
print(d)

# 将dict用于 字符串格式输出format_map：必须要保证{}中的命名参数是dict中的key
phonebook = {'Bech':'9102','Curry':'1024','Klai':'2048'}
print("Curry's phone number is {Curry}".format_map(phonebook))

# 小示例：HTML模板
template = '''
<html>
 <head><title>{title}</title></head>
 <body>
     <h1>{title}</h1>
     <p>{text}</p>
 </body>
</html>
'''
data = {'title':'My home page','text':'Welcome to my home page!'}
print(template.format_map(data))
