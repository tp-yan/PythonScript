
class Employee():
	
	def __init__(self,first,last,salary):
		self.first = first
		self.last = last
		self.salary = salary
		
	def give_raise(self,increment=0):
		if increment == 0:
			increment = 5000
		self.salary += increment
		
	def show_salary(self):
		print('年薪：',self.salary)
	
	def get_salary(self):
		return self.salary
