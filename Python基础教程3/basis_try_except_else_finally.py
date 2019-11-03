# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 14:59:56 2019

Python异常处理机制
@author: tangpeng
"""

try:
    print("try后面接可能产生异常的代码块")
    1 / 0
except AttributeError:
    print("捕获AttributeError类型的except块")
except ZeroDivisionError as e:  # 得到捕获的异常对象
    print(e)
except:
    # 字符串换行时，需要在上行末尾添加‘\’
    print("可选部分。产生了异常，且上述的所有except都没有捕获到，则执行except:中的代码，\
          如果产生了异常且没有捕获也没有except:模块，则抛出由Python去处理")
else:
    print("可选部分。若try中没有发送异常，则执行else:中的代码")
finally:
    print("可选部分。finally:块一定被执行,用于关闭打开的数据库、文件、网络资源等")

print("捕获异常后，后续程序继续执行，不会立刻终止")

