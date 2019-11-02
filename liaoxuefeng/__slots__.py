#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 08:40:47 2019

@author: tangpeng


在定义class的时候，定义一个特殊的`__slots__`变量，来限制该class实例能添加的属性
"""

class Student:
    __slots__ = ('name','age') # 用tuple定义允许绑定的属性名称
    
s = Student() # 创建新的实例
s.name = 'tom'
s.age = 25
#s.score = 100
     

# `__slots__`定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 99

# 除非在子类中也定义`__slots__`，这样，子类实例允许定义的属性就是自身的`__slots__`加上父类的`__slots__`
class SeniorStudent(Student):
    __slots__ = ('sex')
    
st = SeniorStudent()
st.name = 'zhang'
st.age = 22
st.sex = 'male'
st.score = 88 # AttributeError: 'SeniorStudent' object has no attribute 'score'