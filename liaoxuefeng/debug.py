#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:22:06 2019

@author: tangpeng

调试
"""

"""
1. 断言
凡是用print()来辅助查看的地方，都可以用断言（assert）来替代,如果断言失败，assert语句本身就会抛出AssertionError。
启动Python解释器时可以用-O参数（英文大写字母O）来关闭assert： python -O err.py 
"""
def foo(s):
    n = int(s)
    assert n != 0, "n is zero" # assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。

def main():
    foo('0')

#main() # AssertionError: n is zero

"""
2. logging
把print()替换为logging，和assert比，logging不会抛出错误，而且可以输出到文件：
logging.basicConfig(level=logging.INFO) 指定记录信息的级别，有debug，info，warning，error等几个级别，
当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。
logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。
"""
import logging
logging.basicConfig(level=logging.INFO) # 控制logging输出等级，默认不输出
s = "0"
n = int(s)
logging.info("n = %d" % n) # logging.info()就可以输出一段文本
print(10/n)
"""
# 在控制台会有logging输出，在IPython下没有
python debug.py 
INFO:root:n = 0
Traceback (most recent call last):
  File "debug.py", line 34, in <module>
    print(10/n)
ZeroDivisionError: division by zero
"""




"""
3. pdb
Python的调试器 pdb ，让程序以单步方式运行，可以随时查看运行状态:
python -m pdb err.py # 以参数-m pdb启动 pdb
> d:\project\pythonproject\script\err.py(9)<module>()
-> '''
(Pdb) l # 输入命令l来查看代码：
  4     Created on Tue Oct 22 15:26:08 2019
  5
  6     @author: tangpeng
  7
  8     err.py:用于调试测试的模块
  9  -> '''
 10
 11     s = '0'
 12     n = int(s)
 13     print(10 / n)
[EOF]
(Pdb) n # 输入命令n可以单步执行代码
> d:\project\pythonproject\script\err.py(11)<module>()
-> s = '0'
(Pdb) n
> d:\project\pythonproject\script\err.py(12)<module>()
-> n = int(s)
(Pdb) n
> d:\project\pythonproject\script\err.py(13)<module>()
-> print(10 / n)
(Pdb) p s # 任何时候都可以输入命令p 变量名来查看变量：
'0'
(Pdb) p n
0
(Pdb) n
ZeroDivisionError: division by zero
> d:\project\pythonproject\script\err.py(13)<module>()
-> print(10 / n)
(Pdb) q # 输入命令q结束调试，退出程序
"""

"""
`pdb.set_trace()`：这个方法也是用pdb，但是不需要单步执行，我们只需要`import pdb`，
然后，在可能出错的地方放一个`pdb.set_trace()`，就可以设置一个断点：
"""