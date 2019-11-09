#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 18:56:04 2019

@author: 10841

第三方库Pillow：Python平台事实上的图像处理标准库
"""

# 1.图像缩放
from PIL import Image

# 打开一个jpg图像文件
im = Image.open("test.jpeg")
# 获得图像尺寸:
w,h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w//2,h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save("test_thumbnail.jpg","jpeg")

# 2.图像模糊
from PIL import ImageFilter
im = Image.open("test.jpeg")
# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save("test_blur.jpg","jpeg")

# 3.绘图
from PIL import ImageDraw,ImageFont
import random 

# 随机字母:
def rndChar():
    return chr(random.randint(65,90))

# 随机颜色1:较浅色，作为背景色
def rndColor1():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

# 随机颜色2:颜色更深，作为字母颜色
def rndColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

# 生成字母验证码
def geneValidateCode():
    # 矩形框宽高 240 x 60:
    width = 60*4
    height = 60
    image = Image.new("RGB",(width,height),(255,255,255)) # 创建纯白色的图片用于绘制
    # 创建Font对象:
    font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf',36)
    #创建Draw对象，才能在图像上进行绘制
    draw = ImageDraw.Draw(image)
    #填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x,y),fill=rndColor1()) # 填充背景色
    # 输出文字:
    for t in range(4):
        draw.text((60*t+10,10),rndChar(),font=font,fill=rndColor2())
        
    # 模糊:
    image = image.filter(ImageFilter.BLUR)
    image.save("test_code.jpg","jpeg")
    image.show() # 调用本地默认图片软件查看
    
geneValidateCode()