#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#type(xxx):判断对象类型，返回对应的Class类型
print(type(123))
print(type("szxc"))
print(type(None))
print(type(abs))
#使用type判断一个对象是否函数，借助 types模块中的常量
import types

def fn():
	pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x:x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# isinstance(obj,class):对象是否为某种类型，能使用 type()判断的基本类型也可以使用isinstance
print(isinstance('a',str))
print(isinstance(12,int))
print(isinstance(b'a',bytes))
print(isinstance([1,2,3],(list,tuple)))	#判断一个变量是否为其中的一种类型

print(dir('ABC'))	#dir():返回一个对象所用属性与方法

class MyObject(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x

obj = MyObject()
print(hasattr(obj,'x'))	#对象是否含有该属性
print(obj.x)
print(hasattr(obj,'y'))	
setattr(obj,'y',19)		#设置一个对象属性
print(getattr(obj,'y'))	#获取属性
print(obj.y)
print(getattr(obj,'z',404))	#获取不存在的属性，返回默认值404
print(hasattr(obj,'power'))	
fn = getattr(obj,'power')	#fn指向obj.power()
print(fn())		#输出 81

print("=========================") 
#使用getattr、setattr、hasattr判断、设置、获取对象属性与方法
class MyObj(object):
	def __init__(self,name,age=18):
		self.name = name
		self.__age = age
	
	def get_name(self):
		return self.name
		
	def get_age(self):
		return self.__age
		
stu = MyObj('张三')
print(hasattr(stu,'get_name'))
print(hasattr(stu,'age'))
print(hasattr(stu,'__age'))
print(hasattr(stu,'_MyObj__age'))

fn = getattr(stu,'get_name')
print(fn())
