#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:49:06 2019

@author: cv
"""

class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
        self._sex = 'male'

    def add_attr(self):
        self.__age = 12
        
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
        
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
        
        
bart = Student('Bart Simpson', 59)
bart.get_name()

# 因为还没有执行 add_attr() 故 bart 还没有属性 __age
# bart.get_age() # AttributeError: 'Student' object has no attribute '_Student__age'

bart.add_attr() # 添加属性  __age
# 说明在方法中给实例绑定的 private属性 也会被换名
# bart.__age # AttributeError: 'Student' object has no attribute '__age'.

bart.__age = 100 # 从外部添加的属性即使以 '__' 开头也不会当作 private属性
print(bart.__age) 
print(bart.get_age())

print(bart._sex) # 以一个下划线开头的属性是可以从外部访问的，但是其表明不应该从外部直接访问
