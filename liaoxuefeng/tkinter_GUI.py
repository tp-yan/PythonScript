#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 21:17:09 2019

@author: tangpeng

Python自带的库是支持Tk的Tkinter，使用Tkinter进行GUI编程。
Tkinter封装了访问Tk的接口；
Tk是一个图形库，支持多个操作系统，使用Tcl语言开发；
Tk会调用操作系统提供的本地GUI接口，完成最终的GUI。
所以，我们的代码只需要调用Tkinter提供的接口就可以了。

"""

# 1.编写一个GUI版本的“Hello, world!”
# 第一步是导入Tkinter包的所有内容：
from tkinter import *

# 第二步是从Frame派生一个 MyApplication 类，Frame是所有Widget的父容器：
# 在GUI中，每个Button、Label、输入框等，都是一个Widget。
# Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树。
class MyApplication(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master) #不能使用 super().
        self.pack() # pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局。
        self.createWidgets()
        
    def createWidgets(self):
        self.helloLabel = Label(self,text="Hello, world!")
        self.helloLabel.pack()
        self.quitButton = Button(self,text="Quit",command=self.quit)
        self.quitButton.pack()

def app1():
    # 第三步，实例化MyApplication，并启动消息循环：
    app = MyApplication()
    # 设置窗口标题:
    app.master.title("hello,world!")
    # 主消息循环:
    app.mainloop()
    #GUI程序的主线程负责监听来自操作系统的消息，并依次处理每一条消息。因此，如果消息处理非常耗时，就需要在新线程中处理。

# 2.加入一个文本框，让用户可以输入文本，然后点按钮后，弹出消息对话框
import tkinter.messagebox as messagebox
class InputApp(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    
    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self,text="Hello",command=self.hello)
        self.alertButton.pack()
        
    def hello(self):
        # 通过self.nameInput.get()获得用户输入的文本后
        name = self.nameInput.get() or "world"
        # 使用tkMessageBox.showinfo()可以弹出消息对话框
        messagebox.showinfo('Message','Hello,%s' % name)
        
def app2():
    app = InputApp()
    app.master.title("Hello World")
    app.mainloop()
    
app2()