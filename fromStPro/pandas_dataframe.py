# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 10:16:55 2018

@author: tangpeng
"""

import pandas as pd
import numpy as np

#DataFrame:由共用同一索引的多列数据组成。是一个表格型的数据类型，每列值类型可以不同
#纵向索引用index表示， 也是0轴即axis=0
#横轴用column表示，是1轴，即axis=1
#DataFrame既有行索引、也有列索引
#DataFrame常用于表达二维数据，但可以表达多维数据

#DataFrame的创建
#从ndarray创建
d = pd.DataFrame(np.arange(10).reshape((2,5)))
d   #相比于ndarray数组，增加了行和列索引
#从字典创建:one、two是列名。键值对应列值。index为行索引值
dt = {'one':pd.Series([1,2,3],index=['a','b','c']), 
      'two':pd.Series([8,7,6],index=['b','c','d'])
    }
d = pd.DataFrame(dt)
d
#在字典中选择指定的key以及index生成，若key或者index不存在则用NaN填充
pd.DataFrame(dt,index=['a','b','c','d'],columns=['two','three'])

#从列表类型的字典创建
dl = {'one':[1,2,3,4],'two':['5',6.1,7,2]}
d = pd.DataFrame(dl,index=['a','b','c','d'])
d

dl = {'城市':['北京','上海','广州','深圳','沈阳'],
      '环比':[101.5,101.2,101.3,102.0,100.1],
      '同比':[120.7,127.3,119.4,140.9,101.4],
      '定基':[121.4,127.8,120.0,145.5,101.6]
      }
d = pd.DataFrame(dl,index=['c1','c2','c3','c4','c5'])
d
d.index     #获得0轴，即行索引值，Index对象
d.columns   #获得1轴，即列索引值，Index对象
d.values    #返回表格中的数据部分，array类型
d['同比']     #获得列数据，是Series对象
d.ix['c2']      #获得某一行数据，也是一个Series对象。index是其列名称
d['同比']['c2']   #获得单个数据


