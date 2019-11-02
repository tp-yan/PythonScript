# 函数创建、文档字符串与返回值

# 创建函数：求斐波那契数列函数
def fibs(num):
	'''这里是函数的文档，成为文档字符串，作为函数的一部分存储'''		# 这里是函数的文档
	result = [0,1]
	for i in range(num-2):
		result.append(result[-2] + result[-1])
	return result


x = int(input("num:"))	# input()读入的内容全是字符串！
print(fibs(x),"\n")
print(fibs.__doc__)	# __doc__：函数属性
help(fibs)	# 打印函数的文档字符串。 
# 注：若函数没有返回值，则默认返回None，故python中的所有函数都是有返回值的！