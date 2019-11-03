import numpy as np

###Array：数组，rank:阶或者维数

a = np.array([1, 2, 3])
print(a)

print(type(a))  # numpy.ndarray
print(a.shape)  # (3,)：一维数组，但是不确定是行还是列数组

a = a.reshape((1, -1))  # 将a改为 1行，列使用占位符-1表示，将根据实际元素来决定列数目
print(a.shape)  # (1, 3)：一行三列的二维数组

a = np.array([1, 2, 3, 4, 5, 6])
print(a.shape)

a = a.reshape((-1, 2))
print(a)
print(a.shape)
a = a.reshape((2, -1))
print(a)
print(a.shape)

a[1, 1] = 55
print(a)

# zeros:元素全为0
a = np.zeros((3, 3))
print(a)

# ones:元素全为1
a = np.ones((2, 3))
print(a)

# full:可指定所有元素值
a = np.full((3, 3), 0)
print(a)

a = np.full((2, 3), 1)
print(a)

# eye:单位矩阵
a = np.eye(4)
print(a)

# random.random:创建随机数组，取值范围0-1
a = np.random.random((3, 4))
print(a)

### indexing
a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]]
             )
print(a.shape)
# 截取子矩阵
print(a[-2:, 1:3])  # 从倒数第二行到最后一行，列：从第一列到第三列（不包括）
print(a[1, -2])  # ():0维数组，即只有一个数

b = a[2, 0:3]
print(b)
print(b.shape)  # (3,):一维数组

b = a[2:3, 1:3]
print(b)
print(b.shape)  # (1, 2):二维数组，对比上面，发现若对某一维度索引取整数，则对应降一维

print(np.arange(3))
print(np.arange(2, 6))  # [2 3 4 5]

a[np.arange(3), 1] += 10  # 将所有行的第二列都加10
print(a)

# 以下操作与上面效果相同
a[np.arange(3), [1, 1, 1]] += 10
print(a)

a[[0, 1, 2], [1, 1, 1]] += 10
print(a)

# 获取a中大于10的所有元素，返回一个相同维度的布尔矩阵
result_index = a > 10
print(result_index)
# 获取符合的元素,，返回一维数组
print(a[result_index])
# 等效操作：
print(a[a > 10])


###元素的数据类型:np自动根据元素类型进行判断
a = np.array([2,3,4])
print(a.dtype)  #int32

a = np.array([1.2,3.3,4,5,6])
print(a.dtype)  #float64

#手动指定dtype
a = np.array([1.2,3.5],dtype=np.int64)  #截断小数点后
print(a)
print(a.dtype)

a = np.array([2.2,7.8])
b = np.array(a,dtype=np.int32)
print(b)
print(b.dtype)


###数学运算
a = np.array([[1,2],
              [3,4]])
b = np.array([[5,6],
              [6,5]])

print(a+b)  #相对应元素相加
print(np.add(a,b))  #等价操作

print(a-b)  #类似的
print(np.subtract(a,b))

print(a*b)  #对应元素相乘
print(np.multiply(a,b))

print(a/b)  #对应相除
print(np.divide(a,b))

print(np.sqrt(a))   #每个元素都开方

b = np.array([[1,2,3],
              [4,5,6]])
print(a.dot(b)) #矩阵乘法 2x2 * 2x3
print(np.dot(a,b))


###常用函数
#sum
print("sum\n",a)
print(np.sum(a))    #将所有元素求和
print(np.sum(a,axis=0)) #将列元素求和
print(np.sum(a,axis=1)) #将行元素求和

#mean:和的均值
print(np.mean(a))
print(np.mean(a,axis=0))
print(np.mean(a,axis=1))

#uniform：生成指定范围内的小数
print(np.random.uniform(3,4))
print(np.random.uniform(5,10))

#tile:将矩阵元素在行或列上重复
print(np.tile(a,(1,2))) #在行上不重复，列上重复两次
print(np.tile(a,(2,1))) #在行上重复2此，列上不重复
print(np.tile(a,(2,3))) #行重复2次，列重复3次

#argsort：排序
a = np.array([[3,6,4,10],
              [5,1,7,11]])
print(a.argsort())  #将每行元素按从小到大排序，输出是排序下标
print(a.argsort(axis=0))  #将每列元素按从小到大排序，输出是排序下标

#矩阵转置
print(a.T)
print(np.transpose(a))


###广播
a = np.array([[1,2,3],
              [2,3,4],
              [12,31,22],
              [2,2,2]])
b = np.array([1,2,3])

for i in range(4):
    a[i,:] += b #将a每一行元素加上b
print(a)
#循环在python中执行效率低

#使用tile函数实现
print(a + np.tile(b,(4,1)))

#使用广播实现
print(a + b)    #直接将不同维度的矩阵/数组相加，np会将数组自动转换为相同维度


