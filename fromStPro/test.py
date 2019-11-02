# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 14:46:34 2019

@author: tangpeng


"""

import random
import numpy as np

A = np.array([[1,2],[3,4],[5,6]])
B = np.array([[1,2],[3,4],[5,6]])

A = ['a','b','c','d','e']
B = ['a','b','c','d','e']
print(A,B)
index = random.sample(A,3)

NUM_SAMPLE = 10
index = np.arange(0,NUM_SAMPLE)
random.shuffle(index)
C = np.array(list(range(0,20)))
D = C[index[:3]]
'''
tmp = np.ones_like(index)
print(tmp)
index -= tmp
print(index)



A_array = np.array(A)
B_array = np.array(B)

print(A_array[index])
print(B_array[index])


'''