# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 22:02:11 2018

@author: tangpeng
"""

import numpy as np

a = np.random.rand(3,4,5)   #均匀分布
b = np.random.randn(3,4,5)  #标准正态分布
c = np.random.randint(100,200,(3,4))    #根据shape创建随机整数或整数数组，范围是[low, high)
np.random.seed(10)                      #若随机种子相同，则产生的随机数也相同
d = np.random.randint(100,200,(3,4))
np.random.seed(10)    
e = np.random.randint(100,200,(3,4))

a = np.random.randint(100,200,(3,4))
np.random.shuffle(a)    #将a数组的第一维度乱序，a改变
np.random.shuffle(a)

a = np.random.randint(100,200,(3,4))
b = np.random.permutation(a)    # 与shuffle一样，但产生新数组，不改变a
c = np.random.randint(100,200,(8,))
np.random.choice(c,(3,2))   #从c中等概率选取某些元素形成 shape=（3,2）数组
np.random.choice(c,(3,2),replace=False)     # 不重复选取同一元素
np.random.choice(c,(3,2),p=c/np.sum(c))     # 值越大的数有更大概率被选中

u = np.random.uniform(0,10,(3,3))   #产生具有均匀分布的数组,uniform
n = np.random.normal(10,5,(3,3))   #产生具有正态分布的数组,10为均值,5标准差

# 梯度函数gradient
a = np.random.randint(0,20,(5))
np.gradient(a)  #最左侧元素： (后一个元素-自身)/1. 最右侧元素:(自身-前一个元素)/1，其他：(后一个-前一个)/2

b = np.random.randint(0,20,(5))
np.gradient(b)
#二维数组求梯度
c = np.random.randint(0,50,(3,5))
np.gradient(c)  #有几个维度就返回一个数组
