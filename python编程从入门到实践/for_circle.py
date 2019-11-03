'''
python中有两种循环：
1. for x in ...:主要是循环 list与 tuple
2. while循环
'''

sum = 0
l = list(range(100))	#range(100)产生0,...,99的整数序列，list(range(100))再将序列转化为list

for x in list(range(100)):	#---for...in 循环--
   sum += x
print(sum)

sum = 0
n = 99
while n > 0:	#---while循环及 continue、break--
	sum += n
	n -= 1
	if n % 2 == 0:
		n = n -1
		continue
		print('continue')
		break
print(sum)





L = ['Bart', 'Lisa', 'Adam']
for name in L:
	print('hello,%s'%name)
	
pizzas = ['牛肉','玉米','烤肉','火腿']
for pizza in pizzas:
	print("i like "+pizza+" pizza!") 
print("i really like pizza!")

animals = ['bird','pig','eagle']
for animal in animals:
	print('A '+animal+' would make a great pet')
print('Any of these animals would make a great pet!')

x = range(1,5)
print(x[1])
