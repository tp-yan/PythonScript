#help(abs)：可查看函数信息
#python有很多内置函数：
print(max(1,2))
print(max('1a','2c'))
#数据类型转换函数
print(int('123'))
print(int('44'))
print(float("11.2"))
print(float(11))
print(str(11.92))
print(str(23))
print(bool(23))	#True
print(bool(''))	#False
print(hex(1000))	#hex:将一个整数转换成 十六进制表示的字符串

#函数名就是指向函数对象的引用
a = abs
print(a(-1))

def nop():	#定义空函数
	pass	#pass作为占位符

#--定义函数--
#如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return
#my_abs函数x应该是数值类型，但 my_abs('s')时不会报错，直到比较 x >= 0才报错
#所以根据需要可以检查参数类型，用内置函数isinstance()实现： 
def my_abs(x):
	if not isinstance(x, (int, float)):	#只要x是后面口号中的一种类型就返回True
		raise TypeError('bad operand type')	#如果没有这行，或抛出默认的异常信息
	if x >= 0:
		return x
	else:
		return -x
print(my_abs(-10))
#print(my_abs('s'))  #抛出异常

import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny	#函数可以返回多个值--实质是返回一个tuple对象，返回tuple可以省略括号
x,y = move(100,100,60,math.pi/6)	#按顺序分别赋值x,y
t = move(100,100,60,math.pi/6)	#t是tuple
print(x,y)
print(t)

#位置参数：实参按位置顺序给形参传值
#默认参数：1.必选参数在前，默认参数在后。2.变化大的默认参数在前，变化小的后。有多个默认值时，可以按顺序传值，也可以按参数名传值。3.默认参数必须指向不变对象！！！！！
def enroll(name,sex,age=6,city='beijing'):
	pass
enroll('bob','m',7)		#city使用默认值
enroll('bob','m',city='tianjing') 	#age使用默认值，这里必须指定 city参数名，因为默认参数是从左往右赋值的
#可变参数：传入函数的参数可以是0、1、2,...n个。定义： *参数名
def cal(*numbers):	#参数numbers接收到的是一个tuple
	sum = 0
	for n in numbers:
		sum += n*n
	return sum
cal(1,4,5,6)
myNum = [1,5,6,7] #myNum = (1,5,6,7)
cal(*myNum)	#将已存在的 list或者 tuple传入 可变参数函数： 在 list或tuple变量名前面加 *后传入
#关键字参数：传入>= 0个含参数名的参数，关键字参数，在函数内部被组装成一个dict。定义： **参数名，如下：
def person(name,age,**kw):	#kw得到的是实参的拷贝，改变不影响实参
	print('name:',name,'age:',age,"others:",kw)
extra = {'city':'beijing','job':'engineer'}
person('Jack',24,**extra)	#将已存在的dict传入可变参数时：**变量名
#命名关键字参数：限制关键字参数的名字。1.使用 * 以后的参数就是命名关键字 2.若命名关键字参数前面有可变参数（*num），则不需要再加 *
def person(name,age,*args,city,job):	#python支持函数重载，以下几个person函数不会冲突
	print('name:',name,'age:',age,"args:",args)
	print(city,job)
person('t',12,city='jiangan',job='ffff')	#所有列出的命名关键字参数都必须赋值，*args可以传0个参数，不能传入命名关键字参数之外的参数
def person(name,age,*args,city='beijing',job):	#命名关键字参数，也可以设置默认值
	print(city,job)
person('tp',12,job='ffff')	
#参数定义的顺序：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a,b,c=0,*args,*kw):
	pass

def f2(a,b,c=0,*,d,**kw):
	pass
#对于任何函数，都可以通过类似 func(*args,**kw)	的方式调用



#==========================练习==========================
def quadratic(a,b,c):
	if isinstance(a,(int,float)) & isinstance(b,(int,float)) & isinstance(c,(int,float)):
		d = b*b - 4*a*c
		if d>=0:
			k = math.sqrt(d)/2*a
			print("answer 1 %.2f"%(k-b/(2*a)))
			print("answer 2 %.2f"%(-k-b/(2*a)))
		else:
			print("no answer")
	else:
		print("error")

quadratic(1,4,0)
quadratic(2,3,1)
quadratic(2,1,5)




def display_msg():
	print('in this chapter , i will learn how to define and use function')
display_msg()

def favorite_book(title,year=2016): #year有默认值,默认值参数必须放在最后
	print('One of my favorite books is ',title.title())
	print('year: ',year)
favorite_book('a仙剑奇侠传')
favorite_book(year=2017,title='我的天空')	#关键字调用函数，实参不需要对应形参顺序

def make_shirt(size = 'T',text = 'I Love Python'):
	print('The size of T-shirt is ',size,' and print text: ',text)
make_shirt('medium','hello python!')
make_shirt()
make_shirt(size='L',text='China')
make_shirt(text='China')
make_shirt('China')

def describe_city(city_name,country='Earth'):
	print(city_name,' is in ',country)
describe_city('Tokyo','Japan')
describe_city(country = 'America',city_name = 'New York')
describe_city('London')

def city_country(city,country):
	return city+", "+country
print(city_country('Shanghai','China'))
print(city_country('Chengdu','China'))
print(city_country('Paris','France'))
print(city_country('Moscow','Russia'))

def make_album(singer_name,album_name,num=1):
	album = {'singer_name':singer_name,'album':album_name}
	album['num'] = num
	return album
print(make_album('tp','no more no time !'))
print(make_album('Jacson','爱你一万年',3))
print(make_album('刀郎','西海情歌',4))

def show_magicians(magicians):
	for magician in magicians:
		print(magician)
my_magicians = ['于谦','项羽','关羽','流星']
show_magicians(my_magicians)

def make_great(magicians):
	for num in range(0,len(magicians)):
		magicians[num] = 'The Great '+magicians[num]
	return magicians
		
new_magicians = make_great(my_magicians[:])
show_magicians(my_magicians)
show_magicians(new_magicians)


def sanwich_ingredient(*ingredients):	#定义参数个数不确定的函数
	''' * 代表将所有的参数存放到ingredients列表中'''
	for ingredient in ingredients:
		print(ingredient)
sanwich_ingredient('香蕉','萝卜','草莓','榴莲')
sanwich_ingredient('苹果','番茄','茄子')
sanwich_ingredient('果冻','凉糕','燃面')

def build_profile(first_name,last_name,**user_info):
	'''位置、关键字参数都必须放在任意数量参数前面
		first_name last_name为位置参数
		**：表示任意的key-value参数.所有的key-value将封装到user_info这个字典中
	'''
	profile = {}
	profile['first_name'] = first_name
	profile['last_name'] = last_name
	for key,value in user_info.items():
		profile[key] = value
	return profile
print(build_profile('tang','peng',age=22,address='成都',school='swjtu'))
	
def make_car(manufacturer,model,**car_info):	
	car = {}
	car['manufacturer'] = manufacturer
	car['model'] = model
	for key,value in car_info.items():
		car[key] = value
	return car
print(make_car('subaru','outback',color='blue',tow_package=True))

