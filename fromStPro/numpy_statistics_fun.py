# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 22:30:01 2018

@author: tangpeng
"""

import numpy as np
#numpy的统计函数

a = np.arange(15).reshape(3,5)
np.sum(a)           # axis=None，即所有元素求和
np.sum(a,axis=0)
np.sum(a,axis=1)

np.mean(a,axis=1)   #第二维数据求平均
np.mean(a,axis=0)   

np.average(a,axis=0,weights=[10,5,1])   # 求加权平均
#4.1875 = (2*10+7*5+12*1)/(10+5+1)
np.std(a)   #标准差
np.var(a)   #方差

b = np.arange(15,0,-1).reshape(3,5)  # 15-->1
np.max(b)
np.argmax(b)    # 将数组b扁平化，即降成一维数组后，找到最大值下标  argmin最小值

np.unravel_index(np.argmax(b),b.shape)  #将一维展开的元素下标，求其在指定多维下的索引
np.ptp(b) # 最大值与最小值差
np.median(b)    # 求中位数，返回浮点数

#梯度函数