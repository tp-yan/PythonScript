# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:34:46 2019

数据处理工具之Pandas(panel data analysis):python的一个数据分析包，适合时间序列分析
Panel data(面板数据):经济学中关于多维数据集的术语
Pandas数据结构：Panel、Series、DataFrame(后2个构建在Numpy之上)
Series：一维数据序列，与numpy中的一维array类似
DataFrame：二维表格型数据结构，可理解为Series的容器
Panel：三维数组，可理解为DataFrame的容器
@author: tangpeng
"""

# 数据准备
# 数据类型：python常见3种类型：Logic、Numeric、Character
# 1. Logic(逻辑型-布尔型)，逻辑运算： &、|、not
# 2. Numeric(数值型)
# 3. Character(字符型)
# 变量命名不能以数字或下划线开头

# 数据结构(Pandas中常用的是Series和DataFrame)
# 1. Series：存储一行或一列数据，以及数据对应的索引值，Series([data1,data2,..],index=[idx1,idx2,...])
# 2. DataFrame数据框：存储多行多列数据集合，是Series的容器，类似于Excel二维表格，其操作无外乎增删改查

import numpy as np
from pandas import Series
from pandas import DataFrame


# =========================Series=========================
'''
Series：存储一行或一列数据，以及数据对应的索引值，Series([data1,data2,..],index=[idx1,idx2,...])
1. Series对象本质就是一个Numpy数组，Numpy的数组函数可以直接对Series进行处理
2. Series不仅有数据还有索引(当做数据的标签key)，可通过标签存取元素，与字典类似
3. Series由2部分(属性)组成：(1)index：从Numpy数组继承的index对象，保存标签信息
                         (2)values:保存值的Numpy数组
4. Series数据类型没有限制(任何Numpy数据类型)
5. Series同时具有数组与字典的功能，支持部分字典方法
'''

# 创建序列对象
# Series对象的元素类型不要求相同
X = Series(['a',2,'螃蟹'],index=[1,'a',1.2])
print(X)
S = Series([1,2,3])     # 默认index从0开始，这种默认的index，称为索引号
print(S)
A = Series([1,2,3],index=['a','b','c']) # 指定index的值，这种非默认的index，称为索引名
print(A)
# Series的元素通过索引号来访问，值与索引号是一一对应的，如果设置了索引名，也可通过索引名访问
print(A[0])     # 索引号访问
print(A['c'])   # 索引名访问

# 用字典创建Series，key作为标签
B = Series({'a':1, 'b':3, 'c':3})
print(B)


# Series不能追加单个元素，但能追加序列
X = Series(['a',True,1],index=['1st','2nd','3rd'])
n = Series(['2'])   # 索引号默认为0
X = X.append(n)     # 追加返回的是新序列

print(X.values) # X的属性values：返回ndarray，一维数组
print( 2 in X.values)
print( True in X.values)
print( '2' in X.values)

# 可以追加相同索引号的序列:但是强烈建议别这么做，若存在一个索引对应多个值，那么Series将不能被修改，只能读
n = Series(['3'])   # 索引号默认为0
X = X.append(n)     # 追加返回的是新序列
print(X)
print(type(X[0])) # 如果一个索引(号/名)(即存在同名的索引)对应多个值，则返回的是一个Series对象，而不是单个值
print(X[0][0])      # 返回的还是Series，所以同索引的值无法取出来

# 切片：根据索引号
print("\n\n")
print(X[1:3])
print(X[:])

# 定位获取，常用于随机抽样
print("\n\n")
print(X[[0,2,1]])    # 返回Series，按照传入的列表索引号排序

# 根据索引删除
print("\n\n")
print(X.drop(0))    # 返回新Series
print("\n\n")
print(X.drop('2nd'))

# 根据索引号找索引名, X.index:返回的是一个Index对象，一维数组
print(X.index)
print(X.index[2])
print(X.index[[2,3]])   # 返回Index对象，类似于对list做切片的效果
print(X.drop(X.index[2]))

print( '2' != X.values)   # 返回布尔ndarray一维数组，list没有这种批量操作
# 显示值不等于'2'的序列，即删除'2'，返回新序列
print(X[ '2' != X.values])

X = X.drop(0)   # 把索引号0对应的所有值删除。删掉一个索引多个值，Series才能修改
print(X)
# 批量修改序列的值:
print(X.values == True)     # 这里会把整数1当做True来处理,返回ndarray
X[X.index[X.values == True]] = 'b'  # 会将所有True的项，改为'b'
print(X)
# 得到某个值对应的index
print(X.index[X.values == 'a'])

a = np.array([1,2,3,4])
print(a[[True,False,False,True]])   # 对数组进行筛选
print(a[[0,2,3,1]])     # 将数组重新排列

# 修改Series的Index部分
X.index = [2,3,4]
print(X)

# 对index排序
X.sort_index(ascending=True)    # 默认升序
X = X.sort_index(ascending=False)    # 默认升序
print(X)

# 使用reindex重排序
obj = Series([4.5,7.2,-5.3,3.6],index=['a','b','c','d'])
print(obj)
obj2 = obj.reindex(['a','b','c','d','e'])   # 若索引的值不存在则引入缺失值
print(obj2)
print(obj.reindex(['a','b','c','d','e'],fill_value=0))  # 使用指定值填充缺失值

# =========================Series=========================


# =========================DataFrame=========================
'''
DataFrame数据框：存储多行多列数据集合，是Series的容器，类似于Excel二维表格，其操作无外乎增删改查
'''

# 创建DataFrame
print("=========================DataFrame=========================")
df = DataFrame({'age':Series([26,28,30]),'name':Series(['Ken','Ben','Jon'])},index=[0,1,2])
print(df)
# index也可省略
df = DataFrame({'age':Series([26,28,30]),'name':Series(['Ken','Ben','Jon'])})

#  访问某列: df[列名]
A = df['age']
print(A)    # Series对象

# 访问一/多行： df[n:m]: 从n到m-1的行
B = df[1:2]     # 即使访问一行也必须用这种形式，不能是 df[1] 这种
print(B)
print(df[0:2])

# 访问块 df.iloc[n1:n2,m1:m2]:n1到n2-1，m1到m2-1的块
C = df.iloc[0:2,0:2]
print(C)    # DataFrame对象

# 访问某个位置的值 df.at[行名,列名]
D = df.at[0,'name']
print(D)

# 如果使用Series来创建DataFrame，并且指定index的话，必须保证指定的index与每个Series的index一致，否则无法将Series的值赋给DataFrame
df2 = DataFrame({
        'age':Series([26,28,30],index=['first','second','third']),
        'name':Series(['Ken','Ben','Jon'],index=['first','second','third'])}
,index=['first','second','third'])

print(df2)
# 如果使用list作为初始化数据创建DataFrame的话，则python用指定的index和list数据去创建对应的Series
df2 = DataFrame(
        {'age':[22,21,26],
         'name':['Tom','Bark','Jimi']
         },
        index=['first','second','third'])
print(df2)
print(type(df2['age']))

print(df[1:100]) # DataFrame的index超过范围时不会报错，空缺部分而是返回空值，Series则会报错
print(df[1:1])  # 空
print(df[4:1])  # 空
print(df2[0:1])
print(df2['third':'third']) # 通过索引名来获取一行
print(df2['first':'second']) # 通过索引名来获取多行

print(df.columns) # 将列名封装到Index对象中
print(df['age'])
print(df[df.columns[0:1]]) # df.columns[0:1] == 'age'，故上行一样

# 访问块
print(df.iloc[0:1,0:1])
# 访问位置
print(df.at[1,'name'])  # 1是索引
print(df2.at['second','name']) # ’second‘是索引名
#print(df2.at[1,'name'])     # 当有索引名时，不能用索引号访问？？？

# 修改列名
df.columns = ['age2','name2']
print(df)
# 修改行索引
df.index = range(1,4)
print(df)
# 根据行索引删除
df.drop(1,axis=0)   # axis=0：表示行轴，默认值
print(df)
# 根据列名删除
df = df.drop('age2',axis=1) # axis=1：列轴
print(df)
# 第二种删除列的方法
del df['name2']
print(df)   # 虽然为Empty DataFrame，但是仍然还有Index数据
'''
Empty DataFrame
Columns: []
Index: [1, 2, 3]
'''
# 增加列
df['age'] = [2,3,4] # 长度必须与原来的index一致
print(df)
# 增加行：效率低
df2.loc[len(df2)] = [24,'Keno'] # 索引号默认为当前行数-1
print(df2)

# 增加行：合并2个DataFrame
# 使用二维list创建DF，需要提供列名
df3 = DataFrame([[1,2],[3,4]],columns=list('AB'))  # 使用默认index
print(df3)
df4 = DataFrame([[5,6],[7,8]],columns=list('AB')) 
# 简单合并，没有将df4那部分对应的index进行修改，故会存在多个同值的索引号
df5 = df3.append(df4)
print(df5)
# 修改合并后新的DataFrame的index部分，重新索引，索引号唯一
print(df3.append(df4,ignore_index=True))
# =========================DataFrame=========================