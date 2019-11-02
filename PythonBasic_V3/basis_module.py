# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 11:36:54 2019

模块：就是程序，任何python程序都可作为模块导入
模块只会在导入时执行一次，后续再导入不会再执行，因为模块本身就是用来定义的
__pycache__目录：处理后的模块文件，以便快速再次导入模块.
模块具有作用域，在其中定义的类，函数，变量等都是模块的属性.模块是重用代码的重要方式
@author: 10841
"""

import sys

# 加入 path环境变量
sys.path.append(r'C:\Users\10841\Documents\Python Scripts\Python基础教程3')

import hello
import hello

import importlib
hello = importlib.reload(hello) # 重新导入模块，会再次执行，并替换掉之前的模块
hello.hello()

import pprint
# python解释器如何找到自己的模块
# 1.放到python解释器的目录下
pprint.pprint(sys.path) # python解释器寻找包的目录，一般将自己的包存在site-packages目录下

# 2.告诉解释器去指定的地方查找：将模块所在目录存于环境变量PYTHONPATH中即可


#================sys模块=================
# 将命令行参数反序输出
print(sys.argv[0])
print(" ".join(reversed(sys.argv[1:]))) # argv[0]:脚本名称

#================os模块=================
import os
print(os.environ) # 操作系统所有环境变量
print(os.environ['PYTHONPATH']) # 访问PYTHONPATH环境变量
print(os.environ['PATH'])
print(os.sep)   # 路径分隔符
print(os.pathsep)   # 多个路径分隔符，Linux是':'，Win下是';'
pprint.pprint(os.linesep) # 行分隔符

import webbrowser # 专门用于启动浏览器的模块
webbrowser.open("http://www.baidu.com") # 使用系统默认浏览器打开URL



