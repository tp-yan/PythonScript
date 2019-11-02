#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:00:27 2019

@author: tangpeng

操作文件和目录练习
2. 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
"""
import os 

def find_file(cur_path,target_str):
    for f in os.listdir(cur_path):
        if os.path.isfile(f):
            if target_str in f:
                print(os.path.join(cur_path,f))
        elif os.path.isdir(f):
            find_file(os.path.join(cur_path,f),target_str)
            

find_file(".","test")
