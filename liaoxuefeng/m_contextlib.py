#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 17:10:30 2019

@author: tangpeng

contextlib模块：封装了一些decorator，可用于快速实现上下文管理器
"""

# 正确关闭文件资源的一个方法是使用try...finally：
path = r'C:\Users\tangpeng\Desktop\test.txt'
try:
    f = open(path,"r")
    f.read()
finally:
    if f:
        f.close()
        
# 写try...finally非常繁琐。Python的with语句允许我们非常方便地使用资源，而不必担心资源没有关闭:
with open(path,"r") as f:
    f.read()
    
"""
1. 实现上下文管理
任何对象，只要正确实现了上下文管理，就可以用于with语句。
实现上下文管理是通过__enter__和__exit__这两个方法实现的：
"""
class Query(object):
    def __init__(self,name):
        self.name = name
        
    def __enter__(self):
        print("begin")
        return self
    
    def __exit__(self,exc_type, exc_value, traceback):
        # 一般在这里进行资源关闭
        if exc_type:
            print("Error")
        else:
            print("End")
    
    def query(self):
        print('Query info about %s...' % self.name)
        
with Query("Bob") as q:
    q.query()
    
"""
2. @contextmanager
编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法，上面的代码可以改写如下：
"""
from contextlib import contextmanager

class Query:
    def __init__(self,name):
        self.name = name
    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager # 使得不用修改原来代码的类定义，而使得类实例可以用于with语句
def create_query(name):
    print("Begin")
    q = Query(name)
    yield q
    print("End")
    
# @contextmanager这个decorator接受一个generator，用yield语句把with ... as var要操作的变量抛出，
# 然后，with语句就可以正常地工作了：
with create_query('Bob') as q:
    q.query()
    
# 很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现。例如：
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield 
    print("</%s>" % name)

with tag("h1"): # 先执行生成器tag yield 之间的代码，在执行 with中的代码段，最后回来执行yield之后的代码
    print("hello")
    print("world")


"""
3. @closing
如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。

closing也是一个经过@contextmanager装饰的generator，这个generator编写起来其实非常简单：
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()  # thing对象必须有close方法
        
它的作用就是把任意对象变为上下文对象，并支持with语句。

例如，用with语句使用urlopen()：
"""
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
