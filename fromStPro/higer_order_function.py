#函数式编程：函数没有变量。特点：函数本身可以作为参数传入另外一个函数，还允许返回一个函数。python部分支持函数式编程
#high-order function，即高阶函数：一个将函数，作为参数传入另一个函数。这就是一种函数式编程
#函数名其实是一个指向函数的变量
s = 'asd2'
for ch in s:
	print(ch.isalpha())	#isalpha：是否为字母字符

def add(x,y,f):	#将函数f，作为参数传入函数add
	return f(x)+f(y)

print(add(-5,6,abs))
