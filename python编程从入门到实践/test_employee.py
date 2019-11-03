import unittest
from class_employee import Employee

class TestEmployee(unittest.TestCase):
	'''测试Employee类'''
	def setUp(self):
		self.my_employee = Employee('tang','peng',50000)
		
	def test_give_default_raise(self):
		self.my_employee.show_salary()
		self.my_employee.give_raise()
		self.my_employee.show_salary()
		
		self.assertEqual(self.my_employee.get_salary(),50000+5000)
		

	def test_give_custome_raise(self):
		self.my_employee.show_salary()
		self.my_employee.give_raise(10000)
		self.my_employee.show_salary()
		
		self.assertEqual(self.my_employee.get_salary(),50000+10000)

unittest.main()
