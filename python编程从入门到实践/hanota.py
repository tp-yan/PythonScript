#使用generator生成器生成列表
def triangles():
	row = 1 #行数
	last_list = [1]
	while True:
		current_list = []
		if row == 1:
			current_list = last_list[:]
		else:
			index = 0
			while index < row:
				if index == 0 or index == row-1:
					current_list.append(1)
				else:
					current_list.append(last_list[index-1]+last_list[index])
				index += 1
				
		yield current_list
		
		last_list = current_list
		row += 1	

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')		

#列表生成式
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x,str)]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

def findMinAndMax(L):
	'''迭代查找一个list中最小和最大值，并返回一个tuple'''
	if L != []:
		l_min = l_max = L[0]
		for value in L:
			if l_min > value:
				l_min = value
			if l_max < value:
				l_max = value
		return (l_min,l_max)
	return (None, None)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

def move(n,A,B,C):
	'''汉诺塔,n:表示A柱子上的初始盘子数量，要将A上的盘子借助B移至C柱上,盘子由大到小堆放'''
	if n == 1:
		print(A,"--->",C)
	else:
		#将 A上的n-1个盘子，借助C转移到B
		move(n-1,A,C,B)
		#将编号为n的盘子，即最大的盘子从A-->C
		move(1,A,B,C)
		#将B上的盘子借助A转移到C，此时相当于把原来的AB柱子，名字互换。
		#实质都是从一个柱子借助另外一个柱子将盘子转移到第三个柱子上
		move(n-1,B,A,C)

# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
move(3, 'A', 'B', 'C')

#print("787809aas0".index("0"))
print("\n\n\n")

def trim(s):
	'''利用切片操作，取出字符串首尾空格'''
	first_index = 0
	while first_index < len(s):
		if s[first_index] == ' ':
			first_index += 1
		else:
			break
	last_index = len(s) - 1
	while last_index >= 0:
		if s[last_index] == ' ':
			last_index -= 1
		else:
			break
	if first_index <= last_index:
		return s[first_index:last_index+1]
	else:
		return ""
		
print(trim('hello  '))

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
