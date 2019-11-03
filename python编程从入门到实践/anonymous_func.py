#python对匿名函数提供有限支持
#关键字lambda就表示匿名函数，匿名函数只能有一个表达式，不用写return，表达式结果即是返回值
#可以把匿名函数赋值给一个变量或者作为返回值

anonyFunc = lambda x,y,z: x + y + z	#：前面声明参数，：后面跟一个表达式
anonyFunc(1,2,3)

def build(x,y):
	return lambda:x*x + y*y	#匿名函数作为函数返回值

#请用匿名函数改造下面的代码
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
L1 = list(filter(lambda n:n%2 == 1, range(1, 20)))

print(L)
print(L1)
