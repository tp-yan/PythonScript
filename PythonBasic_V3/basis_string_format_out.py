# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 13:09:42 2019

字符串之格式输出
@author: 10841
"""

# 1. 最原始格式输出： % :左边指定一个格式化字符串，右边指定要格式化的值
format_str = 'Hello, %s . %s enough for you ya?'
values = 'world','Hot'
print_s = format_str % values
print(print_s)
print(format_str % values)

# 2. 模板字符串 Template
from string import Template
tmp1 = Template('Hello, $who! $what enough for ya?')
sentence = tmp1.substitute(who='Mars',what='Dusty')
print(sentence)
print(tmp1.substitute(who='Tom',what='Money'))

# 3. 推荐：强大的字符串方法 format
# 每个替换字段都对应一个{}，在{}里面可包含名称，对值如何转换，格式设置等信息
s = '{},{} and {}. '.format('first','second','third')
print(s)
# 索引指向填充值的位置
s = '{0},{1} and {2}'.format('1st','2nd','3rd')
print(s)
# 索引顺序可以任意，解决填充值重复问题
s = "{3} {0} {2} {1} {3}".format('be','not','or','to')
print(s)

from math import pi,e
# 命名字段与模板使用一样
# {value:.2f}：格式说明符
s = '{name} is approximately {value:.2f}.'.format(value=pi,name='π')
print(s)
# 若命名字段名称与变量相同，则有如下简写
s = f"Euler's constant is roughly {e}" # 导入的 e变量与命名字段相同名称
print(s)
print("Euler's constant is roughly {e}".format(e=e))
# 在格式字符串中输出{}：{{}}
print("{{hello,python}}".format())

# 完整的字符串格式输出：都是调用format方法
# 替换字段{}包括：字段名、转换标志、格式说明符，都是可选’
# 字段名：索引或标识符
# 转换标志：叹号后面的字符，只有3种：s(str),r(repr),a(scii)
# 格式说明符：指定输出类型，字段宽度，精度，显示符号，千位分隔符等
# 1. 替换字段名
s = "{foo} {} {bar} {}".format(1,2,bar=4,foo=3)     # 自动编号
print(s)
s = "{foo} {1} {bar} {0}".format(1,2,bar=4,foo=3)   # 手动编号
print(s)
# 访问输出值得组成部分，如同在常规python代码中使用一样
fullname = ['Stephen','Curry']
s = "Mr {name[1]} ".format(name=fullname)   # 相当于把 fullname传给局部变量name
print(s)
import math
s = "The {mod.__name__} module defines the value {mod.pi} for π".format(mod=math)
# mod指向了math模块,__name__:模块的名称
print(s)
# 2.基本转换：转换标志
print("{pi!s} {pi!r} {pi!a} ".format(pi='π'))
# 分别使用str(),repr(),a:以其ascii值，对输入值进行转换后输出
print(ascii('a'))

# 指定输出类型
print("The number is {num}".format(num=42))
print("The number is {num:f}".format(num=42)) # 将整数以定点小数格式输出
print("The number is {num:b}".format(num=42)) # 整数以二进制格式输出
print("The number is {num:c}".format(num=4332)) # 输出Unicode字符集对应的字符
print("The number is {num:e}".format(num=42)) # 科学记数法输出
print("The number is {num:g}".format(num=42)) # g:自动确定是用科学技术e还是定点f输出小数
print("The number is {num:%}".format(num=42)) # 百分数格式：乘100，再用f格式输出
print("The number is {num:o}".format(num=42)) # 8进制
print("The number is {num:x}".format(num=42)) # 16进制


# 3.宽度、精度和千分位分隔符
print("{num:10}".format(num=3)) # 指定宽度,数字默认右对齐
print("{num:10}".format(num='Non')) # 指定宽度，字符串默认左对齐
print("{pi:.2f}".format(pi=pi)) # 指定精度：前面必须添加小数点。f指定的是小数点后的位数
print("{pi:.2f}".format(pi=3)) # 指定精度：指定的是小数点后的位数
print("{pi:.2}".format(pi=pi)) # 指定精度：默认指定的是有效位数
print("{pi:10.2f}".format(pi=pi)) # 宽度+精度
print("{:.5}".format("Guido van Rossum")) # 对其他类型指定精度。格式说明符必须写在':'后面

# 使用逗号添加千分位分隔符
print("one googol is {:,}".format(10**100))
# 逗号应位于 宽度和精度的小数点之间
print("one googol is {:10,.2f}".format(10**10))

# 4.符号、对齐和0填充
# 在指定宽度和精度前面添加一个标志：0、+、-或空格
print("{:010.2f}".format(pi))
# 左对齐、右对齐、居中：<、>、^
print("{0:<10.2f} \n{0:^10.2f} \n{0:>10.2f}".format(pi))
# 使用其他字符扩充对齐说明符，而非默认的空格来填充
print("{:$^15}".format(' Will '))

print("{0:10.2f} \n {1:10.2f}".format(pi,-pi))
# =:将填充字符放在 符号和数字之间
print("{0:10.2f} \n {1:=10.2f}".format(pi,-pi))
# 给数字添加+号:放在对齐说明符后面
print("{0:-.2} \n {1:-.2}".format(pi,-pi)) # 默认设置
print("{0:+.2} \n {1:+.2}".format(pi,-pi)) 
print("{0: .2} \n {1: .2}".format(pi,-pi)) 

# ‘#’:放在符号说明符和宽度之间,将触发另一种转换方式,随类型而异
print("{:b}".format(42))
print("{:#b}".format(42))
print("{:g}".format(42))
print("{:#g}".format(42))

# 简单应用：根据输入的宽度打印 格式良好的价格列表
width = int(input('please enter width:')) # 列表总宽度
price_width = 10
item_width = width - price_width
# 动态指定宽度和字符串右对齐
header_fmt = '{{:{}}}{{:>{}}}'.format(item_width,price_width)
fmt = '{{:{}}}{{:>{}.2f}}'.format(item_width,price_width)

print('='*width)
print(header_fmt.format('Item','Price'))
print('-'*width)

print(fmt.format('Pears',0.5))
print(fmt.format('Apples',0.4))
print(fmt.format('Cantaloupes',1.84))
print(fmt.format('Dried Apricots',8.0))
print(fmt.format('Prunes(4 lbs.)',12.00))

print('='*width)
