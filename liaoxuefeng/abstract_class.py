# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 09:46:13 2019

@author: cv
"""

from abc import ABC,abstractmethod

class Talker(ABC): # 抽象类必须继承自ABC类
    @abstractmethod # 形如 @this的是修饰器，此处将方法标记为抽象方法
    def talk(self):
        pass        # 抽象方法不能实现，只能定义

class Knigget(Talker):
    def talk(self):
        print('Ni')
        
k = Knigget()
k.talk()
print(isinstance(k,Talker))

class Herring:
    def talk(self):
        print("Blub")
        
h = Herring()
print(isinstance(h,Talker))

Talker.register(Herring) # 将 Herring类注册为Talker的子类，但实际上并没有继承Talker，也没拥有Talker的方法
print(isinstance(h,Talker))
print(issubclass(Herring,Talker))