#!/usr/bin/env python3
# -*- coding: utf-8 -*-



"""
此处是模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；

文档第1行注释可以让这个 .py 文件直接在Unix/Linux/Mac上运行
文档第2行注释表示.py文件本身使用标准UTF-8编码

Created on Fri Oct 18 14:33:59 2019

@author: cv
"""

__author__ = "tangpeng" 

import sys

def test():
    args = sys.args # 用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
    if len(args) == 1:
        print("hello,world!")
    elif len(args == 2):
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


# 当在命令行运行 此模块文件时，Python解释器把一个特殊变量__name__置为__main__
if __name__ == "__main__":
    test()