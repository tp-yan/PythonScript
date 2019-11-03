# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 09:16:04 2019
 关键字与默认参数
@author: tangpeng
"""

def hello(greeting='Hello',name="world"):
    '''关键字参数：优点1：不用关心参数在哪个位置
        2：参数有默认值，可以选择性传入参数
    '''
    print("%s, %s !\n" % (greeting,name))   

hello()
hello(greeting="hi")
hello(name='China')
hello(name='China',greeting="hei")  # 不用在意参数位置

def hello_2(name,greeting="Hello",punctuation=","):
    '''位置和关键字参数混合使用：位置参数在前且调用时必须传入实参'''
    print("%s, %s%s" %(greeting,name,punctuation))
    
hello_2("zhangsan")
hello_2("zhangsan",punctuation="&")
hello_2("zhangsan",punctuation="&",greeting="wa")

