#继承最大的好处：子类获得了父类的全部功能
#多态的好处：所有声明父类的地方，都可以传入子类，当增一个子类时，原来的代码完全不变。调用父类的方法，就会转去调用传入的子类对应的方法。这是开闭原则的一种体现

class Animal(object):
	def run(self):
		print("Animal is running...")

class Dog(Animal):
	def run(self):	#当子类中有和父类重名的方法时，子类将父类的方法覆盖，总是会调用子类的方法，这就是“多态”
		print("Dog is runing...")

def run_tiwce(animal):	#由于Python中不需要指明数据类型，所以animal可以是任何类型的变量。只要animal变量有 run方法就能正确执行，这就是动态语言的“鸭子类型”
	animal.run()		#而静态语言比如Java，就规定了参数的类型为Animal，传入参数就必须是Animal或其子类类型
	animal.run()

run_tiwce(Animal())
run_tiwce(Dog())

class Tortoise(Animal):	
	def run(self):
		print("Tortoise is running...")

run_tiwce(Tortoise())	#新增子类直接传入方法，而无需改变run_tiwce的任何内容。这就是 对扩展开放，对修改封闭

class Timer(object):
	def run(self):
		print("Timer start...")

run_tiwce(Timer())	#“鸭子类型”