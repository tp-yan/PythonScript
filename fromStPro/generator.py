#通过列表生成式生成list时，如果数据太大，内存不够用，故出现了生成器generator。generator保存的是某种算法
#generator：列表元素按照某种算法推算出来，在元素循环过程中，后续的元素才被推算出来，而非一次性将所有元素计算出来放入内存

#创建generator
#1.将列表生成式的[]改用()
g = (x*x for x in range(10))	#此时 g就是一个generator而非list
print(next(g))	#next:获得generator的下一个返回值，若没有下一个则抛出异常。基本上用不到next,这里输出0
for n in g:	#因为generator也是Iterable，故也可以用for来迭代，因为上一句已经输出0了，故这里输出从1开始
	print(n)

#2.若函数中出现了 yield 关键字，则这个函数是generator，不再是普通函数
#generator遇到yield就暂停执行，并返回 yield 后面的数，当调用next或者下次循环时，generator就从上次暂定的地方继续执行
def fib(max):	#这个函数就被定义成了 generator
	n , a , b = 0 , 0 , 1
	while n < max:
		yield b
		a, b = b, a+b
		n = n + 1
	return 'done'

g = fib(6)	#generator函数的调用，实际是返回一个 generator对象
print(g)
for n in g:
	print(n)

def odd():
	print('step 1')
	yield 1
	print('step 2')
	yield(2)
	print('step 3')
	yield(3)
o = odd()
print(next(o))	
print(next(o))
print(next(o))

#能够使用 next函数不断返回下一个值的对象称为迭代器：Iterator。Iterator对象表示的是一个数据流
#生成器都是Iterator对象，也是Iterable对象，但list、tuple、dict、set、str不是Iterator对象