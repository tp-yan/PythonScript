# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 09:13:04 2019

标准库之file：随机存取
@author: 10841
"""

f_path = r"somefile.txt"

f = open(r"somefile.txt","w") # "w"：不存在，则创建，覆盖式写入
f.write("abcdefghijklmn")
print(f.seek(5)) # offset=5：相对偏移量5个字节(字符)，参数whence默认为文件开头位置
f.write("00000")
f.close()

f = open(r"somefile.txt")
print(f.read()) # 从当前文件指针位置，读取余下所有的内容
f.close()

f = open(r"somefile.txt")
print(f.read(3)) # 指定多3个字节/字符
print(f.read(4))
print(f.tell()) # 当前文件读写指针位置
print(f.read())
f.close()

'''
一行读入：readline
读取所有行，列表返回：readlines
写入：write
写入多行：writelines传入字符串列表，注意必须手动添加换行符,不会自动换行
flush：将文件写入缓存立即写入到磁盘，并清空缓冲区
推荐使用 with 上下文管理器来读写文件
'''
with open(f_path,"a+") as file:
    file.writelines(["\nyour","\n","mother","\n","is a beautiful \n","women"])
    file.flush()
    file.seek(0) # 重置文件指针位置
    print(file.readlines())