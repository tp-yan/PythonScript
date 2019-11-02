# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 11:38:54 2019

作为模块测试用
@author: 10841
"""
print("hello,python")

def hello():
    print("hello")


def test():
    print("inner module test")

# 作为主程序执行的模块名为 '__main__'，作为模块导入到其他程序中其"__name__"为模块名
# 故要在模块中写测试代码应如下：
if __name__ == "__main__":
    test()