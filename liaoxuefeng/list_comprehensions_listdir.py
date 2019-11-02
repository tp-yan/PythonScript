# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:57:54 2019

@author: cv
利用列表生成式，列出路径下文件和目录
"""


import os

files = [d for d in os.listdir('.')] # 当前工作路径
print(files)