#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#测试：参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def fun(name,age,city='Chengdu',sex='male', * ,school,**kw):
	print("name:",name,", age:",age,", from:",city,", sex: ",sex)
	for arg in args:
		print(arg,"\t")
	print("grade:",grade,", school:",school)
	for key,value in kw:
		print(key,":",value,"\t")

#可变参数
number = ['basketball',100,123.45]
extra = {'job':'software engineer','salary':12223}

fun('tp',22,*number,grade='senior',school='CAS',**extra)
