#第一步是导入Tkinter包的所有内容：
from tkinter import *

#第二步从Frame派生一个Application类，这是所有Widget的父容器：
import  tkinter.messagebox  as messagebox


class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self,text="Hello",command=self.hello)
        self.alertButton.pack()
        '''
        self.helloLabel = Label(self,text="Hello,World!")
        self.helloLabel.pack()
        self.quitButton = Button(self,text="Quit",command=self.quit)
        self.quitButton.pack()
        '''

    def hello(self):
        name = self.nameInput.get() or "world"
        messagebox.showinfo("Message","Hello,%s" % name)

#在GUI中，每个Button、Label、输入框等，都是一个Widget。Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树。
#pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局。
#在createWidgets()方法中，我们创建一个Label和一个Button，当Button被点击时，触发self.quit()使程序退出。
#第三步，实例化Application，并启动消息循环：
app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()
#GUI程序的主线程负责监听来自操作系统的消息，并依次处理每一条消息。因此，如果消息处理非常耗时，就需要在新线程中处理。

# 输入文本
# 我们再对这个GUI程序改进一下，加入一个文本框，让用户可以输入文本，然后点按钮后，弹出消息对话框。
