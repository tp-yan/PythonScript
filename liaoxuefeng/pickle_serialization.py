#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:17:57 2019

@author: tangpeng

序列化: pickling == serialization == flattening
"""

"""
每种编程语言都有自己特有的序列化方法，python中是 pickle ，只能用于python。
通用的序列化方法是将对象序列化为JSON或XML等标准格式.
JSON对象表示出来就是一个字符串，可以被所有语言读取。
"""
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        
"""
1. python特有的pickle
pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件.
或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object.
要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，
也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
"""
import pickle
import os

d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))

f = open("dump.txt","wb")
pickle.dump(d,f)
f.close()

f = open("dump.txt","rb")
d = pickle.load(f)
f.close()
print(d)


s = Student('Bob', 20, 88)
print(s)
f = open("dump_student.txt","wb")
pickle.dump(s,f)
f.close()

f = open("dump_student.txt","rb")
s1 = pickle.load(f)
f.close()
print(s1) # 这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已

""" 2. JSON
要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式
dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
"""
import json

d = dict(name='Bob', age=20, score=88)
json_str = json.dumps(d) # JSON字符串
print(json_str)
with open("dump_json.txt","w") as f:
    json.dump(d,f)
with open("dump_json.txt","r") as f:
    d_tmp = json.load(f)
    print(d_tmp,"-->",type(d_tmp))

"""
3. JSON进阶
Python的dict对象可以直接序列化为JSON的{}，而一般对象不可以直接序列化为JSON
print(json.dumps(s)) # TypeError: Object of type Student is not JSON serializable
默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象.
可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可.
要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例
"""
def student2dict(std):
    return {
            'name':std.name,
            'age':std.age,
            'score':std.score
            }
    
# Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON：
print(json.dumps(s,default=student2dict))
# 通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。
print(json.dumps(s,default=lambda obj:obj.__dict__))

def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

json_str = '{"name": "Bob", "age": 20, "score": 88}'
s2 = json.loads(json_str,object_hook=dict2student)
print(s2,"-->",type(s2))


# print(r"\u%04x" % ord('中')) # 打印一个字符的Unicode编码
"""
练习
对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响：
"""
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True) # 用ascii显示字符串，不能为ascii码表示的用 16进制的 Unicode码指示
print(s)
print(json.dumps(obj, ensure_ascii=False))

