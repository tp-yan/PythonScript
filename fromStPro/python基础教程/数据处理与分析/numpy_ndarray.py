# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:20:46 2019
数据处理工具之Numpy
Numpy:数值计算扩展包，主要用来处理矩阵，运算效率比列表高。
Numpy的数据结构是n维数组对象：ndarray-n dimension array，即本质上是数组对象、对象！
Numpy中的数据对象与MATLAB中的数组很像，同时要求数组中的元素类型必须一致！！！不同于list
@author: tangpeng
"""

import numpy as np # numpy是第三方python库，需要导入

# array()：创建ndarray对象
data1 = np.array([1,2,3,4,5])
print(data1)
data2 = np.array([i*2 for i in range(1,10)])
print(data2)
data3 = np.array((1,2,3,4,5))
print(data3)

# 矩阵：即二维数组
data4 = np.array([[1,2,3],[4,5,6]])
print(data4)
# 查看数组(元素)类型:dtype属性
print(data4.dtype)  # int32

# 转换数组类型:astype()
data5 = data4.astype('str') # 返回新的数组，原数组不改变
print(data5)
print(data5.astype('float'))

# 与matlab一样，数组可进行批量运算，而无需循环
print(data4 + 1)
print(data4 * data4)
print(data4 * 2)

# 访问数组元素、切片、赋值与list类似
print(data4[-1:])
print(data4[-1,-1])

# ndarray对象其他方法：reshape、T转置、ufunc、sort等

input("Press <Ennter>")