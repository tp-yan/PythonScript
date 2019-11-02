# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:08:30 2019

yield关键字:使函数变为生成器generator
@author: tangpeng
"""

# yield关键字将函数执行的中间结果返回但不结束程序
# yield将函数变为一个生成器generator，而不再是一个(普通)函数

# 使用yield模仿range() 函数
def func_range(n):
    i = 0
    while i < n:
        yield i
        i += 1
    
# 生成器用于迭代，直到报错，for循环会处理异常
for i in func_range(5):
    print(i)

# yield实现Fibonacci数列，不保存中间结果，只记录某个位置上的值一次
def fib(n):
    '''返回Fibonacci数列的前n个值'''
    i, a, b = 0,0,1 # a作用中间变量保存b的前一个数，b才是Fibonacci数列中的元素
    while i < n:
        yield b
        a ,b = b, a+b # 以‘,’隔开的多个变量，其实被组织成元组，实际上是 (a,b) = (b,a+b)
        i += 1

# 执行fib(10)不会执行fib函数，而是返回一个可迭代(Iterable)对象
# 每次循环都会执行fib函数内部的代码，执行到yield时，fib返回一个值，下次迭代就从上次yield的后续
# 代码继续执行，直到下一次遇到yield。相当于不断循环执行fib函数的函数体
for i in fib(10):
    print(i)