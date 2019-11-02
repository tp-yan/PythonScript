#类定义： class ClassName(父类，默认是object):	#object是所有类的父类
#所有类中的方法，第一个参数必须是self,指实例本身，类中的方法与普通函数一样
#如果类中有 __init__方法(不是必须)，则创建类实例时，必须输入与 __init__匹配的参数
#Python中的实例对象可以自由绑定属性

from student import Student
from sub_student import SubStudent

ss = Student('zs',20)
print(ss.get_age())

stu = SubStudent("tp",22)

stu.score = 99

print("age:",stu.age,"\n")
print("name:",stu.get_name(),"\n")
print("score:",stu.score)

stu.add_age(5,False)
print("age:",stu.age,"\n")


print("Student Count:",Student.count)
print("SubStudent Count:",SubStudent.count)

# 在python中实例的变量若以'__'开头，就变成了一个Private变量，只能内部访问，外部不能访问。但是可以通过其他方式访问，因为Python解释器，将private变量改成了 _类名__变量名
# 在python中 变量名为'__xxx__'的变量不是private变量，而是特殊变量。而 一个'_'开头的变量虽然能直接访问，但是不要随意访问

class MyStudent(object):
	def __inti__(self,name,score):
		self.__name = name 		# 变量名改成 _MyStudent__name，所以MyStudent实例里面没有 __name这个名字的变量了
		self.__score = score 	#同上， _MyStudent_score

	def print_score(self):
		print("%s: %s " % (self.__name,self.__score))

myStu = MyStudent('tangpeng',99)
myStu.print()
myStu.__name #TypeError: object() takes no parameters， MyStudent类已经没有 __name这个名字的变量了