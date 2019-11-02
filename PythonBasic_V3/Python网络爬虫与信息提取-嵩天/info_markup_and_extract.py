# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 08:19:27 2019

信息标记的三种方式：XML、JSON、YAML
@author: 10841
"""

"""
XML     最早的通用信息标记语言，可扩展性好，但繁琐
        应用：Internet上的信息交互与传递
JSON    信息有类型，适合程序处理(js)，较XML简洁。key:value格式，key和value都是有类型的
        可以成为程序的一部分
        应用：移动应用云端和节点的信息通信，无注释
YAML    信息无类型，文本信息比例最高，可读性好。也是key:value格式，但是key和value都
        是无类型的
        应用：各类系统的配置文件，有注释易读
"""

"""
信息提取的一般方法
方法一：完整解析信息的标记形式，再提取关键信息
XML JSON YAML：需要标记解析器，例如：bs4库的标签树遍历

方法二：无视标记形式，直接搜索关键信息
搜索：对信息的文本查找函数即可

融合方法：结合形式解析与搜索方法，提取关键信息
XML JSON YAML 搜索：需要标记解析器及文本查找函数
"""

import requests
import re
from bs4 import BeautifulSoup

url = "https://python123.io/ws/demo.html"
r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')

# 1. <>.find_all(name, attrs, recursive, string, **kwargs)
# 1∙1 name : 对标签名称的检索字符串
print('=============== name ==============')
for link in soup.find_all('a'):
    # soup中所有a标签
    print(link)

for tag in soup.find_all(['a','b']):    # 同时查找多个标签5
    print(tag)
    
for all_tag in soup.find_all(True):     # soup中所有标签
    print(all_tag)
    
for b_tag in soup.find_all(re.compile('b')): # 正则表达式：所有包含b的标签
    print(b_tag)
    
# 1.2 attrs: 对标签属性值的检索字符串，可标注属性检索
print('=============== attrs ==============')
print(soup.find_all('p','course'))  # 属性(任何属性)值含有'course'的所有p标签
print(soup.find_all(id='link1'))    # 只按指定属性查找
print(soup.find_all(id=re.compile('link')))

# 1.3 recursive: 是否对子孙全部检索，默认True
print('=============== recursive ==============')
print(soup.find_all('a'))
print(soup.find_all('a',recursive=False)) # a不是soup的直接子标签
print(soup)

# 1.4 string: <>…</>中字符串区域的检索字符串
print('=============== string ==============')
print(soup.find_all(string = 'Python')) # 要求精确匹配
print(soup.find_all(string = re.compile('Python')))

# 注：find_all的缩写方式
'''
<tag>(..) 等价于<tag>.find_all(..)
soup(..) 等价于soup.find_all(..)
'''
print(soup(string = 'Basic Python'))

'''
扩展方法
方法                         说明
<>.find()                   搜索且只返回一个结果，同.find_all()参数
<>.find_parents()           在先辈节点中搜索，返回列表类型，同.find_all()参数
<>.find_parent()            在先辈节点中返回一个结果，同.find()参数
<>.find_next_siblings()     在后续平行节点中搜索，返回列表类型，同.find_all()参数
<>.find_next_sibling()      在后续平行节点中返回一个结果，同.find()参数
<>.find_previous_siblings() 在前序平行节点中搜索，返回列表类型，同.find_all()参数
<>.find_previous_sibling()  在前序平行节点中返回一个结果，同.find()参数
'''
print('=============== find ==============')
print(soup.find('a')) # 只返回第一个 a标签
print(soup.a.find_parent())
print(soup.a.find_parents()) # 所有先辈
