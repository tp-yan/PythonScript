#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#给实例绑定属性的方法：1.通过实例变量 2.通过 self 变量
class Staff(object):
    name = 'Staff'    #类属性，所有的实例都可访问。如果实例中有与类变量同名变量则优先被访问
    def __init__(self,name):
        self.__name = name


staff = Staff('张三')
staff.age = 29  
staff.__score = 88  #通过这种方法无法绑定private属性
print(staff.age)
# print(staff.__name)
print(staff.__score)
print(Staff.name)
print(staff.name)   # 实例staff因为没有name属性，故访问的是类属性

#为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        #给实例添加属性，而不是引用类属性
        #self.count += 1
        Student.count += 1
        
# 测试:
if Student.count != 0:
	print(Student.count)
	print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
        print(Student.count)
        print(bart.count)
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
