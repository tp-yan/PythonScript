# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 20:37:54 2018

@author: tangpeng
"""

#matplotlib的基础图表绘制函数

#plt.plot():坐标图
#plt.boxplot():箱型图
#plt.bar():条形图
#plt.barh():横向条形图
#plt.polar():极坐标图
#plt.pie():饼图
#plt.psd():功率谱密度图
#plt.specgram():谱图
#plt.cohere():X-Y相关性函数
#plt.scatter():散点图
#plt.step():步阶图
#plt.hist():直方图
#plt.contour():等值图
#plt.vlines():垂直图
#plt.stem():柴火图
#plt.plot_date():数据日期

import numpy as np
import matplotlib.pyplot as plt

#绘制饼图
labels = 'Fogs','Hogs','Logs','Dogs'
sizes = [20,10,40,50]       # 自动归一化为100%
explode = (0.1,0,0.15,0)    # 饼图突出比例
plt.pie(sizes,explode=explode,labels=labels,autopct="%1.1f%%",shadow=False,startangle=90)
#autopct:设置饼图数据的显示格式
#shadow：饼图是否有阴影
#startangle:起始角度
plt.axis('equal')   # 绘制饼图时，XY轴尺寸一样。否则绘制的是扁的饼图
plt.show()

#绘制直方图
np.random.seed(0)                           #设置随机种子
mu, sigma = 100,20                          #均值与标准差
a = np.random.normal(mu,sigma,size=100)     #生成100个服从正态分布的随机数

plt.hist(a,20,normed=1,histtype='stepfilled',facecolor='b',alpha=0.75)
#第二个参数bin=20：将a中的最小值至最大值区间等分为20份，然后计算落到每份的个数，所以绘制的图有20根柱子
#normed=1：将纵轴个数归一化为 概率值
plt.title('Histogram-20')
plt.show()

plt.hist(a,40,normed=1,histtype='stepfilled',facecolor='b',alpha=0.75)
plt.title('Histogram-40')
plt.show()

#绘制极坐标图
#面向对象绘制极坐标
N = 20  #绘制极坐标图的个数
theta = np.linspace(0.0,2*np.pi,N,endpoint=False)   # 产生N个极坐标角度
radii = 10*np.random.rand(N)                        # N个元素的一维数组
width = np.pi/4*np.random.rand(N)                   #扇形的宽度
ax = plt.subplot(111,projection='polar')            #得到一个绘制极坐标的对象
bars = ax.bar(theta,radii,width=width,bottom=1.0)   #前三个参数分别对应left height width

for r,bar in zip(radii,bars):   #设置每个极坐标的颜色与透明度
    bar.set_facecolor(plt.cm.viridis(r/10.))
    bar.set_alpha(0.5)
    
plt.show()

#散点图
#使用面向对象的方法绘制散点图,推荐方法
fig, ax = plt.subplots()
ax.plot(10*np.random.randn(100),10*np.random.randn(100),'o')
ax.set_title('Simple Scatter')
plt.show()
