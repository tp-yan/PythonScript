#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 09:29:44 2019

@author: tangpeng

@property装饰器负责把一个方法变成属性调用：访问属性时实质调用其getter()，而赋值属性时实质调用
setter()，这样才访问属性时就可以进行额外的操作
"""

class Student:
    def __init__(self):
        self.__score = 99
        self.__age = 22
    
    @property # 把一个getter方法变成属性,此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
    def score(self):
        return self.__score
    
    @score.setter
    def score(self,value):
        # 对 value 类型和值范围进行检查
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.__score = value
        
    # 只读属性，只定义`getter`方法，不定义`setter`方法
    @property
    def age(self):
        return self.__age
    

s = Student()
print(s.score)
s.score = 80
#s.score = 999 # ValueError: score must between 0 ~ 100!

print(s.age)
#s.age = 27 # AttributeError: can't set attribute


"""
练习
请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
"""
class Screen(object):
    def __init__(self):
        self.__height = 0
        self.__width = 0
        
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self,value):
        if value >= 0:
            self.__width = value
        else:
            raise ValueError('width must be positive')

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,value):
        if value >=0:
            self.__height = value
        else:
            raise ValueError('height must be positive')
            
    # 定义不存在的属性
    @property
    def resolution(self):
        return self.__height * self.__width
    
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

