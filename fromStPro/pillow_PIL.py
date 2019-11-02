# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 08:56:11 2018

@author: tangpeng
"""

#使用 PIL库

from PIL import Image

import numpy as np

#图像的数组表示
dirPath = "./image/"
imgName_1 = "2.jpg"

im = np.array(Image.open(dirPath+imgName_1)) # 读入图像，并将其转换为数组
print(im.shape,im.dtype)    #图像是一个三维数组，维度分别是高度、宽度和像素RGB值

#图像的变换
b = [255,255,255] - im  # 对RGB的图像变换
im_new = Image.fromarray(b.astype('uint8'))
im_new.save(dirPath+imgName_1.split(sep='.')[0]+"_new."+imgName_1.split(sep='.')[1])

imgName_2 = "3.jpg"
a = np.array(Image.open(dirPath+imgName_2).convert('L'))    #彩色图转为灰度图
b = 255 - a
im = Image.fromarray(b.astype('uint8'))
im.save(dirPath+imgName_2.split(sep='.')[0]+"_new."+imgName_2.split(sep='.')[1])

imgName_3 = "4.jpg"
a = np.array(Image.open(dirPath+imgName_3).convert('L'))    #彩色图转为灰度图
b = (100/255)*a + 150   #区间变换
im = Image.fromarray(b.astype('uint8'))
im.save(dirPath+imgName_3.split(sep='.')[0]+"_new."+imgName_3.split(sep='.')[1])

imgName_4 = "5.jpg"
a = np.array(Image.open(dirPath+imgName_4).convert('L'))    #彩色图转为灰度图
b = 255*(a/255)**2   #像素平方
im = Image.fromarray(b.astype('uint8'))
im.save(dirPath+imgName_4.split(sep='.')[0]+"_new."+imgName_4.split(sep='.')[1])

#实现图像的手绘效果
imgName_6 = "7.jpg"
a = np.array(Image.open(dirPath+imgName_6).convert('L')).astype('float')    #二维数组
#手绘风格：在灰度图像上由立体与明暗效果叠加而成
#灰度：图像的明暗程度，梯度：灰度的变化率
#立体效果由添加虚拟深度值来实现
depth = 10.0    #取值范围0-100
grad = np.gradient(a)
grad_x,grad_y = grad  #得到x，y方向的梯度值
grad_x = grad_x*depth/100.   # 除以100对深度值归一化 grad_x*depth：添加深度值对梯度的影响
grad_y = grad_y*depth/100.
A = np.sqrt(grad_x**2+grad_y**2+1.)
uni_x = grad_x/A
uni_y = grad_y/A
uni_z = 1./A

vec_el = np.pi/2.2  #光源的俯视角度，弧度制
vec_az = np.pi/4.   #光源的方位角度，弧度制
dx = np.cos(vec_el)*np.cos(vec_az)  #光源对x轴的影响
dy = np.cos(vec_el)*np.sin(vec_az)  #光源对y轴的影响
dz = np.sin(vec_el)                 #光源对z轴的影响

b = 255*(dx*uni_x+dy*uni_y+dz*uni_z)    #光源归一化
b = b.clip(0,255)   # 截断0-255以外的数
im = Image.fromarray(b.astype('uint8'))
im.save(dirPath+imgName_6.split(sep='.')[0]+"_new."+imgName_6.split(sep='.')[1])


