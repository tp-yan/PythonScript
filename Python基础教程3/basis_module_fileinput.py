# -*- coding: utf-8 -*-                            #  1
"""                                                #  2
Created on Sun Jul  7 14:42:20 2019                #  3
                                                   #  4
标准库之fileinput                                          #  5
                                                   #  6
@author: 10841                                     #  7
"""                                                #  8
                                                   #  9
import fileinput                                   # 10
                                                   # 11
for line in fileinput.input(inplace=True):         # 12 默认从控制台参数读取文件行，也可指定文件路径参数
    line = line.rstrip()                           # 13 inplace=True：直接在原文件上修改
    num = fileinput.lineno()                       # 14
    print("{:<50} # {:2d}".format(line,num))       # 15 必须使用print将内容写入文件
                                                   # 16
