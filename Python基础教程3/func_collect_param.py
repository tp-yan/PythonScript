# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 15:17:40 2019
收集参数：让用户输入任意数量的参数
@author: tangpeng
"""

# =============1=============
def print_params(*params):
    '''*参数：收集多余的位置参数（不能是关键字参数）到一个元组中'''
    print(params)

print_params(1,2,4)

def print_params_2(title,*params):
    '''收集多余的位置参数'''
    print(title)
    print(params)

print_params_2('Params:','2','###',4)

def print_params_3(**params):
    '''**参数：收集多余的关键字参数，并封装到字典中'''
    print(params)

print_params_3(a="A",b=0,c="C")

def print_params_4(x,y,z=3,*pospar,**keypar):
    '''位置 + 关键字参数 + * + ** '''
    print(x,y,z)
    print(pospar)
    print(keypar)

print_params_4(1,2,4,5,6,7,foo=1,bar=2)



# =============2=============
# 参数收集的逆过程：传入list与dict
# 传入list:*
def add(x,y):
    return x+y
params = (1,2)
add(*params)    # 将list的每个元素分别传给位置参数，不能多也不能少

def hello(greeting='Hello',name="world"):
    print("%s, %s !\n" % (greeting,name))   

# 传入dict:**
params = {'name':"tp",'greeting':"hello"}
hello(**params)  # 将dict每个key-value，传入对应的关键字参数

def with_stars(**kwds):
    '''可以接受任意多个关键字参数'''
    print(kwds['name']," is ",kwds['age'])

def without_stars(kwds):
    print(kwds['name']," is ",kwds['age'])

args = {"name":"tp","age":23}
# 两处调用效果一样，说明星号只在定义和调用函数才有效
with_stars(**args)
without_stars(args)


# =============3=============
# 演示：使用拼接操作符传递参数，这样就不用关心参数的个数了
def foo(x,y,z,m=0,n=0):
    print(x,y,z,m,n)

def callFoo(*args,**kwds):  # 这里的星号是定义函数用的
    ''' *args,**kwds: 可以接受任何类型的参数 '''
    print("Calling foo!")
    foo(*args,**kwds)   # 这里的星号是调用函数用的，定义时的含义不同

callFoo(1,2,3,m=11,n=22)
callFoo(1,2,3,11,22)
