from user import User

class Priviliges():
	def __init__(self,priviliges):
		self.priviliges = priviliges
	def show_priviliges(self):
		if self.priviliges:
			for privilige in self.priviliges:
				print(" -",privilige)
		else:
			print('There are no priviliges')
			
class Admin(User):
	def __init__(self,first_name,last_name,age,gender):
		super().__init__(first_name,last_name,age,gender)
		self.login_attempts = 0
		self.privilige = Priviliges(['can add post','can delete post','can ban user'])

admin = Admin('张','三',24,'男')
admin.privilige.show_priviliges()

