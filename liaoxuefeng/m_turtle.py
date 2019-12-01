#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 22:03:36 2019

@author: tangpeng

海龟绘图（Turtle Graphics）通过编程指挥一个小海龟（turtle）在屏幕上绘图。
Python内置了turtle库，基本上100%复制了原始的Turtle Graphics的所有功能。
"""


# 1.指挥小海龟绘制一个长方形的简单代码：
from turtle import *

def draw_rectangle():
    # 设置笔刷宽度:
    width(4)
    # 前进:
    forward(200)
    # 右转90度:
    right(90)
    # 笔刷颜色:
    pencolor('red')
    forward(100)
    right(90)
    
    pencolor('green')
    forward(200)
    right(90)
    
    pencolor('blue')
    forward(100)
    right(90)
    
    # 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
    done()

# 2.turtle包本身只是一个绘图库，但是配合Python代码，就可以绘制各种复杂的图形。例如，通过循环绘制5个五角星：
def drawStar(x,y):
    pu()
    goto(x,y)
    pd()
    # set heading: 0
    seth(0)
    for i in range(5):
        fd(40)
        rt(144)

def draw_5_star():
    for x in range(0,250,50):
        drawStar(x,0)
    
    done()
    
#draw_5_star()

# 3.使用递归，可以绘制出非常复杂的图形。例如，下面的代码可以绘制一棵分型树：

# 设置色彩模式是RGB:
colormode(255)

lt(90)

lv = 14
l = 120
s = 45

width(lv)

# 初始化RGB颜色:
r = 0
g = 0
b = 0
pencolor(r, g, b)

penup()
bk(l)
pendown()
fd(l)

def draw_tree(l, level):
    global r, g, b
    # save the current pen width
    w = width()

    # narrow the pen width
    width(w * 3.0 / 4.0)
    # set color:
    r = r + 1
    g = g + 2
    b = b + 3
    pencolor(r % 200, g % 200, b % 200)

    l = 3.0 / 4.0 * l

    lt(s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    rt(2 * s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    lt(s)

    # restore the previous pen width
    width(w)

def drawTree():
    
    speed("fastest")
    
    draw_tree(l, 4)
    
    done()
    
drawTree()