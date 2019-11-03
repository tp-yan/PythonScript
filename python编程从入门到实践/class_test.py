
class Restaurant():
	'''init方法，左右两边是两条下划线'''
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
	
	def set_number_served(self,num):
		if num >= self.number_served:
			self.number_served = num
		else:
			print('输入的值必须大于等于原有的值')
		
	def increment_number_served(self,increment):
		if increment > 0:
			self.number_served += increment
		else:
			print('增数必须大于0')
			
	def describe_restaurant(self):
		print("restaurant_name : ",self.restaurant_name,"\t",end="")
		print("cuisine_type : ",self.cuisine_type)
		
	def open_restaurant(self):
		print('The Restaurant is opening!')

m_restaurant = Restaurant('红宝石','川菜')
y_restaurant = Restaurant('佛跳墙','粤菜')
h_restaurant = Restaurant('宜宾燃面','川菜')

print('name:',m_restaurant.restaurant_name)
print('cuisine:',m_restaurant.cuisine_type)
m_restaurant.describe_restaurant()
y_restaurant.describe_restaurant()
h_restaurant.describe_restaurant()
m_restaurant.open_restaurant()

print("原有就餐人数：",m_restaurant.number_served)
m_restaurant.set_number_served(100)
print("设置后的就餐人数：",m_restaurant.number_served)
m_restaurant.increment_number_served(22)
print("增加后的就餐人数：",m_restaurant.number_served)


#继承
class Car():
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	def get_descriptive_name(self):
		long_name = str(self.year)+' '+self.make+' '+self.model
		return long_name
	
	def read_odometer(self):
		print('This car has ',self.odometer_reading," mile on it.")
	
	def fill_gas_tank(self):
		print('Has filled the tank!')
		
	def set_year(self,year):
		print('this is father class set_year ')
		
#将 电池抽象出来，单独作为一个类
class Battery():
	def __init__(self,battery_size=70):
		self.battery_size = 70
	def describe_battery(self):
		print('This car has a ',self.battery_size,'-KWh battery')
	def get_range(self):
		'''指出电瓶的续航里程'''
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 80:
			range = 270
		elif self.battery_size == 85:
			range = 300
		msg = "This car can go approximately "+str(range)
		msg += " miles on a full charge."
		print(msg)
	def update_battery(self):
		if self.battery_size != 85:
			self.battery_size = 85
	
#父类Car必须与子类在同一个.py中，且父类在子类之前		
class ElectricCar(Car):
	def __init__(self,make,model,year):
		#初始化父类的属性
		super().__init__(make,model,year)
		#子类属性，以实例对象作为属性
		self.battery = Battery()
		
	#重写父类方法，只需要名字相同即可，参数不必相同
	def fill_gas_tank(self):
		print('ElectricCar does not need a gas tank!')
		
	def set_year(self):
		print('this is child class set_year ')
	
e_car = ElectricCar('tesla','model s',2016)
print(e_car.get_descriptive_name())
e_car.battery.describe_battery()
e_car.fill_gas_tank()
e_car.set_year()
e_car.battery.get_range()
e_car.battery.update_battery()
e_car.battery.get_range()

#此句报错，说明父类的set_year(self,year)被子类的同名方法覆盖了，即使参数不同
#e_car.set_year(2020)


class IceCreamStand(Restaurant):
	def __init__(self,restaurant_name,cuisine_type,flavors):
		super().__init__(restaurant_name,cuisine_type)
		self.flavors = flavors
	def show_flavors(self):
		if self.flavors:
			for flavor in self.flavors:
				print(" -",flavor)
		else:
			print('There are no flavors')
	
ice_cream_stand = IceCreamStand('蓝田','咸菜',['草莓','玉米','紫苏','椰子'])
ice_cream_stand.show_flavors()

