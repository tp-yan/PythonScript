# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 09:06:19 2019

标准库之file：标准输入与输出以及管道
@author: 10841
"""

# 计算 sys.stdin中单词个数
import sys

text = sys.stdin.read() #  sys.stdin：流对象，类似于文件对象
words = text.split()
wordcount = len(words)
print("wordcount:",wordcount)

# 控制台输入：
# cat .\basis_module_file_stdin.txt | python .\basis_module_file.py
# 利用管道将 cat的标准输出sys.stdout 链接到 标准输入 sys.stdin，然后 python脚本从
# sys.stdin读入数据

"""
打开文件模式：
x:独占写入，若文件已存在则报错
a:追加模式
b:二进制模式，需与其他模式结合使用
t:文本模式，需与其他模式结合使用。
+:读写模式，可与其他任何模式结合使用。
r+:在文件尾部追加
w+:清空所有内容再写入
open()默认模式就是rt，即打开文本文件，则会经过自动编码和解码过程，默认按utf-8编码
参数encoding:可指定编码格式
"""
with open("test_file.txt","w") as f:
    f.writelines(["abc\n","def\n","ijk\n"])

with open("test_file.txt","r+") as f:
    print(f.read())
    f.write("123")
    f.flush()
    f.seek(0)
    print(f.read())

with open("test_file.txt","w+") as f:
    print(f.read())
    f.write("321")
    f.flush()
    f.seek(0)
    print(f.read())