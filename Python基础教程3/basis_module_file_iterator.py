# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 10:57:20 2019

标准库之file：文件迭代器，文件对象(流对象)也是可迭代对象
@author: 10841
"""

f = open("sometxt.txt","w")
print("First","line",file=f) # 将print输出内容写入文件中，且自动添加换行符
print("Second","line",file=f) # 将print输出内容写入文件中，且自动添加换行符
print("Third","line",file=f) # 将print输出内容写入文件中，且自动添加换行符
f.close()

# 以下代码说明 文件对象是可迭代对象
lines = list(open("sometxt.txt"))
print(lines)
first, second, third = open("sometxt.txt")
print(first,second,third)