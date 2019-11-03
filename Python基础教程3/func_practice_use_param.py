# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 17:00:05 2019
练习使用函数参数
@author: tangpeng
"""

def story(**kwds):
    return 'Once upon a time, there was a %(job)s called %(name)s.' % kwds

def power(x,y,*others):
    if others:
        print('Received redunrant params:',others)
    return pow(x,y)

def interval(start,stop=None,step=1):
    '''模拟range()函数'''
    if stop is None:    # 或 stop == None
        start, stop = 0, start
    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step
    return result

print(story(job="king",name="tp"))
print(story(name="zhangsan",job="miner"))
params = {'job':'teacher','name':'wanger'}
print(story(**params))
del params['job']   # 删除key-value
print(story(job="joker",**params))

print(power(3,2))
print(power(2,3))
print(power(y=3,x=2))
params = (5,) * 2
print(params)   # (5,5)
print(power(*params))
print(power(3,4,"hello"))

print(interval(10))
print(interval(1,5))
print(interval(3,14,4))
print(power(*interval(3,7)))
