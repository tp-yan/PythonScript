# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 21:51:00 2018

@author: tangpeng
"""

#绘制引力波

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile  

#产生时间序列
#从配置文档中读取时间相关数据
rate_h,hstrain = wavfile.read(r"H1_Strain.wav","rb")
rate_l,lstrain = wavfile.read(r"L1_Strain.wav","rb")

reftime,ref_H1 = np.genfromtxt("wf_template.txt").transpose()

#读取应变数据
htime_interval = 1/rate_h               #波形的时间间隔
ltime_interval = 1/rate_l
 
htime_len = hstrain.shape[0]/rate_h     # hstrain：数据矩阵。shape[0]：一维数据长度
htime = np.arange(-htime_len/2,htime_len/2,htime_interval) # 绘制关于坐标原点对称图形
ltime_len = lstrain.shape[0]/rate_l
ltime = np.arange(-ltime_len/2,ltime_len/2,ltime_interval)

#使用来自H1探测器的数据作图
fig = plt.figure(figsize=(12,6))    #创建一个大小为12*6的绘图空间
plth = fig.add_subplot(221)         #在fig中划分子绘制区域
plth.plot(htime,hstrain,'y')
plth.set_xlabel('Time(Seconds)')
plth.set_ylabel('H1 Strain')
plth.set_title('H1 Strain')

#绘制L1 Strain & Template
pltl = fig.add_subplot(222)
pltl.plot(ltime,lstrain,'g')
pltl.set_xlabel('Time(Seconds)')
pltl.set_ylabel('L1 Strain')
pltl.set_title('L1 Strain')

pltref = fig.add_subplot(212)
pltref.plot(reftime,ref_H1)
pltref.set_xlabel('Time(Seconds)')
pltref.set_ylabel('Template Strain')
pltref.set_title('Template')

fig.tight_layout()      #自动调整图像外部边缘
plt.savefig('gravitational_wave.png')
plt.show()
plt.close(fig)

