# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 13:27:15 2019

pandas数据处理: 1.数据清洗
处理缺失数据以及清除无意义的信息，如删除无关数据、重复数据，平滑噪声数据，处理缺失、异常值等

@author: tangpeng
"""

from pandas import Series,DataFrame, read_excel

data_source_path = r'C:\Users\tangpeng\Documents\my_data_source\big_data_source'
print("================数据清洗================")
# (1)处理重复数据
df = DataFrame({
        'age':Series([26,34,27,34,88,21,27]),
        'name':Series(['Tom','Lee','Jon','Lee','James','Curry','Curry'])
        })
print(df,'\n')
print(df.duplicated())  # 默认检查所有列(即所有列的值都相同才算是重复行)，将后面重复的行标记为True（即第一次出现的行不计为重复行），返回Series
print('\n')
# subset：只检查部分列的重复值
print(df.duplicated(subset='name')) # 只检查name这列，只要这列的值相同就被视为重复行，不管其他列的值
# keep=False:所有重复行都标记为True，包括第一行。keep='first'(默认)/'last':除了第一/最后一行外其他行都标记为True
print(df.duplicated(subset='age',keep=False)) # 只检查name这列，只要这列的值相同就被视为重复行，不管其他列的值
# 删除重复行，只保留一行
print(df.drop_duplicates()) 
print(df.drop_duplicates(['name']))     # 只检查 name 列


# (2)处理缺失值
# ①识别缺失数据 
# Pandas使用NaN表示浮点和非浮点数组里的缺失数据，使用.isnull() .notnull()：判断是否缺失
filename = r'\rz.xlsx'
df = read_excel(data_source_path+filename,sheet_name='Sheet2')
print(df)
print(df.isnull())
print(df.notnull())

# ②处理缺失数据
# 处理方式：数据补齐、删除对应行、不处理
# 1.删除对应行:dropna
newDf = df.dropna() # 删除包含NaN的行
print(newDf)
print(len(newDf))       # 返回行数
print(newDf.columns)    # 含列名的Index
newDf = df.dropna(how='all')    # 只有当所有列全为空时，该行才删除
print(newDf)
print(df.dropna(axis=1))    # 按列丢弃
print(df.dropna(how='all',axis=1))    # 按列丢弃
# 2.数据补齐:fillna
print(df.fillna('?'))
df.at[0,'数分'] = None
print(df.fillna(method='pad'))  # 使用该列的前一个值填充,若该行没有前一行，则仍然为NaN
print(df.fillna(method='bfill'))  # 使用该列的后一个值填充,若该行没有后一行，则仍然为NaN
# 使用平均值或其他统计量代替NaN
print(df.fillna(df.mean()))  # 使用该列的平均数替代
print(df.fillna(df.mean()['高代':'解几']))  # 用其他列('解几')均值替代指定列('高代')的NaN
# 不同列填充不同值
print(df.fillna({'数分':100,'高代':0})) # 没有列出的列不变
# strip()、lstrip()、rstrip()：清除字符型数据首尾指定的字符(默认空白符)
df2 = DataFrame({
         'age':Series([26,34,27,34,88,21,27]),
        'name':Series([' Tom','Lee ',' Jon',' Lee','James ','Curry ',' Curryy'])
        })
print(df2['name'])
print(type(df2['name']))        # <class 'pandas.core.series.Series'>
print(type(df2['name'][0]))     # <class 'str'>
print('+++++++++++++++++++++')
print(df2['name'].str)          # Series的属性，StringMethods类的实例，str：包含了很多处理字符类型的函数
print(type(df2['name'].str))    # <class 'pandas.core.strings.StringMethods'>
print('+++++++++++++++++++++')
print(df2['name'].str.strip())
print(df2['name'].str.lstrip('L'))   # 去除左边L开头的字符
print(df2['name'].str.rstrip('y'))  # 去除右边y结尾的字符


'''
 2.数据抽取
'''


