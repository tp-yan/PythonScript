
class Student():
	__slots__ = ('__name','age')
	count = 0
	
	def __init__(self,name,age):
		#两个_开头的变量是 private变量，外部不能访问
		self.__name = name
		self.age = age
		Student.count += 1

	def get_name(self):
		return self.__name
		
	def add_age(self,num):
		self.age += num
		
	def get_age(self):
		return self.age
