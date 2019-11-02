# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 16:00:09 2019

正则表达式之Match对象:
    Match对象是一次匹配的结果，包含匹配的很多信息,只包含一个匹配字符串
Match对象的属性：
属性        说明
.string     待匹配的文本
.re         匹配时使用的patter对象（正则表达式）
.pos        正则表达式搜索文本的开始位置
.endpos     正则表达式搜索文本的结束位置

方法          说明
.group(0)     获得匹配后的字符串
.start()      匹配字符串在原始字符串的开始位置
.end()        匹配字符串在原始字符串的结束位置
.span()       返回(.start(), .end())
@author: 10841
"""

import re

pattern = r"[1-9]\d{5}"
text = "UCAS 100081 BIT 200081UTS "
m = re.search(pattern,text)
if m:
    print(m.group(0)) # 
#    print(m.groups()) # 没有使用分组匹配时，match只能匹配一个目标串
    print(type(m))
    print(m.string)
    print(m.re)  # re.compile('[1-9]\\d{5}')，再次说明 正则表达式最终都需要编译，字符串只是其表现形式
    print(m.pos)
    print(m.endpos)
    print(m.start())
    print(m.end())
    print(m.span())

# 贪婪匹配与最小匹配
# Re库默认采用贪婪匹配，即输出匹配最长的子串
match = re.search(r"PY.*N","PYANBNCNDN")
print(match.group(0))

# 输出最短的子串
'''
最小匹配操作符：只要有多种长度匹配的操作符后都可以使用？来指定为最小匹配
操作符 说明
*? 前一个字符0次或无限次扩展，最小匹配
+? 前一个字符1次或无限次扩展，最小匹配
?? 前一个字符0次或1次扩展，最小匹配
{m,n}? 扩展前一个字符m至n次（含n），最小匹配
'''

match = re.search(r"PY.*?N","PYANBNCNDN")
print(match.group(0))

