#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 22:46:54 2019

@author: tangpeng

StringIO和BytesIO
"""

"""
StringIO是存在于内存中的对象，创建StringIO对象，相当于打开了一个文件对象，只能往里读写str
"""
# str写入StringIO
from io import StringIO

f = StringIO()
f.write("hello")
f.write(" ")
f.write("world!")
print(f.getvalue())

# 从 StringIO 读取 str
# 要读取StringIO，可以用一个str初始化StringIO，然后像读文件一样读取：
f = StringIO("hello,\tworld!")
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
    
"""
BytesIO与StringIO类似，但是只能往里读写 bytes 对象
"""
from io import BytesIO
f = BytesIO()
f.write("中文".encode("utf-8")) # 只能写入 bytes
print(f.getvalue()) # b'\xe4\xb8\xad\xe6\x96\x87'
print(f.getvalue().decode("utf-8")) # bytes --> str

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
#print(f.read().decode("utf-8"))