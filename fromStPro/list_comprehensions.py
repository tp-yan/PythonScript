#列表生成式：用来创建list的生成式
L = [x*x for x in range(1,11)]	#单层循环的生成式
L2 = [x*x for x in range(1,11) if x % 2 == 0]	#带条件的单层循环的生成式
L3 = [ m + n for m in 'ABC' for n in 'XYZ']		#双层循环的生成式，三层以上循环很少用
d = {'x':'A','y':'B','z':'C'}
L4 = [k + "=" + v for k,v in d.items()]
words = ['Hello','World','IBM','Apple']
print([s.lower() for s in words])	#将所有元素小写

import os
file = [d for d in os.listdir('.')]	# os.listdir：列出指定路径下的所有目录和文件

squares = [value**2 for value in range(1,11)]
print("squares:",squares)

huge_list = [value for value in range(1,1000001)]
print("huge_list max: ",max(huge_list))
print("huge_list min: ",min(huge_list))
print("huge_list sum: ",sum(huge_list))
for value in list(range(1,21,2)):
	print(value)
cube_list = [value**3 for value in range(1,11)]
print(cube_list)	