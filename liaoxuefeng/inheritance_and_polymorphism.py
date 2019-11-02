#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 16:42:04 2019

@author: cv

继承与多态
"""


class Animal(object):
    def run(self):
        print('Animal is running...')
        

class Dog(Animal):
    # 继承父类所有方法
    # 覆盖父类方法
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')
        
class Cat(Animal):

    def run(self):
        print('Cat is running...')
        
        
a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型

isinstance(a, list)
isinstance(b, Animal)
isinstance(c, Dog)


# 多态的运用
def run_twice(animal):
    animal.run()
    animal.run()
    
run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

# 新定义一个Tortoise类，也从Animal派生：
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')
        
run_twice(Tortoise())

"""
多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。
这就是著名的“开闭”原则：
对扩展开放：允许新增Animal子类；
对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。

注：编译时看左边声明的类型（编译类型），调用时看右边的实际类型（运行类型）
"""

"""
因为Python是动态语言，调用函数run_twice(animal)，不一定需要传入Animal类型。
只需要保证传入的对象有一个run()方法就可以了：
"""
class Timer(object):
    def run(self):
        print('Start...')
        
run_twice(Timer()) # 不要求传入Animal类型，只要该对象有 run() 即可。因为Python没有强制要求传入的参数类型


        