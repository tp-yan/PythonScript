# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 15:09:19 2018

@author: tangpeng
"""
#高维数据：不同于多维数据，键值对的形式
#在python中 高维数据用dict或者数据表示格式（JSON、XML等）
# ndarray--即数组，N维数组对象
#数组对象可以去掉循环运算，将一维数据看成一个对象
#ndarray包含：实际的数据+描述数据的元数据（数据维度、类型）
#numpy可以完成批量操作

#ndarray类型的
# 轴axis:保存数据的维度
# 秩rank:轴/维的数量


import numpy as np

def npSum():
    a = np.array([0,1,2,3,4])   #生成一个ndarray数组，array是ndarray的别名
    b = np.array([9,8,7,6,5])
    c= a**2 + b**3;
    return c

print(npSum())

a = np.array([[1,2,3,4,5],
              [10,9,8,7,6]])
#ndarray的属性
print(a.ndim)   # a的维数
print(a.shape)  # 对象的尺度,shape对象时tuple类型
print(a.size)   # 数组所有元素个数
print(a.dtype)  #元素类型  complex64:实部、虚部都为32浮点数
print(a.itemsize)   #单个元素的大小

# x = np.array(list/tuple,dtypr=np.float32) #由python的list、tuple生成ndarray类型
#使用NumPy中函数创建 ndarray数组. eyes()、ones()、zeros():默认是浮点数
a = np.arange(10)   #与python的range()类似，生成0~9
b = np.ones((3,6))  #传入的参数为 shape
c = np.zeros((3,6),dtype=np.int32)
d = np.eye(5)
x = np.ones((2,3,4))    # 多维数据
y = np.full((3,2),7)    #生成指定值的数组
print("\n","\n",a,"\n",b,"\n",c,"\n",d,"\n",x,"\n",y)
print(x.shape)
np.zeros_like(a)
np.ones_like(d)
np.full_like(b,2)
np.linspace(1,10,4) # 从1~10,4：元素个数，默认浮点数
np.linspace(1,10,4,endpoint=False) #重视元素不作为数组元素,endpoint默认为True
np.concatenate((b,c))   #将2或多个个同型的数组合并生成新的数组

#ndarray数组的维度变换
a = np.ones((2,3,4),dtype=np.int32)
a.reshape((3,8))    #reshape返回一个新的数组，元素个数与原数组相同
a.resize((3,8))     #与reshape一样但是修改原数组尺度
b = a.flatten()     #将a降维成一维数组,a不变

#改变ndarray数组的类型
a = np.ones((2,3,4),dtype=np.int)   #int具体是几位，由编译器根据数据再决定
b = a.astype(np.float) #返回新的数组，np.float:指定为浮点类型，同np.int代表一类数据类型
# ndarray --> list
a = np.full((2,3,4),25,dtype=np.int32)
b = a.tolist()  # 转换成python 中的list类型

#数组的索引与切片
#一维数据的索引与切片
a = np.array([9,8,7,6,5])
a[2]        #数组索引，与python的list索引一样
a[1:4:2]    #数组切片。从1~4(不含)，步长为2递增，返回一个 array对象
#二维数据的索引与切片
a = np.arange(24).reshape((2,3,4))
#索引
a[1,2,3]
a[0,1,2]
a[-1,-2,-3]
#切片
a[:,1,-3]   #不考虑第一个维度，即所有第一维度的数据
a[:,1:3,:]  #每个维度的切片方法
a[:,:,::2]  # 第三个维度要求获得所有数据，但以步长为2跳跃切片

#ndarray的运算
#数组与标量的运算：每个元素与标量运算
a = np.arange(24).reshape((2,3,4))
a.mean()    # 所有元素的平均值
a = a/a.mean()
np.square(a)

