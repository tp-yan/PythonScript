import math
from numpy import *
import numpy as np
import matplotlib.pyplot as plt

# 求高度
z = []
for i in range(1, 11):
    z.append(0.025 * (math.exp(0.5 * (i - 0.5)) - 1))

# 求c(10,n+1)
c = np.zeros(shape=(10, 1))
c[7][0] = 1

# 扩散系数D=0.001，时间步长为1年
D = 0.001
dt = 1

# 先对A进行赋值
A = np.zeros(shape=(10, 10))
A[0, 0] = 1 + 2 * D * dt / (z[1] - z[0]) / (z[0] + z[1])
A[0, 1] = -2 * D * dt / (z[1] - z[0]) / (z[0] + z[1])

for i in range(1, 9):
    A[i, i - 1] = -2 * D * dt / (z[i] - z[i - 1]) / (z[i + 1] - z[i - 1])
    A[i, i] = 1 + 2 * D * dt / (z[i + 1] - z[i - 1]) * (1 / (z[i + 1] - z[i]) + 1 / (z[i] - z[i - 1]))
    A[i, i + 1] = -2 * D * dt / (z[i + 1] - z[i]) / (z[i + 1] - z[i - 1])
A[9, 8] = -D * dt / pow((z[9]) - z[8], 2)
A[9, 9] = 1 + D * dt / pow((z[9] - z[8]), 2)

# 将list转为矩阵形式
c_matrix = mat(c)
A_matrix = mat(A)
# print(A_matrix.I)

# 时间循环
for i in range(1000):
    col_data = A_matrix.I * c_matrix[:, i]
    c_matrix = np.column_stack((c_matrix, col_data))
    if i < 3:
        print(c_matrix)

# 画图
c = c_matrix
y0 = c[:, 0]
y1 = c[:, 100]
y2 = c[:, 200]
y3 = c[:, 300]
y4 = c[:, 400]
y5 = c[:, 500]
y6 = c[:, 600]
y7 = c[:, 700]
y8 = c[:, 800]
y9 = c[:, 900]
y10 = c[:, 1000]

# figure：使用默认参数 创建一个绘图窗口 等效于：figure(1)
plt.plot(z,y0,label='Initial')
plt.plot(z,y1,label='100 year')
plt.plot(z,y2,label='200 year')
plt.plot(z,y3,label='300 year')
plt.plot(z,y4,label='400 year')
plt.plot(z,y5,label='500 year')
plt.plot(z,y6,label='600 year')
plt.plot(z,y7,label='700 year')
plt.plot(z,y8,label='800 year')
plt.plot(z,y9,label='900 year')
plt.plot(z,y10,label='1000 year')
plt.legend()    # 显示label
plt.show()
