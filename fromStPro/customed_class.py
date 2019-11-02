# __xxx__的变量或者函数名 在python中有特殊用途

class Student(object):
	def __init__(self,name):
		self.name = name

	def __str__(self):
		return 'Student object (name:%s)' % self.name 	#当使用 print打印一个对象时，调用的是它的 __str__方法

	__repr__ = __str__ 	#在命令行输出对象时，调用的是 __repr__()方法（用于调试的），通常它与__str__()输出内容一样，故这样让其重定向到__str__

print(Student('zhangsan'))

class Fib(object):
	def __init__(self):
		self.a, self.b = 0,1

	def __iter__(self):	#实现该方法的对象可用于for...in循环，类似list，该对象返回一个迭代对象，for循环会迭代调用该对象的 __next__方法得到下一个值
		return self

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 100000:
			raise StopIteration()	#退出循环条件
		return self.a	#返回下一个值

	def __getitem__(self,n):	#使其可以像list一样通过索引取值

		if isinstance(n,int):	#增加类似list的切片功能，需要对 n进行类型判断
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a
		if isinstance(n,slice):
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b
			return L

f = Fib()
print(f[0])
print(f[3])
print(f[0:5])

for n in f:
	print(n)