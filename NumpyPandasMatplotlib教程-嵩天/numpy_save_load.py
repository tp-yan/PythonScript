# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 20:44:05 2018

@author: tangpeng
"""

import numpy as np
a = np.arange(100).reshape(5,20)
#np.savetxt(frame, array, fmt='%.18e', delimiter=None)
#• frame : 文件、字符串或产生器，可以是.gz或.bz2的压缩文件
#• array : 存入文件的数组
#• fmt : 写入文件的格式，例如：%d %.2f %.18e
#• delimiter : 分割字符串，默认是任何空格
np.savetxt('a.csv',a,fmt="%d",delimiter=',')    # savetxt()不止用来生成 csv文件，也可以是其他文件
np.savetxt('a1.csv',a,fmt="%.1f",delimiter=',')
#加载 csv文件
#np.loadtxt(frame, dtype=np.float, delimiter=None， unpack=False)
#• frame : 文件、字符串或产生器，可以是.gz或.bz2的压缩文件
#• dtype : 数据类型，可选
#• delimiter : 分割字符串，默认是任何空格
#• unpack  : 如果True，读入属性将分别写入不同变量
np.loadtxt('a.csv',delimiter=',')

#多维数据的存取
a = np.arange(100).reshape(5,10,2)
a.tofile("b.dat",sep=",",format="%d")   # 数据写入文件后，维度信息丢失
# sep数据分割字符串，如果是空串，写入文件为二进制
#• format : 写入数据的格式
a.tofile("b1.dat",format="%d") 
#读取数据 fromfile():需要与 tofile()配合使用，使用fromfile需要知道数组的维度与类型以及分隔符信息
c = np.fromfile("b.dat",dtype=np.int,sep=",").reshape(5,10,2)
c
d = np.fromfile("b1.dat",dtype=np.int).reshape(5,10,2)
d

#必须基于numpy自定义的数据格式
# save() 扩展名.npy  savez() 压缩扩展名.npz
a = np.arange(100).reshape(5,10,2)
np.save("a.npy",a)  #以二进制形式存储，但文件头存储了数据的元信息(维度、类型)
b = np.load("a.npy")
b

#save load：适合程序数据缓存
#与其他程序进行数据交互，tofile fromfile savetxt loadtxt较适合

# numpy的随机数函数
# python中的rand库：标量的随机函数
# numpy的random子库：为数组提供随机功能
a = np.random.rand(3,4,5)
sn = np.random.randn()

