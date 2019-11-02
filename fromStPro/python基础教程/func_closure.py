# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 17:44:34 2019
函数式编程之闭包与嵌套作用域
闭包：将函数作为返回值返回。可以延长变量的作用时间与作用域！
@author: tangpeng
"""

def foo():
    def bar():
        print("hello from Bar!")
    bar()

foo()

# 函数嵌套
# 一般函数嵌套用处不大，但有一个突出应用：调用一个函数取创建另一个(返回)函数
def multiplier(factor):
    def multiplyByFactor(number):
        return number*factor
    return multiplyByFactor     # 返回内部函数，但未调用。但返回的函数可访问它的定义所在的作用域，即它“带着”它的环境(和相关的局部变量)

double = multiplier(2)
print(double(5))
triple = multiplier(3)  # 每次调用外部函数，内部函数都重新绑定，且每次返回的内部函数互不影响
print(triple(3))
print(double(2)) # 返回的函数，依然保持当时返回时的“环境”和那时相关的局部变量
print(multiplier(5)(4))
four = multiplier(2)
print(four(5))

# 类似multiplyByFactor函数，存储子封闭作用域的行为叫做闭包(closure)

# 函数式编程的一个例子：函数式编程，基本被面向对象编程代替
def func():
    res = []
    
    def put(x):
        res.append(x)
        
    def get():
        return res
    return put,get

p,g = func()
p(1)
p(2)
print("res:",g())
p(3)
p(4)
print("res:",g())


