#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#动态给实例与class添加属性或方法，以及使用__slots__限制实例属性

class Student(object):
	__slots__ = ('name','age','set_age','score') #实例最多只能有这个两个属性
	
	def get_name(self):
		return self.name
	
s1 = Student()
s1.name = "张三"	#动态添加属性
s1.age = 18
#s1.score = 99 #报错，无法添加限制外的属性

def set_age(self,age):
	self.age = age

from types import MethodType
s1.set_age = MethodType(set_age,s1) #此处相当于添加属性，所以‘set_age’这个属性必须包含在__slots__中，不然也报错
s1.set_age(22)
print(s1.age)
print(s1.get_name())


def set_score(self,score):
	self.score = score

Student.set_score = set_score	 #class动态添加方法，适用于所有实例，在该方法中所涉及到的属性也必须在__slots__中
s1.set_score(100)

s2 = Student()
s2.set_score(88)
s2.set_age(56) #报错
