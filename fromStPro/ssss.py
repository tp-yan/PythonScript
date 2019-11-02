#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：

def is_palindrome(n):
	s1 = str(n)
	s2 = s1[::-1]
	if s1 == s2:
		return True
	else:
		return False

# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
	print('测试成功!')
else:
	print('测试失败!')



#假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#请用sorted()对上述列表分别按名字排序：
def by_name(t):
	return t[0].lower()

print(by_name(L[0]))
'''
L2 = sorted(L, key=by_name)
print(L2)

#再按成绩从高到低排序：
def by_score(t):
    pass
L2 = sorted(L, key=by_score)
print(L2)
'''
