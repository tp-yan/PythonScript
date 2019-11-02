#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 14:46:42 2019

@author: tangpeng

类和实例属性
"""

# 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
class Student(object):
    count = 0
    name = 'Student' # 类属性

    def __init__(self, name):
        self.name = name # 给实例绑定属性
        Student.count += 1
   

s = Student("xixi") # 创建实例s
print(s.name)
print(Student.name)
s.name = 'Michael' # 给实例绑定name属性
print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
del s.name # 如果删除实例的name属性
print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
Student.name = "senior student"
print(s.name)
print(Student.name)

# 给实例绑定方法：
def set_age(self,age):
    self.age = age
    self.__sex = '男'
    
from types import MethodType
s.set_age = MethodType(set_age,s)
s.set_age(23)
print(s.age)
print(s.__sex)

s2 = Student("jordan")

# 给一个实例绑定的方法，对另一个实例是不起作用的。为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self, score):
    self.score = score

Student.set_score = set_score
s.set_score(100)
print(s.score)
# print(s2.score) # AttributeError: 'Student' object has no attribute 'score'
s2.set_score(111)
print(s2.score)

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')