# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 23:44:11 2019

python基础之序列：list
@author: tangpeng
"""

# 1.list函数：将字符串(其他序列)转为list
l = list("hello")
print(l)
# 2.join():list转字符串
print(''.join(l))

# 3.删除元素 del
names = ['Tom','Snow','Kobe','Klai','Curry','Kevin']
print(names)
del names[1]    # 必须按索引下标删除
# del还能用于 字典和变量
print(names)

# 4.使用切片赋值替换元素
# 4.1 相同长度替换
name = list('Perl')
name[2:] = list('ar')
print(name)
# 4.2 不同长度替换
name[1:] = list('ython')
print(name)

# 5.使用切片赋值插入新序列
numbers = list(range(6))
print(numbers)
numbers[2:2] = [0,0,0]  # 使用新序列替换空序列[]
print(numbers)
# 6.使用切片赋值删除序列
numbers[1:4] = []
print(numbers)
# 同理可以使用 del 删除子序列(切片)
del numbers[0:2]
print(numbers)
del numbers[0::2]   # 步长不为1
print(numbers)
numbers += [6,7,8]
print(numbers)
del numbers[::-2]   # 步长为负数:从右往左删
print(numbers)

# list对象的方法
# 1. append:添加一个对象到尾部
numbers = [1,2,3]
numbers.append(4)
print(numbers)

# 2. clear：清空list
numbers.clear() # numbers[:]  = []
print(numbers)

# 3. copy：返回副本
a = [1,2,3]
b = a.copy()    # b = a[:] or b = list(a)
print(a is b)

# 4. count:指定元素出现的次数
x = [[1,2],1,1,[2,1,[1,2]]]
print(x.count(1))       # 2
print(x.count([1,2]))   # 1
print(x.count([2,1,[1,2]])) # 1

# 5. extend:扩展list，将另一个list拼接到尾部
a = [1,2,3]
a.extend([6,6,6])
print(a)
print(a + [0,0,0])  # extend跟加法拼接不同，会改变原list
print(a)
# 使用切片赋值也可以实现
a[len(a):] = [9,9,9]
print(a)

# 6. index：元素第一次出现的索引
knights = ['we','are','the','knights','who','say','ni']
print(knights.index('who'))

# 7. insert:指定位置插入一个对象
numbers = [3,3,3]
numbers.insert(0,1) # numers[0:0] = [1]
numbers.insert(0,[2,2])
print(numbers)

# 8. pop：删除指定位置的元素，默认队尾元素,返回被删除元素
print(numbers.pop())
print(numbers.pop(1))
print(numbers.pop(0))
# 可以利用append+pop+list实现栈
# 可以利用append+pop(0)+list实现队列，collections模块中的dequ已实现队列

# 9. remove：删数指定的第一个元素
x = ['to','be','or','not','to','be']
x.remove('to')
print(x)

# 10. reverse:将list反序
x.reverse()
print(x)
# reversed函数：返回 list 反序后结果，是一个迭代器，用list()转为list对象，而不改变原list
print(list(reversed(x)))
print(x)

# 11. sort:对list排序，修改原list
numbers = [2,5,2,1,0,9]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
# sorted():可对任何可迭代对象排序，返回总是list，并不修改原对象，返回排序结果
x = [4,6,2,1,7,0,9]
y = sorted(x)
print(y)
print(sorted('python'))

# 12. 高级排序：sort、sorted的参数
names = ['Tom','Snow','Kobe','Klai','Curry','Kevin']
# key参数指定一个函数，该函数对每一个元素创建一个键，然后sort根据这个键对元素排序
names.sort(key=len,reverse=False)   # key=len:按元素长度大小排序
print(names)
names.sort(key=len,reverse=True)
print(names)

# 元组
x = 2,3,4
print(x)    # 多个值用逗号隔开，就会自动创建一个元组
print((42,))
print(3*(42,))
