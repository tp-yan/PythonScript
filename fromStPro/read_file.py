#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#请将本地一个文本文件读为一个str并打印出来：

fpath = r'/home/tp/文档/python学习/test'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)
