# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 15:29:06 2019

类：更多内容
@author: 10841
"""

# 1.构造函数 __init__():对象创建后自动调用，完成对象的初始化工作
# 重写构造函数时，必须调用父类的构造函数
class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print("Aaaah")
            self.hungry = False
        else:
            print("No, thanks")
    def __del__(self): # 析构函数
        print("析构函数__del__在对象被销毁时被调用，因无法知道python何时销毁一个对象，故不推荐使用")
b = Bird()
b.eat()        
b.eat()
   
class SongBird(Bird):
    def __init__(self):
        # 1. 调用未关联的父类构造函数
        Bird.__init__(self) 
        # 通过类调用方法时，没有实例与其关联，故可以随便给self参数传值。这里传入SongBird实例，完成属性绑定
        self.sound = "Squawk"
    def sing(self):
        print(self.sound)

class SongBird2(Bird):
    def __init__(self):
        # 2. 使用函数 super
        super().__init__() 
        ''' 
        super()时super(SongBird2,self)的简写，推荐简写方式
        super()返回的是super对象，它调用的是父类(而非子类)中的方法和属性。
        即使子类有多个超类，也只需调用super一次。
        super对象负责执行方法解析，当调用属性时，将在所有的父类中去寻找
        '''
        self.sound = "Squawk2"
    def sing(self):
        print(self.sound)
    
sb = SongBird()
sb.sing()
sb.eat()

sb2 = SongBird2()
sb2.sing()
sb2.eat()

# 2.协议：通常指规范行为的规则，指定应实现哪些方法以及这些方法应做什么
# 在Java中则是实现了某个接口或者属于特定的类，而python只要求对象遵守特定的
# 协议（行为，即实现了特定的方法），而不要求对象是什么类型，比如要成为序列，遵守序列协议即可
'''
2.1基本的序列和映射协议:实现如下4个方法即可
__len__(self):返回序列的个数，若返回0，则在布尔值的上下文中被当作假
__getitem__(self,key)：返回与key关联的值，key:对list来说是整数值，对映射来说可以是任何类型
__setitem__(self,key,value):仅可变对象需要实现。
__delitem__(self,key)：仅可变对象需要实现。当对象的组成部分使用__del__语句时被调用
'''

# 2.1 下面实现一个无穷序列
def check_index(key):
    '''辅助函数检查序列的索引值是否有效'''
    if not isinstance(key,int):
        raise TypeError
    if key < 0:
        raise IndexError
        
class ArithmeticSequence:
    def __init__(self,start=0,step=1):
        """
        start:序列起始位置的值
        step:2个元素间的间距
        changed:一个字典，保存用户修改后的值
        因为禁止删除元素，故没有实现 __delitem__
        因为是无穷序列，故没有实现 __len__
        """
        self.start = start
        self.step = step
        self.changed = {}
        
    def __getitem__(self,key):
        check_index(key)
        try:
            return self.changed[key] # 如果该key对应的值，是用户修改过的，则直接返回
        except KeyError:
            return self.start + key*self.step # 否则，根据key和step、start直接计算后返回
        
    def __setitem__(self,key,value):
        check_index(key)
        self.changed[key] = value

s = ArithmeticSequence(1,3)
print(s[3])
print(s[2])
print(s[10])
s[3] = 111
print(s[3])

# 2.2 一般可以从list、dict、str派生扩展功能，没必要从头实现
class CounterList(list):
    def __init__(self,*args):
        super().__init__(*args)
        self.counter = 0
    def __getitem__(self,index):
        self.counter += 1
        return super().__getitem__(index)        

cl = CounterList(range(10))
print(cl)
print(cl.reverse())
del cl[3:6]
print(cl.counter)
print(cl[4]+cl[2])
print(cl.counter)

# 3.特性
# 3.1 函数property：创建一个特性
# 特性：通过存取方法定义的属性
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def set_size(self,size):
        self.width, self.height = size
    def get_size(self):
        return self.width, self.height
    # 创建了一个特性并用size关联到这个特性，这样就可以把size当做Rectangle的一个属性来看待了
    size = property(get_size,set_size)
    
# get_size,set_size是假想属性sise的存取方法
r = Rectangle()
r.width = 10
r.height = 5
print(r.size) # 想访问属性一个访问，其值由其他属性计算得到
r.size = 150,100 # 设置时，也会影响到它的源头属性
print(r.width)

# 关于property函数：其返回一个类实例，实现了 __get__,__set__,__delete__任何其一的方法(协议)
# 所以它是一个描述符对象

# 3.2静态方法和类方法
# 3.2.1 类方法：包装在 classmethod对象中,由类似于self的cls参数，cls自动关联到类，可通过类和实例调用
# 3.2.2 静态方法：包装在 staticmethod对象中，没有self和cls参数，通过类或实例来调用
class MyClass:
    def smeth(): # 注意没有self，或者cls参数
        print("this is a static method")
    smeth = staticmethod(smeth)
    
    def cmeth(cls):
        print("This is a class method of ",cls)
    cmeth = classmethod(cmeth)
    
    def imeth(self):
        print("This is a instance method of",self)
    
    
MyClass.cmeth()
MyClass.smeth()
c = MyClass()
c.imeth()
print(c.cmeth) # bound method MyClass.cmeth
print(c.smeth) # function MyClass.smeth:跟普通函数一样，只是其定义在类中（属于类的命名空间范围内），需要使用类或者实例调用
print(c.imeth) # bound method MyClass.imeth
# 现在一般都使用装饰器来声明
# 装饰器：用于包装任何可调用的对象，可用于方法和函数，可指定多个装饰器，使用@运算符列出
class MyClass:
    @staticmethod
    def smeth(): # 注意没有self，或者cls参数
        print("this is a static method")
    @classmethod
    def cmeth(cls):
        print("This is a class method of ",cls)
    
    def imeth(self):
        print("This is a instance method of",self)
