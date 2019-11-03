
class Student():
	__slots__ = ('__name','age')
	count = 0
	
	def __init__(self,name,age):
		#����_��ͷ�ı����� private�������ⲿ���ܷ���
		self.__name = name
		self.age = age
		Student.count += 1

	def get_name(self):
		return self.__name
		
	def add_age(self,num):
		self.age += num
		
	def get_age(self):
		return self.age
