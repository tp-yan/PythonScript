#在代码运行期间动态增加函数功能(但不改变函数的定义)的方式，称为 装饰器。
#装饰器需要接受一个函数作为参数，并返回一个函数。python的decorator可以使用函数或者类来实现
import time, functools
#定义一个decorator:
def log(func):
	def wrapper(*args,**kw):
		print("call %s()" % func.__name__)	#函数对象属性__name__：返回函数名
		return func(*args,**kw)
	return wrapper

@log #使用装饰器来修饰另一个函数，即给函数动态添加功能
def now():
	print('2015-3-15')
now()	
print(now.__name__)
#将@log放到now()函数的定义出，调用now()相当于执行了： now = log(now)，现在now指向了wrapper，即装饰器返回的那个函数，而非原来的now函数，但now函数仍然存在

#若decorator需要参数，则需要定义一个返回decorator的高阶函数,如下：
def log(txt):
	def myDecorator(func):
		def wrapper(*args,**kw):
			print("%s %s():" % (txt,func.__name__))
			return func(*args,**kw)
		return wrapper
	return myDecorator

@log('execute')
def now():
	print("2015-3-25")
now()	#三层嵌套的decorator效果： now = log('execute')(now)
print(now.__name__)	#此处输出 wrapper，但是有些代码执行依赖于 函数签名，所以我们需要将 原始函数的信息复制到 wrapper函数里面

#完整的decorator：
'''
def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print("call %s()" % func.__name__)	#函数对象属性__name__：返回函数名
		return func(*args,**kw)
	return wrapper

def log(txt):
	def myDecorator(func):
		@functools.wraps(func)	# wrapper.__name__ = func.__name__
		def wrapper(*args,**kw):
			print("%s %s():" % (txt,func.__name__))
			return func(*args,**kw)
		return wrapper
	return myDecorator
'''

#=======================================练习=======================================
#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：

def metric(fn):
	@functools.wraps(fn)
	def wrapper(*args,**kw):
		t0 = time.time()
		result = fn(*args,**kw)
		print('%s executed in %s ms' % (fn.__name__, time.time() - t0))
		return result
	return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


#请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
def call(fn):
	@functools.wraps(fn)
	def wrapper(*args,**kw):
		print("%s begin call" % fn.__name__)
		result = fn(*args,**kw)
		print("%s end call" % fn.__name__)
		return result
	return wrapper

# 测试
@call
def fast1(x, y):
    time.sleep(0.0012)
    print("fast1 executing...")
    return x + y;

@call
def slow1(x, y, z):
    time.sleep(0.1234)
    print("slow1 executing...")
    return x * y * z;

f1 = fast1(11, 22)
s1 = slow1(11, 22, 33)
if f1 != 33:
    print('测试失败!')
elif s1 != 7986:
    print('测试失败!')
    
#再思考一下能否写出一个@log的decorator，使它既支持：
'''
@log
def f():
    pass

又支持：

@log('execute')
def f():
    pass
'''

def log(param):
	def inner_log(text='call'):
		def decorator(fn):
			@functools.wraps(fn)
			def wrapper(*args,**kw):
				print("%s %s()" % (text,fn.__name__))
				return fn(*args,**kw)			
			return wrapper
		return decorator
	
	if callable(param):
		return inner_log()(param)
	return inner_log(param)
	
@log('execute')
def f4():
    pass
f4()

@log
def f3():
    print("@log")

f3()
    


