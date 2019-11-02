# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 19:09:52 2019

@author: cv
"""

"""
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
"""
def normalize(name):
    return name.title()

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

"""
Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
"""
from functools import reduce
def prod(L):
    return reduce(lambda x,y: x*y,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
    

"""
利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
"""
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2float(s):
    def char2Num(ch):
        return DIGITS[ch]
    dot = s.index('.')
    s = s.replace(".","")
    print(s)
    times = len(s)-dot; # 小数点后个数
    return reduce(lambda x,y: x*10+y,map(char2Num,s))*pow(0.1,times)
    
    
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
    
    
"""
把str转换为int的函数：
"""
def str2int(s):
    def char2Num(ch):
        return DIGITS[ch]
    return reduce(lambda x,y:x*10+y,map(char2Num,s))

print(str2int("1234654"))