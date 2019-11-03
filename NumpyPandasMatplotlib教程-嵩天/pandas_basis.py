# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 13:45:57 2018

@author: tangpeng
"""

#Pandas是Python第三方库，提供高性能易用  数据类型  和   分析工具
#Pandas基于NumPy实现，常与NumPy和Matplotlib一同使用
#Pandas提供两个基于ndarray的数据类型：Series：一维, DataFrame：二维和多维数据
#Pandas的数据类型是基于NumPy的数据类型的

import pandas as pd
import numpy as np

d = pd.Series(range(20))
d.cumsum()  #求前N项累加和

#Series类型由一组数据及与之相关的数据索引组成
#Series类型的创建
#从list
a = pd.Series([9,8,7,6])    #自动生成索引从0开始
a
b = pd.Series([9,8,7,6],index=['a','b','c','d'])    #自定义索引值
b
#从标量值
s = pd.Series(25,index=['a','b','c'])   #index不能省略
s
#从字典类型1：key构成index，values对应values
d = pd.Series({'a':9,'b':8,'c':7})  #字典的key变成 Series对象的index值
d
#从字典类型2：从dict中选择指定的key-value构造Series,若有key不存在则其值为NaN
d2 = pd.Series({'a':9,'b':8,'c':7},index=['c','b','d'])     #float64类型
d2
#从ndarray创建
n = pd.Series(np.arange(5))     #使用自动生成的索引作为index的值
n
n2 = pd.Series(np.arange(5),index=np.arange(9,4,-1))    #指定index的值
n2

#Series的操作
#Series实际上由index(由Index对象表示)与values(由ndarray对象表示)组成
b = pd.Series([9,8,7,6],index=['a','b','c','d']) 
b.index
b.values
b['b']  #使用自定义的索引值
b[1]    #使用自动生成的索引值
b[['c','d',0]]  #不能混合使用，否则0会被当做自定义索引。若没有对应索引则返回NaN
b[['c','b','d']]

#Series的切片：返回一个Series类型
#可以通过自定义索引的列表进行切片
#可以通过自动索引进行切片，如果存在自定义索引，则一同被切片
b[3]    #索引值
b[:3]   #返回Series，包括对应的index与values
b[b>b.median()]
np.exp(b)   #也是返回一个Series对象

#Series的操作
'c' in b    # 判断数据是否在 index中,True
0 in b      # 不会判断自动生成的索引，False
b.get('f',100)  #类似dict的get，不存在返回默认值,100
#Series的对齐:Series类型在运算中会自动对齐不同索引的数据
a = pd.Series([1,2,3],['c','d','e'])
b = pd.Series([9,8,7,6],['a','b','c','d'])
a + b     # 相同index值进行运算，不同index值不运算。这里有Bug

#Series对象和索引都可以有一个名字，存储在属性.name中
b = pd.Series([9,8,7,6],['a','b','c','d'])
b.name
b.name = "Series对象"
b.index.name = "索引列"
b
#Series的修改：Series对象可以随时修改并即刻生效
b['a'] = 10
b.name = "Series"
b.name = "New Series"
b['a'] = 'aa'

#Series是一维带“标签”数组
#Series基本操作类似ndarray和字典，但其操作基于索引完成，根据索引对齐
