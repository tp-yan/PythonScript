# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 22:52:16 2019

python基础之序列：list+tuple+string

@author: tangpeng
"""

# 1.切片
numers = list(range(10))
print(numers[::4])
# 负数是从右往左取元素
print(numers[::-2])
print(numers[5::-1])
print(numers[:5:-2])

# 2.序列相加
print([1,2,3]+[4,5,6])
print("hello,"+"world!")

# 3.乘法:重复list n次
print('python' * 5)
print([42]*10)
print([42,11]*10)
# 初始化空list
print([None]*10)

# 4.成员资格检查：运算符 in
permissions = "rw"
print('w' in permissions)
print('x' in permissions)
users = ['mlh','foo','bar']
print(input('Enter your user name:') in users)

subject = "$$$ get rich now!!! $$$"
print("$$$" in subject)

database = [
        ['albert','1234'],
        ['dilbert','4242'],
        ['smith','7524'],
        ['jones','9843']
        ]

username = input('User name:')
pin = input('PIN Code:')
if [username,pin] in database:
    print('Access again!')

# 序列通用函数
numbers = [100,34,678]
print(min(numbers))
print(max(numbers))
print(len(numbers))
print(min(2,4,1))
print(max(1,18,41,12))
