# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 17:19:03 2019

变量作用域
@author: tangpeng
"""

#==========1============
# 全局作用域
x = 1
scope = vars()  # 内建函数vars()以'变量名-值'的形式返回全局变量的字典
# scope这类字典就叫做命名空间或作用域
print(scope['x'])
scope['x'] += 1
print(x)
#print(scope)   # 所有全局变量


#==========2============
# 每个函数调用都会创建一个新的作用域
def foo():  # 函数参数也是函数内部的局部变量
    x = 42  # 只影响函数内部作用域的变量，全局变量不影响
    print(locals()) # locals():返回（当前作用域）局部变量的字典
print(x)
foo()


#==========3============
# 函数内部访问同名的全局变量
# globals()与vars()一样返回全局变量的字典
print(globals() == vars())
print(locals() == globals())   # 在全局域下调用locals效果与globals()一样

def combine(param):
    # param：局部变量
    print(param+globals()['param'])

param = "berry" # 全局变量
combine("Shrub")


#==========4============
# 重绑定全局变量：使变量引用其他新值
# 在函数内部给一个变量赋值，它将自动成为局部变量!!除非告知python声明其为全局变量
# 注：尽量不要使用全局变量
x = 1
def change_global():
    global x    # 在函数内部声明此变量是全局变量
    x = x+1

change_global()
print(x)