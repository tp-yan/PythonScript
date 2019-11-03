# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 09:12:27 2019

标准库之 re
@author: 10841
"""




# 示例：提取所有的邮件地址
import fileinput,re

pat = re.compile(r'[a-z0-9\-\.]+@[a-z0-9\-\.]+',re.IGNORECASE)
address = set() # 存放邮件地址，去除重复地址

for line in fileinput.input():
    for addr in pat.findall(line): # 找到所有匹配的子串
        address.add(addr)
        
for addr in sorted(address):
    print(addr)
    
