# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 11:25:10 2018

@author: tangpeng
"""

import numpy as np
import pandas as pd

#对一组数据可以通过摘要来进行数据特征分析。摘要：对数据形成有损特征的过程
#1.排序：基于索引与元素值的排序
#2.基本统计函数
#3.累计统计函数
#4.相关性分析

#.sort_index(axis=0, ascending=True)方法在指定轴上 根据索引 进行排序，默认升序.不改变原数据
b = pd.DataFrame(np.arange(20).reshape(4,5),index=['c','a','d','b'])
b.sort_index()      #默认对0轴进行排序
b.sort_index(ascending=False)
c = b.sort_index(axis=1,ascending=False)    #对1轴进行降序排序
c.sort_index()

#.sort_values()方法在指定轴上 根据数值 进行排序，默认升序
#Series.sort_values(axis=0, ascending=True)
#DataFrame.sort_values(by, axis=0, ascending=True) by : axis轴上的某个索引或索引列表
c = b.sort_values(2,ascending=False)    #对0轴上，将第3列进行排序，其他行根据第3列结果进行排序
c
c.sort_values('a',axis=1,ascending=False)   #将‘a’所指向的行元素，进行排序，对应列按照该行元素排序

#若含有NaN元素，NaN不参与排序，统一放在末尾
a = pd.DataFrame(np.arange(12).reshape(3,4),index=['a','b','c'])
c = a+b
c.sort_values(2,ascending=False)
c.sort_values(2,ascending=True)

#pandas数据的基本统计分析
#适用于Series和DataFrame类型
#.sum() 计算数据的总和，按0轴计算，下同
#.count() 非NaN值的数量
#.mean() .median()  计算数据的算术平均值、算术中位数
#.var()  .std() 计算数据的方差、标准差
#.min() .max() 计算数据的最小值、最大值
#.describe() 针对0轴（各列）的统计汇总
#只适用于Series类型
#.argmin()  .argmax() 计算数据最大值、最小值所在位置的索引位置（自动索引）
#.idxmin()  .idxmax() 计算数据最大值、最小值所在位置的索引（自定义索引）
a = pd.Series([9,8,7,6],index=['a','b','c','d'])
a.describe()    #输入各项统计值：count mean std min max 25%... 
type(a.describe())  #是Series对象
a.describe()['count']   #获取单独的统计值
a.describe()['max']

b = pd.DataFrame(np.arange(20).reshape(4,5),index=['c','a','d','b'])
b.describe()
type(a.describe())  #是DataFrame对象
b.describe().ix['max']  #获得某一行
b.describe()[2]         #获得第3列数据

#累积统计分析
#适用于Series和DataFrame类型，累计计算
#.cumsum() 依次给出前1、2、…、n个数的和
#.cumprod() 依次给出前1、2、…、n个数的积
#.cummax() 依次给出前1、2、…、n个数的最大值
#.cummin() 依次给出前1、2、…、n个数的最小值
b.cumsum()
b.cumprod()
b.cummin()
b.cummax()

#滚动计算（窗口计算）
#.rolling(w).sum() 依次计算相邻w个元素的和
#.rolling(w).mean() 依次计算相邻w个元素的算术平均值
#.rolling(w).var() 依次计算相邻w个元素的方差
#.rolling(w).std() 依次计算相邻w个元素的标准差
#.rolling(w).min() .max() 依次计算相邻w个元素的最小值和最大值
b.rolling(2).sum()  #设置窗口大小为2，不存在的位置以NaN代替
b.rolling(3).sum()
b.rolling(3).var()
b.rolling(3).mean()
b.rolling(3).min()
b.rolling(3).max()

#数据的相关分析
#相关性
# X增大，Y增大，两个变量正相关
# X增大，Y减小，两个变量负相关
# X增大，Y没变化，两个变量不相关
#相关性的度量：
#1.协方差  协方差>0, X和Y正相关 协方差<0, X和Y负相关 协方差=0, X和Y独立无关
#2.Pearson相关系数：0.8‐1.0 极强相关 0.6‐0.8 强相关 0.4‐0.6 中等程度相关 0.2‐0.4 弱相关 0.0‐0.2 极弱相关或无相关

#.cov() 计算协方差矩阵
#.corr() 计算相关系数矩阵, Pearson、Spearman、Kendall等系数
index = ['2008','2009','2010','2011','2012']
hprice = pd.Series([3.04,22.93,12.75,22.6,12.33],index=index)
m2 = pd.Series([8.18,18.38,9.13,7.82,6.69],index=index)
hprice.corr(m2) #0.5239439145220387，说明两者是中等相关

import matplotlib.pyplot as plt
#在一幅图上绘制两条线
plt.title('房价与M2的相关性',fontproperties='SimHei')  #设置fontproperties显示中文
plt.plot(index,hprice,'-.*',label='hprice')
plt.plot(index,m2,':+',label='m2')
plt.legend()    #显示上面2条语句的 label
plt.xlabel('时间',fontproperties='SimHei')
#plt.ylable('')
plt.show()
