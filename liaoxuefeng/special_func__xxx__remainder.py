#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 09:36:41 2019

@author: tangpeng

使用特殊方法定制类，余下部分
"""

""" 
__getitem__：实现类似 list 的切片操作
"""
class Fib:
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b = 1,1
            for x in range(n):
                a,b = b,a+b
                return a
        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a,b = 1,1
            L =[]
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b = b,a+b
            return L

f = Fib()
print(f[0:5])
print(f[:10])

# 以上没有对step参数和负数作处理


"""
__getattr__()：动态返回一个属性
当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性
"""
class Student:
    def __init__(self):
        self.name = 'Jordon'
        
    # 注意，只有在没有找到属性的情况下，才调用__getattr__
    def __getattr__(self,attr):
        if attr == 'score':
            return 99
        # 返回函数也是可以的
        if attr == 'age':
            return lambda :25
        # 要让class只响应特定的几个属性，对于其他不存在的属性，应该按照约定抛出AttributeError的错误：
        raise AttributeError("Student object has no attribute %s" % attr)
            
s = Student()
s.name
print(s.score)
print(s.age())

# 利用完全动态的__getattr__，可以写出一个链式调用：
class Chain:
    def __init__(self,path=''):
        self._path = path
        
    def users(self,value):
        return Chain("%s/%s/%s" % (self._path,"users",value))
    
    def __getattr__(self,path):
        return Chain("%s/%s" % (self._path,path))
    
    def __str__(self):
        return self._path
    __repr__ = __str__
        
print(Chain().status.user.timeline.list)   
# 还有些REST API会把参数放到URL中，比如GitHub的API： GET /users/:user/repos
# 调用时，需要把:user替换为实际用户名 ==> /users/michael/repos
print(Chain().users('michael').repos)


"""
__call__():任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用

"""
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self,value):
        print("My name is %s." % value)

s = Student('Michael')
s("jordan")

# 判断一个对象是否能被调用，能被调用的对象就是一个Callable对象
print( callable(Student("zhangsan")))
print(callable(max))
print(callable([1,2,3]))
print(callable('abc'))

#  GET /users/:user/repos 的一种巧妙实现：
class Chain(object):
    def __init__(self, path=''):
       self.__path = path

    def __getattr__(self, path):
       return Chain('%s/%s' % (self.__path, path))

    def __call__(self, path):
       return Chain('%s/%s' % (self.__path, path))

    def __str__(self):
       return self.__path

    __repr__ = __str__

# 调用 .users 时 触发 __getattr__ 返回一个 Chain对象，而该对象又是 Callable对象，故调用了 Chain('michael')
print(Chain().users('michael').repos) # /users/michael/repos
