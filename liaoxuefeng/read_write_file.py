#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:01:38 2019

@author: tangpeng

文件读写
"""

# 1. 指定编码格式读取文本文件
f = open("./hello.py",'r',encoding='utf-8')
print(f.read())
print(f.readline())
print(f.readlines()) # readlines()一次读取所有内容并按行返回list
f.close() # 只有调用了close()，才保证内容全部写到磁盘中


# 无须调用 close()
with open("./hello.py",'r',encoding='utf-8')  as f:
    for line in f.readlines(): # 注意会读入 换行符 \n
        print(line.strip()) # 把末尾的'\n'删掉
    
# 2. 读取二进制文件
with open("./test.jpeg","rb") as f:
    print(f.readline())
    
# 3. 写文件
with open("./test.txt","w",encoding='utf-8') as f:
    f.write("hello,hi!\n 1024")
    
with open("./test.txt","a",encoding='utf-8') as f:
    f.write("append")
   
    
print()
"""
练习
请将本地一个文本文件读为一个str并打印出来：
"""
fpath = r'C:\Windows\system.ini'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)