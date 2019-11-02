# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 13:29:44 2019

第五章之杂乱：
print
@author: 10841
"""
# 1.print
print("hello","world",sep=',')      # 替换默认分隔符
print("hello","world",end=' ++ ') # 替换默认的换行符
print("hello","world",end=' -- ')

# 2.序列解包，即可迭代对象解包
values = 1,2,3
x,y,z = values 
x,y = y,x # 变量交换

d = {'name':'Tom','gs':'ZHang'}
key ,value = d.popitem() # 随机选出一个键值对
print()
print(key,value)

# '*' 收集多余的值
a,b,*rest = [1,2,3,4,5]
print(rest)
first, *middle, last = "TOm JOn Sery Curry Jotdan".split()
print(middle)
print(*middle) # 也是序列解包

a,*b,c = "abc"
print(b) # 无论收集到多少个值，都是以 list 返回
a,*b,c = "ac"
print(b) # 无论收集到多少个值，都是以 list 返回

# 3.True与False实际只是 1,0的别名，可直接参与运算
print(True+1)
print(False+1)

# 4.Python中的条件表达式，等价于C语言的三目运算符 ?:
name = "Tom Gumby"
status = "good" if name.endswith("Gumby") else "bad"
print(status)

# 5. 比较运算符
# 5.1 is与==
# is:判断是否同一对象，查看内存地址是否一样
# 注：不要 将 is用于 数字和字符串这种不可变的基本值上
# ==:比较值/内容是否相等
x = y = [1,2,3]
z = [1,2,3]
print(x is y,id(x),id(y))
print(x is z,id(x),id(z))
print(x == y)
print(x == z)
# 5.2链式比较
age = 11
print("yes" if 0 < age < 100 else "No")

# 5.3序列的比较：字符串，list等以及 ord(),chr()
print("alpha" < "albe") # 按字符的Unicode码字比较
print("alpha" < "bet")
print(ord("中")) # 查看单个字符的Unicode码字
print(chr(20013)) # 获得字符
print([1,2] < [1,3])
print([1,[1,2,3]] < [1,[2,3,4]]) # 尺寸要一样
# 5.4 布尔运算符： and or not

# 5.5 断言assert：不满足某个条件时，抛出异常。用于必须要满足某些条件时程序才能正常执行
# 否则程序应该崩溃
age = 10
assert 0 < age < 100
age = -1
#assert 0 < age < 100, 'The age must be realistic' # 第二参数作为报错说明

# 5.6 并行迭代工具之内置函数zip：可将多个序列拼成一个由元组构成的序列，长度由最短的序列决定
names = ['Tom','Curry','Jordan','faker']
age = [22,21,34]
print(list(zip(names,age)))
for name,age in zip(names,age):
    print(name,' is ',age,"years old")
# 5.7 含索引的迭代 enumerate
for index, name in enumerate(names):
    print(index,'-->',name)
    
# 5.8 sorted与 reversed，都不改变原对象
# sorted:返回list
# reversed:返回可迭代对象
print(sorted([2,1,9,6,3]))
print(sorted("hello,python!"))
print(sorted("hello,PYthon!",key=str.lower)) # 全转为小写后再排序
print(reversed("hello,python!"))
print("".join(reversed("hello,python!")))

# 5.9 循环中的 else 子句：for和while循环都有
from math import sqrt
for n in range(99,81,-1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
else: # 在循环中没有调用break时才执行此 else子句
    print("Don't find it!")
    
# 6. 简单推导
# 6.1 列表推导:for前面只有一个表达式
print([x*x for x in range(10)])
print([x*x for x in range(10) if x % 3 == 0])
print([(x,y) for x in range(10) for y in range(4) if x*y % 8 == 0])
# 小实例：将男女名字开头字母相同的匹配
girls = ['alice','bernice','clarice','clai']
boys = ['chris','arnold','bob']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0],[]).append(girl)
print(letterGirls)
print([b+'+'+g for b in boys for g in letterGirls[b[0]]])

# 6.2 字典推导：for前面是由 key:value组成的键值对，键和值都是表达式
squares = {i:"{} squared is {}".format(i,i**2) for i in range(10)}
print(squares[8])

# 6.3 若将[]替换成()，并不能实现元组推导，而是创建生成器

# 7. del：删除变量或数据结构的成员。只能删除变量名称本身和到对象的引用
# 而不会删除变量所引用的内存空间，即不能删除值
# python中程序员无法自己去删除内存空间，只能由python自动回收释放(当没有引用指向该内存时)
x = ['hello','world']
y = x
y[1] = 'python'
print(x)
del x
print(y)
# print(x) # 变量被删除

# 8. 动态执行Python代码之exec与eval
# 8.1 exec:将字符串的内容作为python语句执行，可执行多条，不会返回结果
exec("print('hello,exec!'); exec(\"print('abc')\")")
# 执行exec时还应该传入 命名空间(即一个字典)，将exec执行的python代码中的变量限制在
# 该命名空间中，防止对原生的变量造成破坏，保证执行的安全性
scope = {}
exec("sqrt = 1",scope) 
print(sqrt(4))
print(scope['sqrt']) # 只有在scope命名空间内，才能访问 exec 中声明的sqrt变量
print(scope.keys()) # python会自动添加 一个键'__builtins__'：其值为python所有的内置函数和值
print(scope) 

# 8.2 eval:计算字符串表示的Python表达式，并返回计算结果
print(eval(input("Enter an arithmetic expression:")))
# 也应该向eval提供一个命名空间
# 命名空间
scope = {}
scope['x'] = 2
scope['y'] = 3
print(eval('x*y',scope))
# 同一个命名空间可多次用于 exec和eval
exec('x = 4',scope)
print(eval('x**2',scope))
