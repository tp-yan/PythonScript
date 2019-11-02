# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 16:11:19 2019

字符串之字符串方法：字符串类的方法基本涵盖了'string'模块中的函数，
但是string模块中还有许多常用的常量

@author: 10841
"""

# string模块中的常量
import string
print(string.digits)    # 包含数字0-9的字符串
print(string.ascii_letters)   # 所有ASCII字母 
print(string.ascii_lowercase)    # 小写ASCII字母
print(string.ascii_uppercase)    
print(string.punctuation)    # 所有ascii标点字符
print(repr(string.printable))     # 所有可打印的 ASCII字符    

# 1.center：在两边填充字符（默认空格），让字符串居中
# 其他：ljust,rjust,zfill
print()
print("The middle by Jimmy Eat world".center(39,'*'))
# 2.find：查找子串，并返回第一个字符的索引，而‘in’只判断是否包含子串
# 其他：count,startswith,endswith,index,rindex,rfind
s = "With a monn-monn here, and a moo-moo there"
print(s.find('moo'))
print(s.find('python'))
# 限定查找范围
subject = "$$$ Get rich now !!! $$$"
print(subject.find('$$$',1))    # 只指定起点
print(subject.find('$$$',0,16))    

# 3.join:与split刚好相反，合并的所有元素都必须是字符串
seq = [str(i) for i in range(1,6)]
sep = '+'
sep.join(seq)
print(seq)
dirs = '','usr','bin','env'
# unix路径
print('/'.join(dirs))
# wins路径
print('C:'+'\\'.join(dirs))

# 4.lower
# 其他：islower,istitle,isupper,trnslate
# capitalize,casefold,swapcase,title,upper
print('ABCd'.lower())
# 最好在存储与搜索字符串时，都以小写格式
# title:将所有词首大写
print("that's all, folks".title()) # 这种情况使用title会出现结果不理想
# 使用string模块的 capwords函数
print(string.capwords("that's all, folks"))

# 5.replace:子串替换，返回替换结果
# 其他：expantabs
print('This is a test'.replace('is','eez'))

# 6.split:字符串拆分为序列
# 其他：partition、rpartition、rsplit、splitlines
print('1+2+3+4+5'.split('+'))
print('using    default   punctuation'.split()) # 默认在连续的几个空白符处拆分

# 7.strip:去除开头、结尾的空白符
print(' internal whitespace is kept   '.strip())
# 指定删除开末尾的多个 字符，中间字符不受影响
print('*** spam * for * everyone !!! ***'.strip(' *!'))
# strip、lower一般用于处理用户输入字符串

# 8.translate:只能进行单字符替换，但同时可替换多个字符，效率比replace高
# 使用前需要创建 转换表：指定字符之间一一对应的替换关系
table = str.maketrans('cs','kz') # 即 k替换c, z替换s。也可以直接传入dict
print(type(table))
print(table)    # 转换表实际就是 dict ，实际就是字符的Unicode码字映射关系
s = 'this is an incrediable test'
print(s.translate(table))
print(s.translate(str.maketrans('cs','kz',' '))) # 第三个参数指定要删除的字符
# 传入字典时可将要删除的那些字符映射成 None
table = str.maketrans({'c':'k','s':'z','i':None,'a':None})
print(s.translate(table))

# 9.判断字符串是否满足特定条件的方法： 以 is 开头’
'''
isalnum,isalpha,isdecimal,isdigit,isidentifier,islower,isnumeric,isprintable,
isspace,istitle,isupper
'''

# 10.capitialize:句首字母大写
s = 'Hello World'
print(s.capitalize())
# 11.casefold：所有大写字符变小写
print(s.casefold()) 