class User():
	def __init__(self,first_name,last_name,age,gender):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.gender = gender
		self.login_attempts = 0
		
	def increment_login_attempts(self):
		self.login_attempts += 1
	
	def reset_login_attempts(self):
		self.login_attempts = 0
			
	def describe_user(self):
		print("first_name: ",self.first_name," last_name: "
		,self.last_name," age: ",self.age," gender: ",self.gender)
		
	def greet_user(self):
		print("欢迎来到王者农药","Welcome to Glory of Kings",
		"\t大吉大利，今晚吃鸡！","winner winner chicken dinner".title())
'''
user_wang = User('王','斌',25,'男')		
user_li = User('李','雪',22,'女')		
user_qing = User('箐','晓',16,'女')		

user_wang.describe_user()
user_wang.greet_user()
user_li.describe_user()
user_li.greet_user()
user_qing.describe_user()
user_qing.greet_user()
user_wang.increment_login_attempts()
user_wang.increment_login_attempts()
user_wang.increment_login_attempts()
user_wang.increment_login_attempts()
print("登录次数：",user_wang.login_attempts)
user_wang.reset_login_attempts()
print("登录次数：",user_wang.login_attempts)
'''
