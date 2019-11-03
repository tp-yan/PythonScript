# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 15:05:14 2019

pandas数据处理: 6.排名索引
@author: tangpeng
"""
from pandas import Series,DataFrame

# 1.重新排序sort_index
# Series的sort_index：对inde默认升序
s = Series([3,2,1],index=list("acb"))
print(s)
print(s.sort_index())
print(s.sort_index(ascending=False))

# DataFrame.sort_index:多了轴向参数axis和by参数(只对列有效)
df0 = {'Ohio':[0,6,1],'Texas':[7,4,1],'California':[2,8,5]}
df = DataFrame(df0,index=list("adc"))
print(df)
print(df.sort_index())  # 默认按index升序
print(df.sort_index(axis=1))  # 按列名升序:California  Ohio  Texas
print(df.sort_index(by='Texas'))  # 按一列排序
print(df.sort_values(by='Texas'))  # 对列进行排序时，推荐使用sort_values：按但列的值来排序
print(df.sort_values(by=['Ohio','California']))   # 按多列排序


# 排名方法 Series.rank:会将排序对象的values替换成名次1~n
ser = Series([3,2,0,3],index=list("abcd"))
print(ser)
print(ser.rank())   # 对于相同值的行，根据参数method来决定名次，默认method=average
print(ser.rank(method='min'))   
print(ser.rank(method='max'))   
print(ser.rank(method='first'))

# DataFrame.rank:只多了 axis参数，可以按行或按列分别排名，没有对全部元素排名的方法
print(df.rank())        # 每列元素自个儿内部排名
print(df.rank(axis=1))  # 每行元素排名
print(df.rank(axis=1,method='first'))  # 每行元素排名

df = DataFrame({'a':[1,2,3,0],'c':["A","E","B","C"],'d':['a','b','d','c'],
                'b':[1,3,2,5]},index=[1,3,2,4])
print(df)
print(df.sort_index())
print(df.sort_index(axis=1))
print(df.sort_values(by='a'))
print(df.sort_values(by=['a','b']))

# 2.重新索引reindex
ser = Series([4.5,7.2,-5.3,3.6],index=list("dbac"))
A = list("abcde")
print(ser)
print(ser.reindex(A))
ser = ser.reindex(A,fill_value=0)  # 对多来的行用0填充
print(ser.reindex(A,method='ffill'))
print(ser.reindex(A,method='ffill',fill_value=0))


