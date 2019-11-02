# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 22:09:32 2019

解约瑟夫问题:41一个人围成圆圈，从1开始报数，喊道3的人自杀，下一个从1又继续开始，知道所有人都死了
而约瑟夫和他的朋友不想死，应该将他们安排在哪两个位置上
@author: tangpeng
"""

def move(man,sep):
    '''将列表前的sep个元素移到列表末尾'''
    for i in range(sep):
        item = man.pop(0)
        man.append(item)

def play(man=41,sep=3,rest=2):
    """开始有man=41个人，喊到第sep=3的人自杀，要求剩余rest=2人"""
    print("开始有%d人，喊到%d的人自杀，最后幸存%d人" % (man,sep,rest))
    # 初始化
    man = [i for i in range(1,man+1)]
    print("玩家列表：\n",man)
    sep -= 1    # 列表需要移动的元素个数
    while len(man) > rest:
        move(man,sep)
        print("kill:",man.pop(0))   # 喊到sep的人自杀，即弹出队首元素
    return man


service = play()
print("幸存者：",service)
