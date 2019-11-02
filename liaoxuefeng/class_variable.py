# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 13:40:31 2019

@author: cv
"""

"""
类变量
"""

class C:
    print("Class C being defined!")
    counter = 0 # 类变量，**只能通过类来改变，实例只能读取而无法改变**
    def init(self):
        C.counter += 1
        
        
c1 = C()
c1.init()
c2 = C()
c2.init()

print(c1.counter)
print(c2.counter)
print(C.counter)

c1.counter = "hi"
print(c1.counter) # hi
print(c2.counter) # 2
print(C.counter) # 2

C.counter = "hello"
print(c1.counter) # hi
print(c2.counter) # hello
print(C.counter) # hello
