# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 19:50:27 2019

字符串
@author: tangpeng
"""

# 1.拼接
print("x"+"y")

# 2.字符串的表示str和repr()
s1 = str("hello,\nworld!")  # 以类str存储、表示字符串
print(type(s1))
print(s1)

s2 = repr('hello,\nworld!')
print(type(s2)) # 也是str类
print(s2)       # 原样输出字符串，不会转义

# 3.长字符串：即跨越多行的字符串,用三引号表示
print('''长字符串：即跨越多行的字符串,用三引号表示
      长字符串：即跨越多行的字符串,用三引号表示
      长字符串：即跨越多行的字符串,用三引号表示''')   # 单双引号都可以，保留原来字符串的多行结构
# 4.原始字符串：不处理反斜杠\，每个字符都保持原样，尤其在表示路径时很有用
path = r'C:\Users\tangpeng\Documents\n\t' # 注：不能以'\'结尾，可以把'\'单独成一个字符串再拼接
print(path)
print(path + "\\")

# 5.Unicode、bytes、bytearray
# python使用Unicode来编码字符串，而字符串本质也是字节序列
# 表示Unicode字符: 16或32位的十六进制字面量表示 or 字符的Unicode名称：\N{name}
print('\u00c6')
print('\U0001F60A')
print('This is a cat:\N{Cat}')
print('This is a Pig:\N{Pig}')
print('This is a Dog:\N{Dog}')
print('This is a Man:\N{Man}')
print('This is a Woman:\N{Woman}')

# 在内存和磁盘中所有对象都是以二进制表示
# 5.1 创建bytes对象(而不是字符串)
byte = b'hello,world'  # bytes是不可变对象，另外一个是可变对象bytearray也表示字节序列对象
print(type(byte))   # <class 'bytes'>
print(byte)

'''
Unicode与utf-8的关系：
Unicode是一个标准，定义了一个字符集以及一系列的编码规则。
一个字符集：即Unicode字符集：为每一个字符分配一个唯一的ID，即码点，一个整数。
一系列的编码规则：UTF-8、UTF-16、UTF-32 等等编码。
编码规则：将「码点」转换为字节序列的规则（编码/解码 可以理解为 加密/解密 的过程）
UTF-8：是一套以 8 位为一个编码单位的可变长编码，而UTF-32是固定编码
'''

# 5.2编码与解码：即字符串与字节序列之间的按一定规则的转换
s = "hello,world!"
print(s.encode("ASCII")) # 将字符串按不同编码规则编码   
print(s.encode("UTF-8"))    
print(s.encode("UTF-16"))    
print(s.encode("UTF-32"))
s2 = "How long is this?"
print(len(s2.encode('UTF-8')))  # utf-8:对ascii范围内的按一个字节编码
print(len(s2.encode('UTF-16'))) # 固定2字节
print(len(s2.encode('UTF-32'))) # 固定4字节

s3 = "щыдへぬぬ㉮ㅖㅙㅞㅞ hello" 
try:
    print(s3.encode('ascii'))   # 默认第二个参数（编码出错时如何处理）为 strict
except Exception as e:
    print("编码错误(一般是超出编码规则的编码范围)：\n",e)
print(s3.encode('ascii','ignore'))
print(s3.encode('ascii','replace'))
print(s3.encode('ascii','backslashreplace'))
print(s3.encode('ascii','xmlcharrefreplace'))

# 在python中默认使用的就是utf-8
print(s3.encode())

# 将编码后的字节序列解码为字符串
print(s3.encode().decode()) # 解码默认也是按utf-8
print(s3.encode('utf-16').decode('utf-16')) 
try:
    print(s3.encode('utf-16').decode('utf-8')) 
except Exception as e:
    print("解码错误(编码与解码必须采用同一个编码规则)：\n",e)

'''
编码解码最重要用途之一：将文本存储于磁盘上。只要文本使用的是utf-8，使用python操作文件时，
就无须担心编码解码问题，python已自动完成。
乱码：即编码与解码使用不同的编码规则，就会出现这种问题
注：python的源代码也会被编码，默认也使用的是utf-8，但可以在文件开头指定该文件存储时的编码规则
# -*- coding: encoding name -*-
encoding name:如utf-8，ascii,ansi,latin-1等
'''

# 直接创建bytes和str对象，不使用encode与decode
print(type(b'hello'))
by = bytes("hello,щыдへぬぬ!",encoding='utf-8')    # 用字符串创建bytes对象
print(by)
st = str(by,encoding='utf-8')  # 使用字节序列按照utf-8生成字符串对象
print(st)
