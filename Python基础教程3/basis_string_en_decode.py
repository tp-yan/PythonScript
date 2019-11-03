# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 17:41:07 2019

字符串之编码处理:
    在Python中不同字符集之间的转换，需要使用 str类型 作为中间的转换桥梁，str就是不同
    编码之间转换的标准。
    注：对字符串的编码与解码必须是同一套编码规则，否则导致乱码
@author: 10841
"""
import chardet # 第三方库，判断字节码的编码方式

# str类型能与任何编码规则之间相互转换
a = '我叫大强' # Python默认字符串类型str使用的是Unicode字符集
str_gb2312 = a.encode('gb2312') # 将 str 转为 gb2312编码的 字节码
print('gb2312:',str_gb2312)
# 由gb2312转为utf-8，必须先解码为 str，再从 str 转为utf-8
gb2312_utf8 = str_gb2312.decode('gb2312').encode('utf-8')
print('utf-8:',gb2312_utf8)
# utf-8转gbk同理
utf8_gbk = gb2312_utf8.decode('utf-8').encode('gbk')
print('gbk:',utf8_gbk)
str_gbk = utf8_gbk.decode('gbk') 
print(str_gbk)

# chardet.detect:只能检查字节码的编码方式
print(chardet.detect(utf8_gbk))
print(chardet.detect(str_gbk.encode())) # Python默认的编码是utf-8

str_gb18030 = str_gbk.encode('gb18030') # 相当于从 utf-8转为 gb18030
print(str_gb18030)
print(str_gb18030.decode('gb18030'))

# gb2312,gb18030,gbk：都是中国的编码，后面的兼容前面的编码格式，故它们得到的字节码都一样
# 小示例：读取二进制文件
path = r'C:\Users\10841\Documents\MyDocument\Data\bigdata_analysis'
filename = r'f_utf8.txt'
filename_ansi = r'f_utf8_ansi.txt'

file_ansi = open(path+"\\" + filename_ansi) # 默认以'rt'读取文本文件，并以所在操作系统
#默认的编码格式(win上是gbk)解码
content_ansi = file_ansi.read()
file_ansi.close();
print(content_ansi)

file = open(path+"\\" + filename,encoding='utf-8') # 所以读取非gbk编码的文件时，指定解码格式
content = file.read()
file.close()
print(content)
# 也可以按照二进制格式先读入后，再自己指定解码格式
file = open(path+ "\\" + filename,'rb')
file_b = file.read()
file.close()
print(file_b)
print(chardet.detect(file_b))
print(file_b.decode('utf-8'))

