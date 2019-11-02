# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 15:23:52 2019

pandas数据处理: 2.数据抽取

@author: tangpeng
"""

from pandas import Series,DataFrame, read_excel


data_source_path = r'C:\Users\tangpeng\Documents\my_data_source\big_data_source'
print("\n================数据抽取================\n")
# 1. 字段抽取：将某列的每个单元格数据的一部分抽取出来成为新列
filename = r'\i_nuc.xls'
df = read_excel(data_source_path+filename,sheet_name='Sheet4')
print(df.head())
df['电话'] = df['电话'].astype(str) # 转为str类型,读入的是float型
print(df.head())

# 号码前3位是运营商
bands = df['电话'].str.slice(0,3) 
print(bands)
# 地区：中间4位
area = df['电话'].str.slice(3,7) 
print(area)
# 手机号：最后4位
tell = df['电话'].str.slice(7,11) 
print(tell)

# 2.字段分隔：指定分隔符sep，拆分字符串
df = read_excel(data_source_path+filename,sheet_name='Sheet4')
df['IP'].str.strip()   # 去掉首尾空格
# split(sep,n,expand=False): n:新增的列数，expand=True:展开为DataFrame，否则为Series
newDF = df['IP'].str.split('.',1,True) # 分隔出来1列后，就不再拆分单元格数据，剩下的数据位一列
print(newDF)
newDF.columns = ['IP_1','IP_2_4']       # 添加列名称
print(newDF)
print(df['IP'].str.split('.',2,True))
print(df['IP'].str.split('.',1,False))  #  每列为Series：[ 221, 205.98.55]

# 3.重置索引：指定某列为索引index
df = DataFrame({
        'age':Series([26,34,27,34,88,21,27]),
        'name':Series(['Tom','Lee','Jon','Lee','James','Curry','Curry'])
        })
df1 = df.set_index('name')    # name列成为索引列
print(df1)
# ix()是loc(索引)、iloc(索引号)的混合：通过行标签或行号返回一行数据
# print(df1.ix['Jon']) 
print(df1.loc['Curry']) 

# 4.记录抽取：按条件进行过滤
# df[condition],condition:过滤条件，返回DataFrame
df = read_excel(data_source_path+filename,sheet_name='Sheet4')
print(df)
print(df[df.电话 == 13322252452])     # 不能用df.'电话'
print(df[df.电话 > 13500000000])
print(df[df.电话.between(13400000000,13599999999)])
print(df[(df.电话>=13400000000) & (df.电话 < 16899999999)])
print(df[df.IP.isnull()])   # 找到空值行
print(df[df.IP.str.contains('222.',na=False)])  # na=False:去掉NaN值
print(df[df.IP.str.contains('222.',na=True)])

# 5.随机抽样：按一定的行数与比例抽样
import numpy
r = numpy.random.randint(0,10,3)    # 产生0~10内的随机3个整数
print(r)
print(df.loc[r,:])  # 或df.loc[r] :抽取r行数据

# 6.通过索引抽取数据
# 注：选择多行数据，行索引(号/名)必须是list形式
# (1)通过索引名选取数据
# df.loc[行标签，列标签]，若行、列标签都是list则返回DataFrame，否则返回Series
df = df.set_index('学号')     # 覆盖原来的index
print(df)
print(df.loc[2308024241:2308024347])    # df.loc['a':'b']从'a'行到'b'行（包含）的数据。默认所有列
print(df.loc[:,'电话'].head())
print(df.loc[2308024310])    # 抽取 学号=2308024310的行，返回Series
print(df.loc[[2308024310,2308024219]])    # 抽取 两行，返回 DataFrame
# (2)通过索引号选取数据
# df.iloc[行索引号，列索引号]
print(df.iloc[1,0])     # 第一行，第一列，返回单元格数据
print(df.iloc[[0,3],:]) # 第一、三行
print(df.iloc[0:3,:])   # 第一到三行
print(df.iloc[:,1])   # 第二列,返回Series
print(df.iloc[1,:])   # 第二行,返回Series
print(df.iloc[1])   # 第二行,返回Series

# 7.字典数据抽取
# 将字典数据抽取为DataFrame
# (1)字典的key,value各作为一列
d1 = {'a':'[1,2,3]','b':'[0,1,2]'}  # 这种方式，一个key只能对应简单的value，不能是list、tuple这种多值结构
a1 = DataFrame.from_dict(d1,orient='index') # 字典转为DataFrame,将key作为index列
print(a1)   # 此时,index列没有名字
a1.index.name = 'key'
print(a1)
b1 = a1.reset_index()   # 重置index列，原来的索引列(key列)将作为新的第一列，此时index列也没有名字
print(b1)   
print(b1.columns)   
b1.columns = ['Key','Value']    # 给列命名，不同于index列
print(b1)
# (2)字典里的每一个元素作为一列(各列同长): 即key作为列名，每个value成为一列
d2 = {'a':[1,2,3],'b':[0,1,2]}
a2 = DataFrame(d2)
print(a2)
# (3)字典里的每一个元素作为一列(各列不同长):空缺值填NaN
d3 = {'one':Series([1,2,3]),
      'two':Series([1,2,3,4])}
a3 = DataFrame(d3)
print(a3)