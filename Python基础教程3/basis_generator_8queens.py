# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 10:51:17 2019

生成器之使用递归生成器解决八皇后问题
@author: 10841
"""

def conflict(state,nextX):
    """
    state:元组，保存了之前所有皇后的位置信息。索引号代表行，值代表该行的皇后所选位置，
    都是从0开始。
    nextX：x坐标，即将要选择的列
    判断当前列位置，是否与之前的皇后冲突
    """
    nextY = len(state) # 当前皇后的行
    for i in range(nextY): # 遍历之前所有的皇后
        if abs(nextX - state[i]) in (0, nextY - i):
        # 0:不能同列，nextY - i:不能位于对角线上
            return True
    return False


def queens(num=8, state=()):
    for pos in range(num): # 遍历每个列位置
        if not conflict(state,pos):
            if len(state) == num-1: # 最后一行，返回可行列位置即可
                yield (pos,) 
            else: # 否则进入下一个，即下一个皇后选位置
                for result in queens(num, state + (pos,)):
                    # result包括下一个皇后到最后一个皇后可行位置的元组
                    yield (pos,) + result # 在第一层的皇后这里，返回所有可行解
                    
def prettyprint(solution):
    '''打印皇后的位置'''
    def line(pos,length=len(solution)): # 打印一行
        return '·'*(pos) + 'X' + '·'*(length-pos-1)
    for pos in solution:
        print(line(pos))

print(list(queens(4)))

import random
prettyprint(random.choice(list(queens(8)))) # 随机选择一个解打印输出
print("8皇后总共有",len(list(queens(8))),"个解")
        
        