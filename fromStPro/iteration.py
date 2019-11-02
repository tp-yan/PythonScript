#for循环可以作用在任何一个可迭代对象上，比如dict、set、str、tuple、list等
from collections import Iterable	
isinstance('abc',Iterable)	#判断str类型是否可迭代
isinstance(123,Iterable)	#判断int类型是否可迭代


library = {'while':'while循环',
	'for':'for循环',
	'in':'是否存在',
	'del':'删除列表或者dict元素',
	'set':'集合','set2':'集合'}
for key in library:		#dict默认根据key遍历，迭代输出顺序与key-value存入顺序也许不同
	print(library[key])

for key,value in library.items():	#遍历字典中的key-value，items():返回key、value的列表
	print('key:',key,'\tvalue:',value)

for key in library.keys():	#显示的使用key迭代,keys():返回key的列表
	print("key: ",key)

for value in library.values():	#遍历value,values():返回value的列表
	print("value: ",value)		#可能包含重复的value

for language in set(library.values()):	#使用set来剔除value中的重复项
	print('language: ',language)

for i, value in enumerate(['A','B','C']):	#将list实现 索引-元素 对的格式来遍历，使用内置函数enumerate
	print(i,value)

for x, y in [(1,1),(2,2),(3,3)]:
	print(x,y)

favorite_num = {
	'zhang':[1,3,8],
	'wang':[2],
	'li':[6,9],
	'zhao':[1,5],
	'han':[8]
	}
for name,nums in favorite_num.items():
	print(name+":")
	for num in nums:
		print("\t",num)