# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 09:04:59 2019

@author: cv
"""

"""
装饰器-decorator
"""

def now():
    print('2015-3-25')
 
f = now # 函数名只是指向函数对象的一个变量
f()

now.__name__ # 函数对象名
f.__name__


# 1. 基本装饰器
def log(func):
    def wrapper(*args,**kw):
        print("call %s():" % func.__name__)
        return func(*args,**kw)
    return wrapper

# 使用装饰器
@log
def now():
    print('2015-3-26')
    
now() # 变量 now 指向了 返回的新函数 wrapper
f() # 原函数对象依然存在
print(now.__name__)
print(f.__name__)


# 2.带参装饰器
# 需要编写一个**返回decorator的高阶函数**
def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print("%s %s():" %(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')

# now = log('execute')(now)
    
now()


# 3. 复制函数对象属性__name__
import functools
def log(func):
    @ functools.wraps(func) # 将func的函数名复制到wrapper的__name__
    def wrapper(*args,**kw):
        print("call %s():" % func.__name__)
        return func(*args,**kw)
    return wrapper


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print("%s %s():" %(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator


# 练习:请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        startTime = time.time() # 1970纪元后经过的浮点秒数
        result = fn(*args,**kw)
        endTime = time.time()
        print('%s executed in %s s' % (fn.__name__, endTime-startTime))
        return result
    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012) # 参数secs指秒数，表示进程挂起的时间
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
    
# 在函数调用的前后打印出'begin call'和'end call'的日志
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print("begin call %s()" % func.__name__)
        result = func(*args,**kw)
        print("end call %s()" % func.__name__)
        return result
    return wrapper

@log
def myAdd(a,b):
    return a+b
print(myAdd(1,9))


"""
写出一个@log的decorator，使它既支持：
@log
def f():
    pass
    
又支持：
@log('execute')
def f():
    pass
"""
def log(param=None):
    if callable(param): # 根据传入的参数判断是调用无参还是有参的装饰器，若传入的是函数则返回wrapper，否则返回decorator
        @functools.wraps(param)
        def wrapper(*args,**kw):
            print("call %s()" % param.__name__)
            return param(*args,**kw)
        return wrapper
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kw):
                print("%s --> %s()" % (param,func.__name__))
                return func(*args,**kw)
            return wrapper
        return decorator

@log('my sum')
def add_2(a,b):
    return a*10+b
print(add_2.__name__)
print(add_2(1,2))


@log
def add_1(a,b):
    return a + b
print(add_1.__name__)
print(add_1(1,2))
