# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:36:39 2019

数据结构之列表：集合set,{v1,v2,v3,...}
集合：不能有重复数据，且元素无序，即集合具有过滤重复数据的功能，元素类型可以不相同
@author: tangpeng
"""

# 1.创建集合
# 可用set去除list或tuple中的重复元素
L = [1,2,3,1,2,3,4]
print(set(L))
T = ["a",12.3,1,2,3,"b","b",12.3]
print(set(T))

s1 = set("abcdefgh")
s2 = set("afh")
print(s1)

# 2.集合运算
# 差集
print(s1-s2)
print(s2-s1) # 空集用 set()表示
# 并集
print(s1|s2)
# 交集
print(s1&s2)
# 并集去掉交集部分
print(s1^s2)

# 3.集合(list、tuple、dict是特殊的集合)的操作符、函数
print('a' in s1)    # 判断元素是否在集合中
print('b' not in s2)

s3 = set(["abc","efg","zxc"])
print(s3)

print("a" in s3)
print("abx" in s3)
print("abc" in s3)

L = [i for i in range(1,11)]
S = set(L)
T = tuple(L)
D = dict(zip(L,L))  # zip(L,L):返回元素为二元列表/元组的列表/元组，即[(k1,v1)(k2,v2)...]
print(L)
print(S)
print(T)
print(D)

# x in & not in S:x是否在S中
print(3 not in L ,3 not in T, 3 not in S, 3 not in D) 
# S+T:连接S+T，返回连接后的新集合类
print(L+L)   
#print(S+S)     # 集合中不能有相同元素，故不能连接
print(T+T)   
#print(D+D)   # 字典中不能有相同key，故不能连接

# S*n 或 n*S :将S自身延长n次
print(L*3)
#print(S*3)
print(T*3)
#print(D*3)

# list、tuple、set有相同的操作函数
L = [1,2,3,4,5]
T = 1,2,3,4,5
S = {1,2,3,4,5}
print(len(L),len(T),len(S))
print(min(L),min(T),min(S))
print(max(L),max(T),max(S))
print(sum(L),sum(T),sum(S))

def add1(x):
    return x+1

print(list(map(add1,L)),list(map(add1,T)),list(map(add1,S)))

# 迭代
for i in S: # in T/L
    print(i)
print()
# 获取迭代器
it = iter(S)    # T\L一样
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it)) # 迭代完后，抛出StopIteration异常

# 对于dict的操作
for i in D:
    print(i,D[i])
print()    
it = iter(D)
k = next(it)
print(k,D[k])
k = next(it)
print(k,D[k])
