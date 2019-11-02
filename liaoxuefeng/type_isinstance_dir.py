#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 14:16:21 2019

@author: tangpeng

获取对象信息
"""
class Animal:
    pass
a = Animal()

# type()：判断对象类型，回对应的Class类型。 
type(123)
type("ABC")
type(None)
type([1,2,3])
# 变量指向函数或者类
type(abs)
type(a)

type(123)==int
type('abc')==str

# 判断一个对象是否是函数
import types
def fn():
    pass

type(fn)==types.FunctionType
type(abs) == types.BuiltinFunctionType
type(lambda x:x) == types.LambdaType
type((x for x in range(10))) == types.GeneratorType


# isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。
isinstance(a, Animal)
isinstance('a', str)
isinstance(123, int)
isinstance(b'a',bytes)
#判断一个变量是否是某些类型中的一种
isinstance([1, 2, 3], (list, tuple))
isinstance((1, 2, 3), (list, tuple))


# dir():获得一个对象的所有属性和方法
dir('ABC')
len('ABC') == 'ABC'.__len__()
class myLenObj:
    def __init__(self):
        self.x = 9
    
    def power(self):
        return self.x * self.x
        
    def __len__(self):
        return 100

obj =   myLenObj()
print(len(obj))

# 测试该对象的属性
hasattr(obj, 'x') # 有属性'x'吗？
setattr(obj, 'y', 19) # 设置一个属性'y'
setattr(obj, '__pri', 19) # 设置一个属性，虽然是 __ 开头但是不是private属性
getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
# 也可以获得对象的方法：
hasattr(obj, 'power') # 有属性'power'吗？
print(getattr(obj, 'power')) # 获取属性'power'
fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
fn()

