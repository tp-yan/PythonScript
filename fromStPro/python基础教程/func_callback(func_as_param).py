# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:33:40 2019

回调函数：一个函数作为另一个函数的参数，如将B函数作为A函数的参数传入，A函数内部再执行B函数。
好处：在函数定义之前就可以使用函数
@author: tangpeng
"""

def func(fun,*args,**kwds):
    fun(*args,**kwds)

def f1(x):
    print("f1 function")
    print("x:",x)

def f2(x,y):
    print("f2 function")
    print("x,y:",x,y)
    
func(f1,12)
func(f2,45,67)
