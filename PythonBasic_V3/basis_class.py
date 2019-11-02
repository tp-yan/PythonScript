# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 09:26:43 2019

类
@author: 10841
"""

# 1.类定义本质
class MyClass:
    name = "python"     # 这里属于类属性
    # 类定义中不仅仅只能有def语句，还可以是任何其他python语句，因为类定义其实就是作为
    # 一段代码段在类的命名空间中执行，故类中定义的都属于这个命名空间中
    print("class:MyClass is being defined")
    def method1(self): # 方法与函数的区别就是这个self参数，对象调用方法时，总是将自己
        # 传给方法的第一个参数，而且这个参数可以是任何名称，不一定是self，但习惯用self
        print(self)
        print("method1")
    
    def method2(myself): # 同时，方法实际上可看作是关联到函数的属性，可以指向外部的函数
        # 但外部函数就无法获得 self参数，也就无法访问对象的属性
        print(myself)
        print("method2")
    
    # 约定俗成：
    # 以2个下划线开头的方法作为private方法
    def __private_method(self): 
        print("实际上，Python是无法阻止别人访问对象的私有方法和属性的")
        print("private方法：名称被转换成：_类名方法名")
    
    def _not_protected_method(self):
        print("一个下划线开头的方法并不是protected方法，只是普通方法，名称不会被转换")

def function1(self): # 类外的函数，即使有参数，被
    print(self)
    print("function1")
    

    
p1 = MyClass()
p2 = MyClass()
print(MyClass.name)
print(p1.name)
MyClass.name = "Java"
print(p2.name)

p1.method1()
p1.method2()
p1.method2 = function1
p1.method2("外部函数，无法获得self对象自身")

# 2.给实例绑定与类属性同名的属性，则将覆盖类属性
p1.name = "p1's name not class's"
print(p1.name)

# 3.从外部访问私有方法
p1._MyClass__private_method()
p1._not_protected_method()

# 4.继承
class Filter:
    def init(self):
        self.blocked = []
        
    def filter(self,sequence):
        return [x for x in sequence if x not in self.blocked]
    
class SPAMFilter(Filter): # 继承自 Filter类，继承父类所有方法
    def init(self): # 重新父类方法
        self.blocked = ['SPAM']

f = Filter()
f.init()
print(f.filter([1,2,3,4])) # Filter实际不过滤序列，只用于作为基类
s = SPAMFilter()
s.init()
print(s.filter(['SPAM','Mars','Spark','SPAM','SPAM','Flower']))


# 5. 与类关系相关的函数
print(issubclass(SPAMFilter,Filter)) # 一个类是否为另一个类的子类
print(SPAMFilter.__base__) # 查看类的父类
print(SPAMFilter.__bases__) # 查看类的所有父类
print(Filter.__base__) # __base__属性：查看类的直接父类
print(isinstance(s,SPAMFilter)) # 对象是否类的实例
print(isinstance(s,Filter))
print(isinstance(s,str))
print(s.__class__) # __class__属性：对象所属类
print(f.__class__) # __class__属性：对象所属类

# 6.多继承：应避免使用多继承
class Calculator:
    def calculate(self,expression):
        self.value = eval(expression) # 给self对象动态绑定属性
class Talker:
    def talk(self):
        self.name = "talker"
        print("Hi, my value is ",self.value) # 访问self.value之前，必须保证self已有该属性
class TalkingCalculator(Calculator,Talker): #若超类中存在同名方法，则左边的类覆盖右边类的方法
    pass

tc = TalkingCalculator()
tc.calculate("1+2*10")
tc.talk()
print(TalkingCalculator.__bases__) # 所有父类
print(tc.__class__)
print(type(tc)) # 与访问 __class__ 属性一样，返回对象所属类
    
# 7.其他与类相关函数
# hasattr：查看对象是否具有某个属性(方法也是一种属性)
print(hasattr(tc,'talk'))
print(hasattr(tc,'going'))
# getattr
print(getattr(tc,'talk',None))
print(getattr(tc,'name',None)) # 有该属性则返回，无返回默认值None
print(getattr(tc,'going',None))
# callable:检查属性是否可调用
print(callable(getattr(tc,'talk',None)))
print(callable(getattr(tc,'name',None)))
# setattr:与getattr相反
setattr(tc,'age',20)
setattr(tc,'__money',100) # 设置私有属性 
print(tc.age)
# __dict__ 属性：查看对象中的所有值
print(tc.__dict__)
print(tc.__dict__['__money']) # 变相取私有属性

# 8.抽象基类，即如同Java中的interface
# 抽象基类：用于指定子类必须提供哪些功能，自身却不实现这些功能
# 需要引入 abc模块才能定义抽象基类
from abc import ABC, abstractmethod

class NewTalker(ABC):
    @abstractmethod     # 形如@this的称为 装饰器。@abstractmethod用于将方法标记为抽象的
    def talk(self):
        pass
class Knigget(NewTalker): # 若子类也不实现 抽象方法则还是抽象类，也不能实例化对象
    pass
class KniggetReal(NewTalker):
    def talk(self):
        print("Ni!")
k = KniggetReal() 
print(isinstance(k,NewTalker))
k.talk()
   
print(type(ABC))
print(ABC.__base__)

# 鸭子类型：只要实现了 talk方法，就是Talker的子类
class Herring:
    def talk(self):
        print("Blub.")
h = Herring()
print(isinstance(h,NewTalker))
# 若Herring是从别人的模块中导入的，那么就无法将其继承自 NewTalker
# 但是又想让程序把它当做NewTalker的子类。解决方法：将Herring注册为 NewTalker
# 这样所有的Herring对象都将被视为NewTalker对象
NewTalker.register(Herring)
print(isinstance(h,NewTalker))
print(issubclass(Herring,NewTalker))
# 但是注册成为子类，并不要求该子类有其基类的所有方法，因为仅仅是注册了，但实际上并没有
# 实现继承，得到父类的所有方法，如下
class Clam:
   pass
NewTalker.register(Clam)
c = Clam()
print(isinstance(c,NewTalker)) 
#c.talk() # 实际上c并没有NewTalker的方法

# 注：应将 isinstance返回True视为一种意图表达

# 9.random.choice:随机返回序列中的一个元素，类似dict的popitem
import random
print(random.choice("abcdf"))
print(random.choice(list(range(10))))
