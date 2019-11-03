#正常情况下可以给 实例动态绑定任何属性与方法。动态绑定的属性或方法，只对该实例有效

class Student(object):
	__slots__ = ('name','age','set_age')	#通过__slots__变量来限制实例可以添加的属性，它只对当前类的实例起作用，对子类无效
	pass

stu = Student()
stu.name = "Michael"	#动态绑定属性
print(stu.name)

def set_age(self,age):	#定义一个函数作为实例方法
	self.age = age

from types import MethodType
stu.set_age = MethodType(set_age,stu)	#实例动态绑定方法，只对该实例有效。绑定方法本质也是绑定属性，若__slots__中没有set_age，则这里报错
stu.set_age(25)
print(stu.age)

def set_score(self,score):
	self.score = score

Student.set_score = set_score	#给class绑定方法，所有实例都可用
stu.set_score(100)
print(stu.score)