# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 13:28:05 2019

@author: cv

递归函数之汉诺塔问题
"""


def move(n,a,b,c):
    '''
    将n个盘子,借助b柱，从a柱移到c柱
    '''
    if n == 1:
        print("%d: %s --> %s " % (n,a,c)) # 只有一个时直接从a移到c，无需借助b
    else:
        # 借助c柱，将n-1个盘子从a柱移到b柱
        move(n-1,a,c,b)
        # 将n盘 a --> c
        print("%d: %s --> %s " % (n,a,c)) 
        # 现在的问题变成：将n-1个盘，借助a，从 b-->c
        move(n-1,b,a,c)

move(1,"a","b","c")
move(2,"a","b","c")
move(3,"a","b","c")
move(4,"a","b","c")
move(5,"a","b","c")