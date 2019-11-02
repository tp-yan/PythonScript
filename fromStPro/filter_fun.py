#filter(func,Iterable):用于过滤序列。func:只接收一个参数，并返回True or False，根据返回值决定该元素是否留在序列中.返回也是Iterator
#使用filter的关键在于：定义一个筛选函数

def no_empty(s):
	return s and s.strip()	#过滤掉空字符串
print(list(filter(no_empty,["A",'','bc',None,'C','  '])))

def is_odd(n):
	return n % 2 == 1	#过滤掉偶数
list(filter(is_odd,[1,2,3,4,5,6,7,8,9]))

#用filter求素数
def _odd_iter():	#构造奇数的generator，是个无限序列
	n = 1
	while True:
		n = n + 2
		yield n
def _not_disvisible(n):	#定义筛选函数
	return lambda x:x % n > 0
def primes():	#返回素数的generator，是个无限序列
	yield 2
	it = _odd_iter()	#初始序列
	while True:
		n = next(it)	#返回序列的第一个数
		yield n
		it = filter(_not_disvisible(n),it)	#构造新序列
#打印1000以内的素数
for n in primes():
	if n < 1000:
		print(n)
	else:
		break

#==========================练习==========================
#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
    reversal = str(n)[::-1] 
    return reversal == str(n)

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

