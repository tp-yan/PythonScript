# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 18:39:28 2019

递归函数,一切用递归实现的都可以用循环实现，但递归更容易理解
@author: tangpeng
"""

# 递归实现二分查找
# 标准库bisect模块已实现二分查找
def search(sequence,number,lower=0,upper=None):
    '''在有序序列sequence中查找number的位置并返回'''
    if upper is None:
        upper = len(sequence)-1
    if lower == upper:
        assert number == sequence[upper]    # 断言(假设)要找的数肯定是存在序列中的
        return upper
    else:
        middle = (upper+lower) // 2
        if number > sequence[middle]:
            return search(sequence,number,middle+1,upper)
        else:
            return search(sequence,number,lower,middle)

seq = [34, 67, 8, 123, 4, 100, 95]
seq.sort()  # list排序
print(seq)

print(search(seq,34))
print(search(seq,8))
# print(search(seq,6))  # 因为6不在序列中，执行到断言处，抛出异常AssertionError


def args_input():
    '''通过递归解决不合法输入'''
    try:
        A = float(input("输入A:"))
        B = float(input("输入B:"))
        C = float(input("输入C:"))
        return A,B,C
    except:
        print("请输入正确的值！")
        return args_input()

def main():
    print(args_input())

# 使此文件不仅可以作为库来使用，还能是可直接运行的程序
if "__main__" == __name__:
    main()
        
            