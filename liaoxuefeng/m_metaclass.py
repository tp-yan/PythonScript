#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:48:27 2019

@author: tangpeng

动态创建类 与 元类
"""

"""
使用type()动态创建类
要创建一个class对象，type()函数依次传入3个参数：
1. class的名称；
2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3. class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
"""

from hello import Hello

h = Hello()
h.hello()
print(type(Hello)) # 类对象是 <class 'type'> 类型
print(type(h)) # <class 'hello.Hello'>

# type()函数既可以返回一个对象的类型，又可以创建出新的类型
# 我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：
def fn(self,name='world'):
    print("Hello %s" % name)
    
Hello = type('Hello',(object,),dict(hello=fn)) # 创建 Hello class
h = Hello()
h.hello()
print(type(Hello))
print(type(h)) # <class '__main__.Hello'> 当前运行模块名为 __main__


"""
尝试编写一个ORM框架：
1. 编写底层模块的第一步，就是先把调用接口写出来。比如，使用者如果使用这个ORM框架，想定义一个`User`类来操作对应的数据库表`User`，我们期待他写出这样的代码：
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()
"""
# 首先来定义`Field`类，它负责保存数据库表的字段名和字段类型：
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)
    
# 在`Field`的基础上，进一步定义各种类型的`Field`，比如`StringField`，`IntegerField`等等：
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

# 下一步，就是编写最复杂的`ModelMetaclass`了
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items(): # 找出所有字段属性并重新封装到__mappings__字典中
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name     # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)
    
# 以及基类`Model`：
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))
        

class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')
# 尝试使用一下
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()
