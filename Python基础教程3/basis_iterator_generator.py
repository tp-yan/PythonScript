# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 10:31:38 2019

迭代器与生成器
@author: 10841
"""

# 1.迭代器iterator：实现了方法__iter__的对象就是可迭代的，同时实现了 __next__方法
# 的对象就是 迭代器了
# 迭代器协议：__iter__和__next__方法
# 迭代器的优势：可逐个地获取值，而不必像list那样一次性获取，尤其是面对大量数据时，内存不足
class Fibs:
    """斐波那契数列"""
    def __init__(self):
        self.a, self.b = 0,1
    def __next__(self): # 返回下一个值
        self.a, self.b = self.b, self.a + self.b
        return self.b
    def __iter__(self): # 返回自身
        return self
    
fibs = Fibs() # 创建一个迭代器对象
for f in fibs: # 任何可迭代对象可都用于 for 循环
    if f > 1000:
        print(f)
        break
    
# 通过调用内置函数 iter()可获得一个迭代器对象
it = iter([1,2,3,4])
print(next(it)) # 与调用 it.__next__()等效
print(next(it))
print(next(it))
# 当迭代完时，抛出StopIteration异常
it = iter("abcdefg")
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# 由迭代器创建序列
class TestIterator:
    value = 0
    def __next__(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value
    def __iter__(self):
        return self
    
ti = TestIterator()
print(list(ti)) # 直接由list构造函数将迭代器转换为list，将迭代器的所有可能值，计算出来存入list
# 直到遇到StopIteration

# 2.生成器generator：一种使用普通函数语法定义的迭代器，逐个产生迭代元素
'''
 生成器 = 生成器的函数 + 生成器的迭代器
 调用生成器函数时，不会执行函数体，而是返回了一个迭代器对象
 每次向迭代器对象请求值时，就执行生成器的代码，直到遇到yield生成一个值，或者return终止生成器
'''
# 2.1创建生成器:包含 yield语句的函数就是生成器
def flatten(nested):
    '''遍历多层嵌套的list的每个元素'''
    for sublist in nested:
        for element in sublist:
            yield element
            
nested = [[1,2],[3,4],[5]]
for num in flatten(nested):
    print(num)
    
print(type(flatten(nested)))
list(flatten(nested)) # 调用生成器函数时，不会执行函数体，而是返回了一个 迭代器对象


# 2.2生成器推导，类似于列表推导，但是其不是创建一个列表，而是返回一个生成器
g = ((i+2)**2 for i in range(2,27)) # 将列表推导的[]换成()即可
print(g)
print(next(g))
print(sum(i**2 for i in range(10))) # 在调用函数时使用生成器推导，无需再添加一对括号
print(max(i**2 for i in range(10)))

# 2.3递归式生成器：处理多层嵌套的list
def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested # 如果传入的是一个元素，而非list，则在for处就抛出异常，直接返回单个元素

nested = [[[1],2],3,4,[5,[6,7]],8]
print(list(flatten(nested)))
for item in flatten(nested):
    print(item)

print("============flatten2==============")
def flatten2(nested):
    try:
        for sublist in nested:
            for item in flatten2(sublist):
                yield item
    except TypeError:
        yield nested 

nested = [[[1],2],3,4,[5,[6,7]],8]
print(list(flatten2(nested)))
for item in flatten2(nested):
    print(item)
print("============flatten2==============")

# 不能将flatten用于迭代类似于字符串的对象：因为单个字符也是一个可迭代的字符串
def flatten(nested):
    try:
        try:
            nested + '' # 将该对象与字符串拼接来检查是否为字符串对象
        except TypeError:
            pass
        else:
            raise TypeError # 拼接没问题，说明该对象就是字符串对象
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested
        
print(list(flatten(['foo',['bar',['baz']]])))


# 2.4 生成器的方法
# 外部世界可以通过调用 生成器的 send方法发送任何一个对象
# 其他方法：throw和close：停止生成器
def repeater(value):
    while True:
        new = (yield value) # 用()括起来的 yield被用作表达式而不是语句了，只有当外部
        # 调用send方法时，该表达式才返回一个由 send发送的“消息”，否则返回None（比如调用next()）
        print("while-outer-new:",new)
        if new is not None:
            print("if-inner-new，我是从外部世界发送来的消息：",new)
            value = new # 将消息赋值给返回值
            
r = repeater(42)
print(next(r))
# 只有当生成器挂起（第一次遇到yield之后）之后才能调用send
print("调用send:\n",r.send("hello,world")) # 返回发送的对象
print(next(r))


