#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 16:08:48 2019

@author: tangpeng

itertools模块：提供了非常有用的用于操作迭代对象的函数。
"""


"""
1. 首先看看itertools提供的几个“无限”迭代器：
注：无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来
"""
import itertools

# 1.1 count()会创建一个无限的迭代器，此函数无法终止
def func_count():
    naturals = itertools.count(0)  # 返回无限迭代器/序列
    for n in naturals:
        print(n)

# 1.2 cycle()会把传入的一个序列无限重复下去
def func_cycle():
    cs = itertools.cycle("ABC")
    for c in cs:
        print(c)
        
# 1.3 repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
def func_repeat(e,n):
    ns = itertools.repeat(e,n)
    for n in ns:
        print(n)

"""
2.tertools提供的几个迭代器操作函数更加有用
"""

# 2.1 chain():把一组迭代对象串联起来，形成一个更大的迭代器
def func_chain():
    for c in itertools.chain("ABC","abc"):
        print(c)
        
# 2.2 groupby():把迭代器中相邻的重复元素挑出来放在一起

def func_groupby():
    for key,group in itertools.groupby("AAABBBCCAAA"):
        print(key,"-->",list(group))
# 实际上groupby()挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key。
# 如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：    
def func_groupby_custom():
    for key,group in itertools.groupby("AaaBBbcCAAa",lambda c:c.upper()):
        print(key,"-->",list(group))

"""
练习
计算圆周率可以根据公式：
利用Python提供的itertools模块，我们来计算这个序列的前N项和：
"""
def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    odd_seq = itertools.count(1,2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    data = []
    for  n in odd_seq:
        if n > 2*N-1:
            break
        data.append(n)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    flag = -1
    for n in range(len(data)):
        flag = -flag
        data[n] = 4 / data[n] * flag
            
    # step 4: 求和:
    return sum(data)

def func_test():
    # 测试:
    print(pi(10))
    print(pi(100))
    print(pi(1000))
    print(pi(10000))
    assert 3.04 < pi(10) < 3.05
    assert 3.13 < pi(100) < 3.14
    assert 3.140 < pi(1000) < 3.141
    assert 3.1414 < pi(10000) < 3.1415
    print('ok')


if __name__ == "__main__":
#    func_cycle()
#    func_repeat('A',3)
#    func_chain()
#    func_groupby()
#    print()
#    func_groupby_custom()
     func_test()
    