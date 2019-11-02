# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 13:22:39 2019
语句断行
@author: tangpeng
"""

from pandas import DataFrame
from pandas import Series

df = DataFrame({'age':Series([26,85,64]),   # 一条语句多行写
                'name':Series(['Ben','Jon','Jef'])})
print(df)
print("juso"); print("123") # ;：可用于一行中分隔几条代码
