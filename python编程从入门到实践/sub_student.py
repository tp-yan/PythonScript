from student import Student

class SubStudent(Student):
	def __init__(self,name,age):
		super().__init__(name,age)

	def add_age(self,num,positive):
		if positive:
			self.age += num
		else:
			self.age -= num
