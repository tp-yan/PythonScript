# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 16:13:15 2019

标准库之 time、random
@author: 10841
"""

from time import *
from random import *

date1 = (2016,1,1,0,0,0,-1,-1,-1)
time1 = mktime(date1) # 将时间元组转为 带小数的秒
date2 = (2017,1,1,0,0,0,-1,-1,-1)
time2 = mktime(date2)
random_time = uniform(time1,time2) # 均匀分布的一个随机变量
print(random_time)
# localtime:秒转为本地时间元组，asctime：时间元组转为字符串
print(asctime(localtime(random_time)))

# 指定骰子和面数，求一次掷骰子的总和
num = int(input("how many dice?"))
sides = int(input("how many sides per dice?"))

sum = 0
for i in range(num):
    sum += randrange(sides) + 1 # randrange参数与range一样，返回指定范围内的一个随机数
print("sum:",sum)

# 小于20的奇数
print(randrange(1,20,2)) # 2:步长
print(sample(range(20),5)) # 从序列中随机选择 n个不同的元素
print(choice(range(10))) # 随机选择一个元素

# 发牌程序
print("=======================")
values = list(range(1,11)) + "Jack Queen King".split()
print(values)
suits = "diamonds clubs hearts spades".split()
deck = ["{} of {}".format(v,s) for v in values for s in suits]
print(len(deck))
shuffle(deck)
while deck:
    input(deck.pop()) # 按回车键返回一张不重复的牌