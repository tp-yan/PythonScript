# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 13:39:01 2019
常用内建函数
@author: tangpeng
"""

print(abs(-1))
print(int(3.22))    # 浮点数转为整数
print(int("34"))    # 字符串(必须是整数字符串)转为整数
print(float(3))
print(float(".23")) # 0.23
print(float("1.23"))
print(str(123))
print(str(12.345))

c = complex(1,2)    # 定义复数
print(c) 
print(c.conjugate())    # 返回共轭复数

print(divmod(10,3)) # 相当于(x//y,x%y)：得到整数与余数

print(2 ** 3)   # 与下行相等
print(pow(2,3))

print(type(input("输入一个数字：")))   # <class 'str'>。input:只返回字符串类型
print(type(0))  # <class 'int'>。python一切皆对象
print(type(c))  # <class 'complex'>
print(type(1.23))   # <class 'float'>

# 获取对象id（地址）
print(id(1))
print(id(c))

# dir():查看指定模块中所包含的所有成员或者指定对象类型所支持的操作(属性与方法)
print("\nlist所支持的操作:\n",dir(list))
print("\nfunctools模块中所包含的所有成员:\n",dir('functools'))

# help()：返回指定模块或函数的说明文档
print("list的说明文档:\n")
help(list)
print("max的说明文档:\n")
help(max)
print("functools的说明文档:\n")
help('functools')

# ord():查询字符的ascii码
print(ord('a'))
print(ord('A'))
# 整数转字符
print(chr(98))

# len():字符串长度
print(len("abc"))
# 通过元素找索引
print("abc".index('b'))

# tuple list string的相同点：都可通过索引取元素，用len检查长度，可以使用‘+’和‘*’
print("a"+"cvb")
print("a" * 10)
# list.append/insert/pop/、del和list[n]赋值等方法只有list才有
# str.split():string转为list
print("I love python, and you? hehe".split())
print("I love python, and you? hehe".split(','))
print("I love python, and you? hehe".split('?'))
# split的逆运算：str.join()
print("abc".join("xyz"))    # 将‘abc’作为分隔符插入到“xyz”每两个元素间
print(":".join("ABC"))

# str.endswith/startswith
print("abcd".endswith("d"))
print("abcd".startswith("ab"))
# str.replace
print("xxxaazzzz".replace('a','X'))

# re模块中的 re.sub(被替词，替代词，替换域，flags=re.IGNORECASE)查找与替换
import re
S = "I love python, and you? hehe"
print(re.sub('python',"R",S))
print(re.sub('python',"R",S,flags=re.IGNORECASE))
print(re.sub('python',"R",S[0:15],flags=re.IGNORECASE))
