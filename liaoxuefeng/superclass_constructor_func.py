# -*- coding: utf-8 -*-
"""
调用父类构造函数的2种方法
"""

class Bird:
    # 构造函数
    def __init__(self,name):
        self.name = name
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('Aaah..')
            print(self.name)
            self.hungry = False
        else:
            print('No, thanks!')
        
# 1. 使用函数super()调用父类构造函数,super()返回的是super对象，调用方法时，其调用的是父类的方法
# super对象负责执行方法解析，访问它的属性时，它将在所有的超类中去寻找。另外。super会自动解决多继承初始化问题
class SongBird(Bird):
    def __init__(self):
        # super() 是 super(SongBird,self)的缩写，其调用的__init__()必须与父类构造函数一致
        super().__init__("Base Bird") # 必须使用 super对象 显示调用父类的构造函数
        self.sound = "Squawk"
    def sing(self):
        print(self.sound)

sb = SongBird()
sb.sing()
sb.eat()
sb.eat()

# 2. 调用未关联的父类构造函数
class SongBird2(Bird):
    def __init__(self):
        # 通过类调用方法时，因为实例与其相关联，故可以随意设置参数self，这样的方法称为未关联的
        # 这相当于在父类构造函数中为 SongBird2对象添加属性 hungry和 name
        Bird.__init__(self,'XiNiao') # 必须显示调用父类构造函数
        self.sound = 'ABc'
    def sing(self):
        print(self.sound)
        
sb = SongBird2()
sb.sing()
sb.eat()
sb.eat()