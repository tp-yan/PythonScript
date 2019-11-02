#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 09:30:27 2019

@author: tangpeng

正则表达式的2个功能:
    1. 匹配字符串 
    2. 切分字符串
"""

import re

"""
1. 匹配字符串
"""
test1 = '010-12345'
test2 = '010    12345'
test3 = '010 - 12345'
test4 = '010 -- 12345'
# 匹配成功返回match对象，否则返回None
mobj = re.match(r'\d{3}(\s\-\s|\-|\s+)\d{5}',test1)
print(mobj)
print(mobj.groups())
mobj = re.match(r'\d{3}(\s\-\s|\-|\s+)\d{5}',test2)
print(mobj)
mobj = re.match(r'\d{3}(\s\-\s|\-|\s+)\d{5}',test3)
print(mobj)
print(mobj.groups())
mobj = re.match(r'\d{3}(\s\-\s|\-|\s+)\d{5}',test4) 
print(mobj)


test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')
    
"""
2. 切分字符串：比使用固定的字符串更灵活
"""
s1 = 'a b   c'
print(s1.split(' '))
# 使用正则表达式识别连续的空格
print(re.split(r'\s+',s1))
# 加入 , 分隔符(需要转义)：
s2 = 'a,b, c  d'
print(re.split(r'[\s\,]+',s2))
# 再加入`;`试试：
s3 =  'a,b;; c  d'
print(re.split(r'[\s\,\;]+',s3))

"""
3. 分组
用于提取子串。用`()`表示的就是要提取的分组（Group）
"""
rex = r'^(\d{3})-(\d{3,8})$'
m = re.match(rex,'010-12345')
print(m.groups()) # 不包含待匹配字符串本身
print(m.group(0)) # 永远是待匹配字符串本身
print(m.group(1))
print(m.group(2))

# 匹配时间的正则表达式
hour_rex = r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$'
t1 = '19:05:30'
t2 = '9:05:5'
print(re.match(hour_rex,t1).groups())
print(re.match(hour_rex,t2).groups())

# 日期正则表达式
date_rex = r'^(0[1-9]|1[0-2]|[0-9])-(0[1-9]|1[0-9]|2[0-9]|3[0-1]|[0-9])$'
# 注：对于`'2-30'`，`'4-31'`这样的非法日期，用正则还是识别不了，或者说写出来非常困难，这时就需要程序配合识别了。

"""
4. 贪婪匹配
正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。
非贪婪匹配：在默认添加 ? 即可
"""
# 匹配出数字后面的0：
regx = r'(\d+)(0*)$'
s = "102300"
print(re.match(regx,s).groups()) # 由于`\d+`采用贪婪匹配，直接把后面的0全部匹配了，结果`0*`只能匹配空字符串了。
# 加个`?`就可以让`\d+`采用非贪婪匹配
regx = r'(\d+?)(0*)$'
print(re.match(regx,s).groups())

"""
5. 编译
python中使用正则表达式都需要先编译正则表达式后，才能去匹配字符串。
如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配。
"""
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$') # 编译后生成`Regular Expression`对象
print(re_telephone.match('010-12345').groups()) # 由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串。
print(re_telephone.match('010-8086').groups())


"""
练习
请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
someone@gmail.com
bill.gates@microsoft.com
"""
def is_valid_email(addr):
    regx = r'\w+\.?\w+@\w+\.\w+'
    return True if re.match(regx,addr) != None else False

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

"""
版本二可以提取出带名字的Email地址：
<Tom Paris> tom@voyager.org => Tom Paris
bob@example.com => bob
"""
def name_of_email(addr):
    regx = r'(<(.+)>\s*\w+|(\w+))@\w+\.\w+'
    r = re.match(regx,addr).groups()
    return r[2] if r[1] == None else r[1]

# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
