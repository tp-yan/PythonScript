# 函数参数

def change(a):
	a = 22

a = "sd"
print("a:",a)
change(a)		# 普通变量是值传递，函数内部会产生一个局部变量a，其是实参a的副本
print("a:",a)

# 注：字符串、数字和元组都是不可变的，无法被修改，只能用新值覆盖！

def changeList(n):
	n[0] = 'hi'

n = ["hello","world"]
print(n)		# ['hello', 'world']
changeList(n)	# 传入的可变的数据结构，如列表和字典，实质传入的是对变量的引用，而不是副本
print(n)		# ['hi', 'world']
n[0] = 'heihei'
changeList(n[:])	# n[:]:列表切片，产生列表的一个副本
print(n)		# ['heihei', 'world']