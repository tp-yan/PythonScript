# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 20:50:04 2018

@author: tangpeng
"""

#matplotlib是python中最优秀的第三方数据可视化库
#matplotlib库由各种可视化类构成
#matplotlib.pyplot是绘制各类可视化图形的命令子库，相当于快捷方式

import matplotlib.pyplot as plt
import numpy as np
import matplotlib

plt.plot([3,2,4,1,5])   # 若只有一维数据，则被当做Y轴值，X轴值为对应索引值(自动生成)
plt.ylabel('grade')
plt.savefig('test',dpi=600) #保存图片。默认PNG格式，dpi指定图像质量即分辨率
plt.show()

#二维图形
plt.plot([0,2,4,6,8],[3,2,4,1,5])   # 当有两个以上参数时，按照X轴和Y轴顺序绘制数据点
plt.ylabel('Grade')
plt.axis([-1,10,0,6])     #指定X Y轴显示值范围，X:-1~10,Y:0~6
plt.show()

#绘制多个子图
#plt.subplot(nrows, ncols, plot_number): 将绘图区分割为nrows行ncols列的方格
#plot_number指明将要绘制的子图区域。从上往下，从左往右 从1开始编号子绘图区域

def f(t):
    #能量衰减函数
    return np.exp(-t)*np.cos(2*np.pi*t)

a = np.arange(0.0,5.0,0.02)
plt.subplot(2,1,1)   #也可写成subplot(211) 
plt.plot(a,f(a))

plt.subplot(2,1,2)
plt.plot(a,np.cos(2*np.pi*a),'r--')     #破折线绘制
plt.show()

#使用plot绘制多条曲线
#plt.plot(x, y, format_string, **kwargs)
#x:X轴数据，列表或数组，可选.y:Y轴数据，列表或数组 format_string: 控制曲线的格式字符串
#可选**kwargs : 第二组或更多(x,y,format_string)
a = np.arange(10)
plt.plot(a,a*1.5,a,a*3.5,a,a*5.5)   


plt.plot(a,a*1.5,'go-',a,a*3.5,'rx',a,a*5.5,'*',a,a*7.5,'b-.')   
plt.show()

#plot显示中文
#plot默认不支持显示中文
#第一种方法：使用rcParams修改字体实现，它会改变所有绘制的字体格式
matplotlib.rcParams['font.family'] = 'SimHei'   #将字体设置为中文黑体
plt.plot([3,1,4,5,2])
plt.ylabel('纵轴值')
plt.savefig('simhei',dpi=600)
plt.show()

matplotlib.rcParams['font.family'] = 'STSong'   #宋体
matplotlib.rcParams['font.size'] = 20       #字体大小
a = np.arange(0.0,5.0,0.02)
plt.xlabel('横轴：时间')
plt.ylabel('纵轴：振幅')
plt.plot(a.np.cos(2*np.pi*a),'r--')
plt.show()

#第二种方法(推荐)：在有中文输出的地方，增加一个属性：fontproperties，只在使用的地方有效
a = np.arange(0.0,5.0,0.02)
plt.xlabel('横轴：时间',fontproperties='SimHei',fontsize=20)     #只对X轴输出字体有效
plt.ylabel('纵轴：振幅',fontproperties='STSong',fontsize=20)     #只对y轴输出字体有效
plt.plot(a.np.cos(2*np.pi*a),'r--')
plt.show()

#plot的文本显示
a = np.arange(0.0,5.0,0.02)
plt.plot(a,np.cos(2*np.pi*a),'r--')
plt.xlabel('横轴：时间',fontproperties='SimHei',fontsize=15,color='green')   #只对X轴输出字体有效
plt.ylabel('纵轴：振幅',fontproperties='STSong',fontsize=15)                 #只对y轴输出字体有效
plt.title(r'正弦波实例$y=cos(2\pi x)$',fontproperties='SimHei',fontsize=15)  #在整个图形上方显示
plt.text(2,1,r'$\mu=100$',fontsize=15)  # text可以在任意指定坐标绘制文本,$...$:Latex格式文字
plt.axis([-1,6,-2,2])
plt.grid(True)
plt.savefig('text_disp',dip=600)    #必须在show函数之前调用
plt.show()

#annotate：
a = np.arange(0.0,5.0,0.02)
plt.plot(a,np.cos(2*np.pi*a),'r--')
plt.xlabel('横轴：时间',fontproperties='SimHei',fontsize=15,color='green')  #只对X轴输出字体有效
plt.ylabel('纵轴：振幅',fontproperties='STSong',fontsize=15)                #只对y轴输出字体有效
plt.title(r'正弦波实例$y=cos(2\pi x)$',fontproperties='SimHei',fontsize=15) #在整个图形上方显示
plt.annotate(r'$\mu=100$',xy=(2,1),xytext=(3,1.5),arrowprops=dict(facecolor='black',shrink=0.1,width=2))
plt.axis([-1,6,-2,2])
plt.grid(True)
plt.savefig('text_disp_annotate',dip=600)    #必须在show函数之前调用
plt.show()

#自定义绘图子区域
#plt.subplot2grid(GridSpec, CurSpec, colspan=1, rowspan=1)
plt.subplot2grid((3,3),(0,0),colspan=3) # 第一行第一列的方格，扩展宽度占3个方格
plt.subplot2grid((3,3),(1,0),colspan=2) # 第2行第一列的方格，扩展宽度占2个方格
plt.subplot2grid((3,3),(1,2),rowspan=2) # 扩展 高度 占2个方格
plt.subplot2grid((3,3),(2,0))           # colspan rowspan默认为1
plt.subplot2grid((3,3),(2,1))


#更方便的方法：GridSpec类专门用于设置绘图子区域
import matplotlib.gridspec as gridspec

gs = gridspec.GridSpec(3,3)     #将绘制区域化为3x3的网格

ax1 = plt.subplot(gs[0,:])      # 占据/扩展第一行所有列
ax2 = plt.subplot(gs[1,:-1])    #第二行，从第1列至倒数第二列(第2列)
ax3 = plt.subplot(gs[1:,-1])    #第二行至最后一行(第三行)，只占最后一列即第三列
ax4 = plt.subplot(gs[2,0])      # 占第三行第1列
ax5 = plt.subplot(gs[2,1])      # 占第三行第2列




