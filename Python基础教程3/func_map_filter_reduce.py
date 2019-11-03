# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 18:54:10 2019

函数式编程：map、filter、reduce、lambda表达式
函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，
因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。
函数的参数如果接收一个指向函数的变量，就变成了一个函数接收另一个函数作为参数，
这种函数称为高阶函数。函数式编程就是指这种高度抽象的编程范式
@author: tangpeng
"""

from functools import reduce

# ============map==================
# map：将序列（只要是Iterable对象就行）中的元素分别传入一个函数进行处理，并返回一个新Iterator
x = list(range(10)) # range(10):返回的只是一个 range对象
print(x)
y = map(str, range(10)) # 等价于 [str(i) for i in range(10)],str()：字符串函数

a = [str(i) for i in range(10)]
print(a)    # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print(y)    # y是一个map对象
print(list(y))  # 可转为list类型


# ============filter==================
# filter:对序列元素进行过滤，返回True的元素,同理返回的是 filter对象
def func(x):
    return x.isalnum()  # 返回布尔值

seq = ['foo','x41','?!','**']
print(list(filter(func,seq)))
print(seq)

# 等价形式：for表达式
print([x for x in seq if x.isalnum()])
# lambda表达式创建函数(lambda在数学中表示匿名函数)
print(list(filter(lambda x: x.isalnum(), seq)))

# ============reduce==================
# map与filter都可以通过列表表达式代替，而代替reduce很难，reduce用处很少
# reduce：将序列前2个元素用给定函数处理后返回，再与第3个元素联合进行相同操作，直到整个序列处理完毕，最后返回一个结果
numbers = [72,101,108,108,111,44,32,119,111,114,108,100,33]
print(reduce(lambda x,y : x+y, numbers)) # reducce需要传入2个参数的函数
print(reduce(lambda x,y : x+y, numbers,1000)) # 含初始值的reduce，首先计算1000和第一个元素的和，再进行后续操作
print(sum(numbers)) # 用sum来等效实现
# reduce 被移到 functools 模块了，需要另外导入才行
