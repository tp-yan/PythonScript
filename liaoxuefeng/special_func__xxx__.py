#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 11:24:09 2019

@author: tangpeng


使用Python的特殊函数`__xxx__()`定制类
"""

# __str__()：print输出对象 与 __repr__()：IPython打印对象
class Student:
    def __init__(self,name):
        self.name = name
    
    #print(obj)时，调用 __str__
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    # 交互控制台直接输出对象时，调用 __repr__()是为调试服务的
    __repr__ = __str__

s = Student('Michael')

print(s)
s

"""
 __iter__() + __next__()
 __iter__()：类实例被用于for ... in循环
 __iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的
 __next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环
"""
# 斐波那契数列
class Fib:
    def __init__(self):
        self.a, self.b = 0,1
        
    def __iter__(self):
        return self     # 实例本身就是迭代对象，故返回自己
    
    def __next__(self):
        self.a, self.b = self.b, self.a+  self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a
    
for n in Fib():
    print(n)
    
"""
__getitem__
Fib实例虽然能作用于for循环，但是还不能像list那样取第几个元素，要表现得像list那样按照下标取出元素，
需要实现__getitem__()方法，同时实现list的切片操作
"""
class Fib:
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b=1,1
            for x in range(n):
                a,b=b,a+b
                return a
        
            
