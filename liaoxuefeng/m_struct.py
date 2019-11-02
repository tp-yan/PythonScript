#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 19:39:22 2019

@author: tangpeng

struct模块来解决bytes和其他二进制数据类型的转换。
struct的pack函数把任意数据类型变成bytes，unpack把bytes变成相应的数据类型。

struct模块定义的数据类型可以参考Python官方文档：
https://docs.python.org/3/library/struct.html#format-characters
"""

"""
练习
请编写一个bmpinfo.py，可以检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数。
"""
import base64,struct


# pack的第一个参数是处理指令，'>I'的意思是：>表示字节顺序是big-endian，也就是网络序，I表示后面操作的是4字节无符号整数。
b1 = struct.pack(">I",10240099) # 将对象转为字节字符串
print(b1)
# >IH:后面的bytes依次变为 I：4字节无符号整数和 H：2字节无符号整数。
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))
print(struct.unpack('>H', b'\x80\x80'))


with open("test1.bmp","rb") as f:
    data = f.read()
    print(len(data)/1024,"K",type(data))
    data = data[:30] # 取前30个字节
"""
BMP格式采用小端方式存储数据，文件头的结构按顺序如下：
两个字节：'BM'表示Windows位图，'BA'表示OS/2位图； 
一个4字节整数：表示位图大小； 
一个4字节整数：保留位，始终为0；
 一个4字节整数：实际图像的偏移量； 
 一个4字节整数：Header的字节数； 
 一个4字节整数：图像宽度； 
 一个4字节整数：图像高度； 
 一个2字节整数：始终为1； 
 一个2字节整数：颜色数。
"""
info = struct.unpack("<ccIIIIIIHH",data) # 将字节字符串每个字节按要求分别解析
print(info) # 尺寸 286x141，大小121314bytes



bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')

def bmp_info(data):
    print(len(data))
    data = data[:30]
    info = struct.unpack("<ccIIIIIIHH",data)
    print(info)
    if info[:2] == (b'B', b'M'):
        color = info[-1]
        width = info[-4]
        height = info[-3]
    
    return {
        'width': width,
        'height': height,
        'color': color
    }

# 测试
bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')