# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 22:46:01 2019

@author: tangpeng
"""

# 1. 手工包装 静态和类方法
class MyClass:
    """    
    静态方法其实就是一个放在类中定义的函数function，与类和实例都未关联，可从外部
    通过类和实例直接访问，实际上与类没有关系。
    静态方法一调用，其内存地址就确定了，无论从哪里调用都一样
    """
    def smeth(): # 静态方法没有 self 参数.
        print('this is a static method')
    smeth = staticmethod(smeth) # 将 smeth方法包装成静态方法
    
    """
    类方法是与类关联的方法，通过实例调用，其实也是通过类调用的。
    类方法一调用，其内存地址就确定了，无论类还是实例调用都一样
    """
    def cmeth(cls): # 类方法有 cls 参数 代表其所属类
        print('this is a class method of',cls)
    cmeth = classmethod(cmeth)

# 2. 使用装饰器代替手工包装
class MyClass2:
    @staticmethod
    def smeth(param):
        print('this is a static method, %s' % param) # 就是上述过程的简写
    
    @classmethod
    def cmeth(cls):
        print('this is a class methodof',cls)

print(MyClass.smeth) # <function MyClass.smeth at 0x000002061C9FBA60>
MyClass.smeth()
print(MyClass.cmeth) # <bound method MyClass.cmeth of <class '__main__.MyClass'>>
MyClass.cmeth()      # this is a class method of <class '__main__.MyClass'>

myClass = MyClass2()   
MyClass2.smeth("hello") # this is a static method, hello
t= MyClass2.smeth       
t("外部变量访问静态方法") # this is a static method, 外部变量访问静态方法
print(MyClass2.smeth) # <function MyClass2.smeth at 0x000002061E96C488>
print(MyClass2.cmeth) # <bound method MyClass2.cmeth of <class '__main__.MyClass2'>>
print(myClass.smeth) # <function MyClass2.smeth at 0x000002061E96C488>
print(myClass.cmeth) # <bound method MyClass2.cmeth of <class '__main__.MyClass2'>>
myClass.smeth("ni")
myClass.cmeth()
