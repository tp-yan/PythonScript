# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 15:55:27 2019

pandas数据处理: 4.修改数据
@author: tangpeng
"""
from pandas import read_excel,DataFrame


data_source_path = r'C:\Users\tangpeng\Documents\my_data_source\big_data_source'
filename = r'\i_nuc.xls'

# 1.整体替换：一行，一列进行值替换
df = DataFrame({'a':[1,2,3],'b':['a','b','c'],'c':["A","B","C"]})
df['a'] = [0,0,0]   # 或者是Series
print(df)
# 2.个别修改
# (1)单值替换
df = read_excel(data_source_path+filename,sheet_name='Sheet3')
print(df.replace('作弊',0))   # replace({'作弊':0})
# (2)指定列单值替换
print(df.replace({'体育':'作弊'},0))
print(df.replace({'体育':'作弊','军训':'缺考'},0))
# (3)多值替换
print(df.replace(['成龙','周怡'],['陈龙','周毅']))
print(df.replace({'成龙','周怡'},{'陈龙','周毅'}))  # 一样
print(df.replace({'成龙':'陈龙','周怡':'周毅'}))  # 一样
