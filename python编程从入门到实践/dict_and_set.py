#-*- coding:utf-8 -*-
#以下部分是 ditc-字典的使用，dict相当于java中的map，也是用 key-value存储。优点：访问速度快，缺点：耗空间
#dict是无序的map，不是按key放入的顺序存储的
#dict的key必须是不可变的，list不能作key，而tuple可以，但tuple中不能包含list，否则也不能作为key

d = {'mical':95,'bob':75,'tracy':88}
print(d['bob'])
d['adam'] = 90	#向dict中添加元素
print('thamos' in d)	#判断是否存在key:thamos
print(d.get('Thomas', -2))	#获得key:bob对应的value，不存在返回-1(自己指定的)，默认返回None

d.pop('bob') 	#删除key-value，pop(key)

kk = {}
kk['ss'] = 'zz'
tt = (1,2,3)
kk[tt] = 123
tt2 = (1,2,[3])	#tuple中不能包含list，否则也不能作为key
# kk[tt2] = 111 #出错
print(kk)

#------------set的使用----------------
#set里面只存 key，不存value，key不能重复，set也是无序的
#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
#set和dict的唯一区别仅在于没有存储对应的value
#set的原理和dict一样,同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”
#要创建一个set，需要提供一个list作为输入集合

s = set(['a',1,1.92])
s.add(3)	#添加元素
s.add('swjtu')
s.remove(3)	#删除元素

s1 = set([1,2,3])
s2= set([2,3,4])
print(s1&s2)	#交
print(s1|s2)	#并
#s1.add([6,7,8])	#报错
print("====================")
s1.add((1,2,3))
#s1.add((1,[12,22]))	#报错



##########################################################################################
alien_1 = {'color':'green'}
alien_1['x_position'] = 0	#向dict中添加新的key-value
alien_1['y_position'] = 25
alien_1['speed'] = 'medium'
print('original x-position:',alien_1['x_position'])
speed = alien_1['speed']
if speed == 'slow':
	x_increment = 1
elif speed == 'medium':
	x_increment = 2
elif spped == 'fast':
	x_increment = 3
alien_1['x_position'] = alien_1['x_position'] + x_increment
print('new x_position:',alien_1['x_position'])

del alien_1['speed'] #删除key-value 或者 alien_1.pop('speed')

#多行定义dict
favorite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'java',
	}
print(favorite_languages)
#print分行输出
print("ssssss"+
	"sssszzzzzz"+
	"zxcvbbvsdfsdfsd"
	)

user = {'first_name':'wang','last_name':'xiao','age':22,'city':'成都'}
user2 = {'first_name':'zhang','last_name':'xiang','age':21,'city':'宜宾'}
user3 = {'first_name':'li','last_name':'hao','age':20,'city':'运城'}
people = [user,user2,user3]
for u in people:
	print("first_name: ",u['first_name'],'last_name: ',u['last_name'],'age: ',u['age'],'city: ',u['city'])
print(user)



#==============================================练习==============================================
rivers = {'changjiang':'china','henghe':'india','mixixibihe':'america'}
for river,country in rivers.items():
	print("The ",river," runs through ",country)
for country in rivers.values():
	print("country: ",country)
for river in rivers.keys():
	print("river: ",river)
cat = {'type':'cat','host':'tp'}
dog = {'type':'dog','host':'mh'}
fish = {'type':'fish','host':'lz'}
pets = [cat,dog,fish]
for pet in pets:
	print('type: ',pet['type'],' host: ',pet['host'])
	
favorite_places = {
	'tp':['宜宾','成都','上海','厦门'],
	'mh':['运城','成都','湘潭','重庆'],
	'lz':['阿克苏','乌鲁木齐','新疆']
	}
for name,places in favorite_places.items():
	print(name+":")
	for place in places:
		print("\t"+place)

cities = {
	'New York':{
		'country':'America',
		'population':11223344,
		'fact':'世界金融中心'
		},
	'Tokyo':{
		'country':'Japan',
		'population':11223434,
		'fact':'亚洲第一大城市'
		},
	'Beijing':{
		'country':'China',
		'population':12342341,
		'fact':'中国第二大城市'
		}
	}
for city_name,infos in cities.items():
	print('城市:',city_name)
	for info,value in infos.items():
		print("\t",info,":",value)
print("=================",end="")
print("+++++++++++++++++")


