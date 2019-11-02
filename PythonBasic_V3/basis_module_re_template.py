# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 19:24:37 2019

标准库之 re：模板系统
模板：一种文件，可插入具体的值来得到最终的文本
@author: 10841
"""

# 一个简单的模板系统
import fileinput, re

# 匹配方括号里的内容
field_pat = re.compile(r'\[(.+?)\]')

# 字典：变量的命名空间即作用域
scope = {}

# 被 re.sub调用处理匹配字符串的函数
def replacement(match):
    code = match.group(1)
    try:
        # 如果字段为表达式则返回其结果
        return str(eval(code,scope)) # 限定在scope命令空间中执行code
    except SyntaxError:
        # 否则在当前作用域中执行赋值语句
        exec(code,scope)
        return ""

# 将文本内容合成一个字符串
lines = []
for line in fileinput.input():
    lines.append(line)
text = "".join(lines) # 这种方式比 += 快，+=：每次会创建新的字符串对象

# 替换所有匹配的字符串内容
print(field_pat.sub(replacement,text))
 
