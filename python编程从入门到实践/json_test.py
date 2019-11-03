#python借助json模块来存储数据到本地或从本地读取到内存
import json

numbers = [1,2,3,4,5,6,7]
#.json：按照json格式存储
file_name = 'numbers.json'

with open(file_name,'w') as f_obj:
	#dump:倾倒，丢下，倾销，卸下，摆脱
	json.dump(numbers,f_obj)

#从本地读取出来
with open(file_name) as f_obj:
	_numbers = json.load(f_obj)
print(_numbers)

'''
#记录用户姓名到本地
file_username = 'username.json'

try:
	with open(file_username) as f_obj:
		username = json.load(f_obj)
except FileNotFoundError:
	with open(file_username,'w') as f_obj:
		username = input('please input your name:')
		json.dump(username,f_obj)
else:
	print('Welcome Mr ',username.title(),'!')			
'''

def get_stored_username(filename):
	'''从本地获得用户名'''
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username(saved_file):
	'''获取并保存新用户名'''
	username = input('please input your name:')
	with open(saved_file,'w') as f_obj:
		json.dump(username,f_obj)
	return username

def greet_user():
	'''欢迎用户'''
	filename = 'saved_username.json'
	username = get_stored_username(filename)
	if username:
		hint = "Are you " +username+"?(Y/N)"
		res = input(hint)
		if res.upper() == "Y":
			print('Welcome back, ',username.title(),"!")
			return
	username = get_new_username(filename)
	print('We\'ll remember you when you come back, ',username.title()+" !")

greet_user()


#test
file_rem_num = 'favorite_nums.json'

def get_stored_num(filename):
	try:
		with open(filename) as f_obj:
			num = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return num

def save_new_num(filename):
	with open(filename,'w') as f_obj:
		num = input('input your favorite num:')
		json.dump(num,f_obj)
	return num
	
def record_num():
	num = get_stored_num(file_rem_num)
	if num:
		print("I know your favorite number!It's ",num)
	else:
		num = save_new_num(file_rem_num)
		print("I remember your favorite num:",num)

record_num()


