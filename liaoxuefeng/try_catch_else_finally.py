#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 23:23:51 2019

@author: tangpeng

错误处理：try-catch-else-finally
"""

"""
try-catch-finally
"""
try:
    print('try...')
    r = 10 / int('a')
    print('result:',r)
    print("异常发生代码后面的部分不会再执行")
except ValueError as e:
    print("ValueError:",e)
except ZeroDivisionError as e:
    print("ZeroDivisionError:",e)
else:
    print("若没有异常发生，则执行else代码块")
finally:
    print("finally 一定会执行，可选")
    
# Python所有的错误都是从BaseException类派生的,注意捕获异常时异常类的继承关系


"""
记录错误
Python内置的logging模块可以非常容易地记录错误信息：
"""
import logging
def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e) # 通过配置，logging还可以把错误记录到日志文件里
        
main()
print('End')

"""
抛出错误
因为错误是class，捕获一个错误就是捕获到该class的一个实例。我们自己编写的函数也可以抛出错误。
如果要抛出错误，首先根据需要，可以定义一个错误的class，然后，用raise语句抛出一个错误的实例：
"""
class FooError(ValueError):
    pass

def foo(s):
    n  = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
        return 10/n
foo('0') # FooError: invalid value: 0

"""
 另一种错误处理的方式：再次抛出错误
"""
def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError')
        raise # raise语句如果不带参数，就会把当前错误原样抛出
        
bar()

# 此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：
try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')
    

"""
练习
运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复：
"""
from functools import reduce

def str2num(s):
    return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()

