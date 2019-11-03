#使用Python自带的标准库即模块,此处导入有序的字典
from collections import OrderedDict
#randint(x,y)：返回位于指定范围内的整数
from random import randint

#创建一个空的有序字典
fav_cities = OrderedDict()
fav_cities['China'] = 'Shanghai'
fav_cities['Japan'] = 'Tokyo'
fav_cities['America'] = 'New York'
fav_cities['Britain'] = 'London'

for country,city in fav_cities.items():
	print("country:",country," city:",city)
	

class Die():
	def __init__(self,sides=6):
		self.sides = sides
		
	def roll_die(self):
		print("random:",randint(1,self.sides),"----",self.sides)

die_6 = Die(6)

die_10 = Die(10)

die_20 = Die(20)

for index in range(0,10):
	die_6.roll_die()
	die_10.roll_die()
	die_20.roll_die()
