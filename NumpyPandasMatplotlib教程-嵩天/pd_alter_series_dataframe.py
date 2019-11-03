# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 12:42:10 2018

@author: tangpeng
"""

import numpy as np
import pandas as pd

#改变Series和DataFrame对象:增加元素或重排索引：重新索引。删除：drop
#.reindex()能够改变或重排Series和DataFrame索引

dl = {'城市':['北京','上海','广州','深圳','沈阳'],
      '环比':[101.5,101.2,101.3,102.0,100.1],
      '同比':[120.7,127.3,119.4,140.9,101.4],
      '定基':[121.4,127.8,120.0,145.5,101.6]
      }
d = pd.DataFrame(dl,index=['c1','c2','c3','c4','c5'])

#.reindex(index=None, columns=None, …)的参数
#d = d.reindex(['c5','c4','c3','c2','c1']) 因为Series是一维的，故默认是对0轴索引重排
#method 填充方法, ffill当前值向前填充，bfill向后填充
#copy 默认True，生成新的对象，False时，新旧相等不复制

d = d.reindex(index=['c5','c4','c3','c2','c1']) #重排0轴索引，即行索引顺序
d = d.reindex(columns=['城市','同比','环比','定基'])    #重排列索引顺序

newc = d.columns.insert(4,'新增')               #.insert(loc,e) 在loc位置增加一个元素e
newd = d.reindex(columns=newc,fill_value=200)   #fill_value 重新索引中，用于填充缺失位置的值
newd
#Series和DataFrame的索引是Index类型,Index对象是不可修改类型
d.columns   #列（1轴）索引
d.index     #行（0轴）索引
#Index方法：
#.append(idx) 连接另一个Index对象，产生新的Index对象
#.diff(idx) 计算差集，产生新的Index对象
#.intersection(idx) 计算交集
#.union(idx) 计算并集
#.delete(loc) 删除loc位置处的元素
#.insert(loc,e) 在loc位置增加一个元素e

nc = d.columns.delete(2)        #删除第二列,生成新的Index对象
ni = d.index.insert(5,'c0')
#nd = d.reindex(index=ni,columns=nc,method='ffill'):报错，用以下代替
nd = d.reindex(index=ni,columns=nc).ffill() #使用前一行/列的值来填充空值
nd

#.drop()能够删除Series和DataFrame指定行或列索引
a = pd.Series([9,8,7,6],index=['a','b','c','d'])
a.drop(['b','c'])
d.drop('c5')              #默认删数0/行索引
d
d.drop('同比',axis=1)     #删数列索引需要指定axis=1
