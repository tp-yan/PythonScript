from functools import reduce

#map、reduce函数都是内置函数
#map(func,Iterable)：将Iterable对象的每个元素传入函数func进行处理，返回一个Iterator,故func是只能接收一个参数的函数
#注意返回的是Iterator对象，惰性序列，往往通过list(Iterator)将序列计算出来返回一了list


def normalize(name):	#把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
	'''首字母大写，其余小写'''
	return name.capitalize() 
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
list(map(str,[1,2,3,4,5,6]))	#将一个数字list，快速转换成 字符串list

#reduce(func,Iterable)：func:必须是接收两个参数的函数，首先将Iterable对象的前两个数传入func，再将返回结果与下一个元素传入func，重复直到最后一个元素
#使用map+reduce编写一个将 str转换成 int的函数：
def fn(x,y):
	return x*10 + y
def char2num(s):
	digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
	return digits[s]
recude(fn,map(char2num,'13579'))



#===================================练习====================================
#Python提供的sum(可以接受一个list并求和，请编写一个prod()函数，接受一个list并利用reduce()求积
def prod(L):
	def m_multiply(x,y):
		return x * y
	return reduce(m_multiply,L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
    
    
#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(ch):
	return DIGITS[ch]

def get_forward(x,y):
	return x*10 + y
	
def get_back(x,y):
	return x/10 + y
	
def str2float(s):
	index = s.find('.')
	s1 = s[:index]
	s2 = s[index+1:]
	
	'''反转s2'''
	s3 = s2[::-1]
	
	v1 = reduce(get_forward,map(char2num,s1))
	v2 = reduce(get_back,map(char2num,s3))/10
	v = v1 + v2 
	return v
		
print('str2float(\'123.456\') =', str2float('123.456'))

if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


