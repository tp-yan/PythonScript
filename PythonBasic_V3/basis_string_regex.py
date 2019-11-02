# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 13:15:48 2019

字符串之正则表达式:
正则表达式：一个字符串来描述、匹配一系列符合某个句法规则的字符串，其本身是一个字符串
正则表达式是一种通用的字符串表达框架
正则表达式是一种针对字符串表达“简洁”和“特征”思想的工具
正则表达式可以用来判断某字符串的特征归属
正则表达式在文本处理中十分常用：
    表达文本类型的特征（病毒、入侵等）
    同时查找或替换一组字符串
    匹配字符串的全部或部分
    最主要应用在字符串匹配中
编译：将符合正则表达式语法的字符串转换成正则表达式特征.
     将正则表达式的字符串形式编译成正则表达式对象

re模块：包含了所有正则表达式的功能
re库采用raw string（原生字符串类型）类型表示正则表达式，表示为：
例如： 
r'[1‐9]\d{5}'     
r'\d{3}‐\d{8}|\d{4}‐\d{7}'
raw string是不包含对转义符再次转义的字符串,若使用string类型表示正则字符串，
因为string将'\'看作转义符，需要更繁琐的表示方法：
例如：
'[1‐9]\\d{5}'
'\\d{3}‐\\d{8}|\\d{4}‐\\d{7}'
故表示正则表达式时，一律使用 r'text'

