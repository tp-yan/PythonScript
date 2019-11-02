# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 13:57:09 2019
for循环与range函数
@author: tangpeng
"""

# for：常用于遍历集合！
a = range(5)    # 返回的是一个容器
print(a)
print(type(a))  # <class 'range'>

# 将容器中的序列转为list
print(list(a))
# 将容器中的序列转为tuple
print(tuple(a))

i = 2
for i in range(5):
    print(i)
print() # 默认输出换行

for j in range(2,5):    # 自定义起始索引号
    print(j)

print(j,"\n")    # 全局的作用域，不限于for循环内

# range按指定步长生成序列
for j in range(2,10,2):
    print(j)
    
    