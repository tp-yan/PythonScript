#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
import re
'''
    someone@gmail.com
    bill.gates@microsoft.com



def is_valid_email(addr):
	if re.match(r'\w+(\.\w+)*@\w+\.com',addr):
		return True
	return False
	
	
# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')
'''

'''
版本二可以提取出带名字的Email地址：
    <Tom Paris> tom@voyager.org => Tom Paris
    bob@example.com => bob
'''

s2 = r'<?([\w\s.\]+)>?([\w\s._]+)?@[\w\s.]+'
def name_of_email(addr):
	if re.match(r'<\w+\s\w+>\s\w+@\w+\.\w+',addr):
		return re.match(r'<(\w+\s\w+)>\s\w+@\w+\.\w+',addr).group(1)
	elif re.match(r'\w+@\w+\.\w+',addr):
		return re.match(r'(\w+)@\w+\.\w+',addr).group(1)
		
# 测试:

print(name_of_email('<Tom Paris> tom@voyager.org'))
print(name_of_email('tom@voyager.org'))
print(name_of_email('bob@example.com'))
'''
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
r'(<(\w+\s\w+)>\s\w+|(\w+))@\w+\.\w+'
'''
