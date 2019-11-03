# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 11:44:09 2019

标准库之Tkinter：创建GUI程序
@author: 10841
"""

from tkinter import *

btn = Button() # 若没有Tk实例，则创建控件时会创建Tk实例
btn.pack() # 创建控件后需要使用布局管理器设置控件位置，否则控件不可见
btn['text'] = 'Click me!' # 通过控件属性来修改外观和行为
def clicked():
    print("I was clicked!")
btn['command'] = clicked # 设置点击事件处理函数
# 同时设置多个属性
btn.config(text='Click me!',command=clicked)
btn2 = Button(text="Click me too!",command=clicked).pack()

Label(text="I'm in the first window!").pack() # 控件第一个参数指定其父控件
# pack将控件默认放于主窗口中，居中排列成一列

second = Toplevel() # 创建新窗口，也是顶级窗口
Label(second,text="I'm in the second window!").pack()

# 布局管理器除了pack还有：grid和place

# 事件处理
# 按钮的 command属性是一种特殊的事件处理
# 控件方法bind：将指定事件与处理函数绑定
def callback(event):
    print(event.x,event.y)
    
second.bind('<Button-1>',callback) # 事件 '<Button-1>' 代表鼠标左键单击

'''
top = Tk() # 创建顶级控件,充当主窗口
'''

from tkinter.scrolledtext import ScrolledText

# 加载已存在的文件并显示其内容
def load():
    with open(filename.get()) as file:
        contents.delete("1.0",END) # 1.0:第一行第0个字符，即第一个字符前面。END：文本末尾
        contents.insert(INSERT,file.read()) # INSERT：当前插入点
        
def save():
    with open(filename.get(),'w') as file:
        file.write(contents.get('1.0',END))

editor = Toplevel()
editor.title("Simple Editor")

contents = ScrolledText(editor) # 可滚动多行文本输入区域
contents.pack(side=BOTTOM,expand=True,fill=BOTH)

filename = Entry(editor) # 单行文本输入区
filename.pack(side=LEFT,expand=True,fill=X) # 靠左，随父控件缩放，在水平方向上填充

Button(editor,text='Open',command=load).pack(side=LEFT)
Button(editor,text='Save',command=save).pack(side=LEFT)

mainloop() # 启动GUI,进入Tkinter主事件循环 
        