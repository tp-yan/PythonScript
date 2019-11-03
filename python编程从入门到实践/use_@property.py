#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Python内置的@property装饰器就是负责把一个方法变成属性调用的，用于修饰类中的方法
#@property：像访问属性一样，调用属性的setter、getter方法，主要用于数据类型检测，或者其他操作
#使用@property（装饰器）来将访问实例属性的操作简单高效化

class Student(object):

	@property 	# 把一个getter方法变成了属性，同时@property又创建了另一个装饰器 @score.setter
	def score(self):
		return self._score
	@score.setter	#将一个setter方法变成属性赋值
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer')
		if value < 0 or value > 100:
			raise ValueError('score must between 0~100')
		self._score = value

	@property
	def birth(self):
		return self._birth
	@birth.setter
	def birth(self,value):
		self._birth = value

	@property
	def age(self):	#只使用@property，不定义@age.setter 即age的setter方法，那么age就是一个只读属性
		return 2018 - self._birth
	


#========================================练习======================================

#请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen(object):
	@property
	def width(self):
		return self._width
	
	@width.setter
	def width(self,value):
		if not isinstance(value,int):
			raise ValueError('width must be a integer!')
		elif value < 0:
			raise ValueError('width must > 0')
		self._width = value

	@property
	def height(self):
		return self._height
	
	@height.setter
	def height(self,value):
		if not isinstance(value,int):
			raise ValueError('height must be a integer!')
		elif value < 0:
			raise ValueError('height must > 0')
		self._height = value
	
	@property
	def resolution(self):
		return self._height*self._width
	
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
