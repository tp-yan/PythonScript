#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 10:20:30 2019

@author: tangpeng

操作文件和目录
"""

import os

print(os.name)
#print(os.uname()) # windows上没有此函数

print(os.environ) # 系统环境变量
print("============================")
print(os.environ.get("PATH"))
print(os.environ.get("X","default"))


# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中
print(os.path.abspath("."))  # 查看当前目录的绝对路径
newDirPath = os.path.join(".","testDir") # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
if os.path.exists(newDirPath):
    os.rmdir(newDirPath) # 删除目录
os.mkdir(newDirPath)

print(newDirPath) # 打印相对路径
print(os.path.abspath(newDirPath)) # 绝对路径

# split：把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
print(os.path.split("/Users/michael/testdir/file.txt")) # ('/Users/michael/testdir', 'file.txt')
print(os.path.split("/Users/michael/testdir/")) # ('/Users/michael/testdir', '')
print(os.path.split("/Users/michael/testdir")) # ('/Users/michael', 'testdir')
# 注：/Users/michael/testdir/ 代表testdir文件夹下的一个空目录，/Users/michael/testdir"才代表testdir目录的路径

# os.path.splitext()可以直接让你得到路径文件扩展名
print(os.path.splitext("/Users/michael/testdir/file.txt")) # ('/Users/michael/testdir/file', '.txt')
print(os.path.splitext("file.txt")) # ('file', '.txt')

# 注：这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作
try:
    # 对文件重命名:
    os.rename("test.txt","test.py")
    # 删掉文件:
    os.remove("tmp2.py")
except Exception as e:
    print(e)

# 复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用
# shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充
# 还有glob模块
import shutil
shutil.copyfile("test.jpeg",r"C:\Users\cv\Desktop\test2.png") # 将目标文件复制为指定格式文件
shutil.copy("test.jpeg",r"C:\Users\cv\Desktop") # 保持原文件名复制到指定目录下

# 利用Python的特性来过滤文件
# 当前目录下的所有目录
print([x for x in os.listdir(".") if os.path.isdir(x)])
# 列出所有的.py文件
print([x for x in os.listdir(".") if os.path.splitext(x)[-1] == ".py"])