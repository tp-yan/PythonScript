#在一个函数中返回函数
def lay_sum(*args):
	def sum():	#内部函数可以使用外部函数的参数与局部变量。返回函数不要引用任何循环变量或者后续会发生变化的变量
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum 	#返回sum时，相关参数都会保存在返回的函数中，这种程序结构称为"闭包"

f = lay_sum(1,3,5,7,9)
print("f:",f)	#此时打印出来是函数 sum
print(f())	#这才是调用 sum()得到返回结果
f1 = lay_sum(1,3,5,7,9)	#每次调用lay_sum都会返回一个新的函数，即使参数一样
print("f1:",f1)	#2个函数输出地址不一样
print(f == f1)	#False

#利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
	# s = [0]
	# def counter():
		# # global time
		# s[0] += 1
		# return s[0]
	# return counter
	i=0
	def couter(): 
		nonlocal i 
		i=i+1 
		return i 
	return couter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
	print('测试通过!')
else:
	print('测试失败!')
