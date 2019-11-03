# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 15:26:30 2019

pandas数据处理: 3.插入数据
pandas没有 指定索引而插入行的方法，只能通过 拼接 来实现

@author: tangpeng
"""
import pandas
from pandas import DataFrame

df = DataFrame({'a':[1,2,3],'b':['a','b','c'],'c':["A","B","C"]})
print(df)
# 将插入的行，也是DataFrame类型,需保持列名一致
line = DataFrame({df.columns[0]:"--",df.columns[1]:"--",df.columns[2]:"--"},
                  index=[1])
print(line)
# pandas.concat:拼接多个DataFrame
# 注：df.loc[:0]：切片，返回DataFrame，不能是df.loc[0]：抽取一行，返回Series
df0 = pandas.concat([df.loc[:0],line,df.loc[1:]])
print(df0)  # index没有更新
# 更新index：
# 方法一: reset_index 后，删除新增的index列，即原来的index列
df1 = df0.reset_index()
print(df1)
df2 = df1.drop('index',axis=1)  # 删除列
print(df2)
# 方法二: reset_index 添加参数drop=True，删除原来的index列后重新生成index列
df3 = df0.reset_index(drop=True)
print(df3)
# 方法三：重新给index赋值，不会增删列
df4 = df0.index=range(len(df0.index))
print(df4)