@author: 10841
"""

import re

# 1.re.match方法：判断模式串与目标串是否匹配
# '\-':转移特殊字符'-'，'^':代表开始的字符或者子表达式
pattern = r'^\d{3}\-\d{3,8}$' # 最好使用 'r'前缀的字符串来表示正则表达式，这样就不用考虑转义字符
# 若不在模式串结尾添加'$'，则其尾部相当于添加了'.*'
target1 = '021-12345'
target2 = '021 12345'
print(re.match(pattern,target1))    # 匹配成功返回 一个Match对象
print(re.match(pattern,target2))    # 匹配失败返回None

# 2.re.split:使用正则表达式切分字符串,对split功能的加强
# 原始split
s = 'a b   c'
print(s.split(' ')) # 只以' '作为分隔符，无法处理连续空格
print(s.split())    # 默认可以处理连续空格
print(re.split(r'\s+',s))
# 多个字符作为分隔符, []:匹配其中任一字符，'\,'：对','的转义
print(re.split(r'[\s\,]+','a,b, c  d'))
print(re.split(r'[\s\,\;]+','a,b,;;c  ;d'))

# 3. ^与$
regex = r'^py$' # $:表示从字符串的末端匹配。这里必须是py开始和结束，中间不能有任何其他字符
print(re.match(regex,'python'))
print(re.match(regex,'py'))
print(re.match(regex,'pypy'))   # None,不匹配

# 4.分组：提取子串，使用()表示的即是要提取的分组
pattern = r'^(\d{3})-(\d{3,8})$'
m = re.match(pattern,target1)
print(m.groups()) # 返回提取的子串
print(m.group(0)) # 永远是目标字符串本身
print(m.group(1)) # 提取的第一个子串
print(m.group(2)) # 提取的第二个子串
# 嵌套分组
target = 'tree/combined 010-12345'
pattern = r'(([^/]*)(/.*)?)[\s]+((\d{3})\-(\d{3,8})$)' # [^]：匹配除了里面列出的任一字符
m = re.match(pattern,target)
print(m.groups())
print(m.group(1))   # 首先匹配最外层的()
print(m.group(2))   # 然后依次匹配里层的分组
print(m.group(3))
print(m.group(4))   # 同理，从左往右依次匹配，若()里面还有分组就递归下去匹配分组
print(m.group(5))
print(m.group(6))

# 5.贪婪匹配：默认尽可能多的匹配字符
print(re.match(r'^(\d+)(0*)$','102300').groups()) # (\d+)匹配所有的数字，导致(0*)无法匹配到0
# 非贪婪匹配：(\d+?)，?用在+,*,{0,}这种可无限匹配的情况
print(re.match(r'^(\d+?)(0*)$','102300').groups())

# 6.编译正则表达式
# 使用re模块的正则表达式匹配方法时，第一步先编译正则表达式，检查语法错误；
# 第二步用编译后的正则表达式去匹配目标串
# 若重复使用一个模式串，则可以预编译模式串，以后直接使用来匹配目标串
# 返回Pattern对象，保存了模式串
re_telephone = re.compile(r'^(\d{3})\-(\d{3,8})$')
print(type(re_telephone))
# 编译后直接使用
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups())

# 7.表示IP地址
''' 
思想：每一段都是0-255，只需表示一段然后重复四次即可
如何表示0-255？ 解：将0-255区间分段表示
0-99: [1-9]{1,2} 
100-199: 1\d{2}
200-249: 2[0-4]\d
250-255: 25[0-5]
'''
IP_regx = "(([1-9]{1,2}|1\d{2}|2[0-4]\d|25[0-5]).){3}([1-9]{1,2}|1\d{2}|2[0-4]\d|25[0-5])"

'''
操作符   说明                            实例
.       表示任何单个字符
[ ]     字符集，对单个字符给出取值范围      [abc]表示a、b、c，[a‐z]表示a到z单个字符
[^ ]    非字符集，对单个字符给出排除范围    [^abc]表示非a或b或c的单个字符
*       前一个字符0次或无限次扩展          abc* 表示ab、abc、abcc、abccc等
+       前一个字符1次或无限次扩展          abc+ 表示abc、abcc、abccc等
?       前一个字符0次或1次扩展            abc? 表示ab、abc
|       左右表达式任意一个                abc|def 表示abc、def

{m}     扩展前一个字符m次                 ab{2}c表示abbc
{m,n}   扩展前一个字符m至n次（含n）        ab{1,2}c表示abc、abbc
^       匹配字符串开头                    ^abc表示abc且在一个字符串的开头
$       匹配字符串结尾                    abc$表示abc且在一个字符串的结尾
( )     分组标记，内部只能使用|            操作符(abc)表示abc，(abc|def)表示abc、def
\d      数字，等价于[0‐9]
\w      单词字符，等价于[A‐Za‐z0‐9_]
注：只有'|'的选择单位是表达式，其他都指的是 单个字符
{:3}:表示0~3次

经典正则表达式实例            ^[A‐Za‐z]+$
由26个字母组成的字符串        ^[A‐Za‐z0‐9]+$
由26个字母和数字组成的字符串   ^‐?\d+$
整数形式的字符串              ^[0‐9]*[1‐9][0‐9]*$
正整数形式的字符串            [1‐9]\d{5}
中国境内邮政编码，6位         [\u4e00‐\u9fa5]
匹配中文字符                 \d{3}‐\d{8}|\d{4}‐\d{7}
国内电话号码                 010‐68913536
'''
'''
re库中的函数
函数             说明
re.search()     在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象
re.match()      从一个字符串的开始位置起匹配正则表达式，返回match对象
re.findall()    搜索字符串，以列表类型返回全部能匹配的子串
re.split()      将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
re.finditer()   搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象
re.sub()        在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串
'''

# A. re.serach()
target = "BIT 100081 200081"
pattern = r'[1-9]\d{5}'
match = re.search(pattern,target)
if match:
    print(match.group(0)) #
    print(match.groups()) # 空.只能匹配一个
    
# B. re.match()
target1 = "100081 BIT 200081UTS "
match = re.match(pattern,target)
if match:
    print(match.groups()) # 必须从开头就匹配，不然无法匹配
    
match1 = re.match(pattern,target1)
if match1:
    print(match1.group(0))
   
# C. re.findall():返回list对象
ls = re.findall(pattern,target1)
print(ls)

# D. re.split():将匹配的字符串作为分隔符进行分割，返回list。
# maxsplit:指定最多匹配的子串，也就是分割出来的字符串个数，剩余的字符串不再进行匹配也不再分割
ls = re.split(pattern,target1)
print(ls)
ls = re.split(pattern,target1,maxsplit=1)
print(ls) # 只分出一个元素，剩余字符串保留不再分割

# E. re.finditer():
for m in re.finditer(pattern,target1): # 返回迭代对象，每个元素是match对象
    if m:
        print(m.group(0))
        
# F. re.sub():新串替换匹配串，返回替换后的串
s = re.sub(pattern,'这是替换串',target1)
print(s)
