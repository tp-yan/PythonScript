#从class_test模块中导入Restaurant
'''
from class_test import Restaurant

my_res = Restaurant('万州烤鱼','川菜')
my_res.describe_restaurant()

from car_test import Car
my_car =  Car('BYD','唐',2016)
my_car.read_odometer()
5
class MyCar(Car):
	def __init__(self,make,model,year,country):
		super().__init__(make,model,year)
		self.country = country
	
	def describe_car_info(self):
		print("manufacturer:",self.make," year:",self.year," country:",self.country)

mycar = MyCar('吉利','送',2015,'中国')
mycar.describe_car_info()
'''
from system_db import Priviliges,Admin

admin = Admin('张','无',22,'男')
admin.privilige.show_priviliges()
