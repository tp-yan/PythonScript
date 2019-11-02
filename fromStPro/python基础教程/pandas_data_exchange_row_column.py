# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 13:12:59 2019

pandas数据处理: 5.交换行或列
@author: tangpeng
"""
import pandas as pd

# 1.使用 df.reindex 交换2行或2列
df = pd.DataFrame({'a':[1,2,3],'b':['a','b','c'],'c':['A','B','C']})
print(df)

# 交换2行
hang = [0,2,1]  # 新的 index 序
print(df.reindex(hang))

# 交换2列
lie = ['a','c','b'] # 列名序
print(df.reindex(columns=lie))

# 2.DIY实现 reindex
df.loc[[0,2],:] = df.loc[[2,0],:].values   # 直接交换第0与2行数据,index不变
print(df)
df.loc[:,['b','a']] = df.loc[:,['a','b']].values   # 交换'a' 'b'2列，但列名也没变
print(df)   # 交换列后，需要更新列名
# 更新列名
name = list(df.columns)
i = name.index('a')
j = name.index('b')
name[i], name[j] = name[j], name[i] # 交换'a''b'在columns中的位置
df.columns = name
print(df)

# 插入列
df['d'] = range(len(df.index))  # 新增加一列
print(df)
# 将'd'移到'b''a'中间
# 'd'与‘c’列交换
df.loc[:,['c','d']] = df.loc[:,['d','c']].values
name = list(df.columns)
i = name.index('c')
j = name.index('d')
name[i], name[j] = name[j], name[i]
df.columns = name
# 'd'与‘a’列交换
df.loc[:,['a','d']] = df.loc[:,['d','a']].values
name = list(df.columns)
i = name.index('a')
j = name.index('d')
name[i], name[j] = name[j], name[i]
df.columns = name
print(df)
