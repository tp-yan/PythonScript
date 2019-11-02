#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 17:06:54 2019

@author: tangpeng

向python脚本传控制台参数
当在控制台输入： python args_2_py_script.py --help 时，会出现：
usage: args_2_py_script.py [-h] -i IMAGE -o OUTPUT [-p PREFIX]

optional arguments:
  -h, --help            show this help message and exit
  -i IMAGE, --image IMAGE
                        path to the input image
  -o OUTPUT, --output OUTPUT
                        path to output directory to store augmentation
                        examples
  -p PREFIX, --prefix PREFIX
                        output filename prefix
"""

# 1. 方式一
import argparse

# 设置参数以及要求，会在 --help时显示
parser = argparse.ArgumentParser() # 用于解析命令行字符串参数
parser.add_argument("-i","--image",required=True,help="path to the input image") # required未输入时会提示error
parser.add_argument("-o","--output",required=True,help="path to output directory to store augmentation examples")
parser.add_argument("-p","--prefix",type=str,default="image",help="output filename prefix")
namespace = parser.parse_args() # 解析命令行参数
print(namespace,type(namespace)) # Namespace(image='./img.jpg', output='./', prefix='image') <class 'argparse.Namespace'>
print(namespace.__dict__) # 与vars()效果一样
args = vars(namespace) # 如果对象具有__dict__属性，则vars（）函数返回给定对象的__dict__属性
print(args['image'],type(args['image']))
print(args['output'],type(args['output']))

# 2. 方式二
import sys
print(sys.argv[0]) # args_2_py_script.py
print(sys.argv[1]) # -i 
print(sys.argv[2]) # -o
