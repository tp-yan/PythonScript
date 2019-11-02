# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 17:50:52 2019

BeautifulSoup库之入门:
    BS可以对传入的“标签”文本进行解析，并以树结构返回
    Beautiful Soup库是解析、遍历、维护“标签树”的功能库
    BeautifulSoup对应一个HTML/XML文档的全部内容，同时是一个标签树
@author: 10841
"""

from bs4 import BeautifulSoup
import requests

url = "https://python123.io/ws/demo.html"
r = requests.get(url)
demo = r.text
# 'html.parser'：bs4提供的HTML解析器
soup = BeautifulSoup(demo,'html.parser') # 指定要解析的内容和解析器，返回BS对象
print(soup.prettify()) # 输出其树形结构

'''
BeautifulSoup常用解析器，都可以解析HTML和XML
解析器             使用方法                              条件
bs4的HTML解析器     BeautifulSoup(mk,'html.parser')     安装bs4库
lxml的HTML解析器    BeautifulSoup(mk,'lxml')            pip install lxml
lxml的XML解析器     BeautifulSoup(mk,'xml')             pip install lxml
html5lib的解析器    BeautifulSoup(mk,'html5lib')        pip install html5lib
'''
'''
BeautifulSoup类的基本元素
<p class=“title”> … </p>
基本元素        说明
Tag             标签，最基本的信息组织单元，分别用<>和</>标明开头和结尾
Name            标签的名字，<p>…</p>的名字是'p'，格式：<tag>.name
Attributes      标签的属性，字典形式组织，格式：<tag>.attrs
NavigableString 标签内非属性字符串，<>…</>中字符串，格式：<tag>.string
Comment         标签内字符串的注释部分，一种特殊的Comment类型
'''

print('=====================================')
# 1.获取HTML/XML中的标签tag
title = soup.title
print(title)
tag_a = soup.a # 若存在多个时，只能获取HTML中的第一个a标签
print(tag_a)
# 1.1 tag name
print(type(soup.a))
print(soup.a.name)
print(soup.a.parent.name) # 父节点
print(soup.a.parent.parent.name)
# 1.2 tag attrs：字典类型，tag无属性时，为空字典
print(soup.a.attrs)
print(soup.a.attrs['id'])
print(soup.a.attrs['class'])
print(soup.a.attrs['href'])
# 1.3 NavigableString:<tag>...</tag>标签之间的那部分内容，可对递归跨越子标签，返回标签内部的字符串
print(soup.a.string)
print(type(soup.p.string))
print(soup.p.string) # 实际内容在其子标签<b></b>中
doc = """<p>hello <b>python<!--world--></b></p><span>This is not comment</span>
<h1><!--This is comment--></h1>
"""
print('=====================================')
soup2 = BeautifulSoup(doc,'html.parser')
print(soup2.p.string) # 若一个标签包含了多个类型，则无法通过一个类型返回标签间的内容
print(soup2.b.string)
print(soup2.span.string)

# 1.4 comment：也是 通过 tag.string获得，但其类型为Comment，在爬取时需要与NavigableString区分
print(soup2.h1.string)
print(type(soup2.h1.string))

# 2.遍历HTML结构，3种遍历方式
# 2.1 下行遍历
'''
属性说明
.contents 子节点的  列表，将<tag>所有儿子节点存入列表
.children 子节点的  迭代类型，与.contents类似，用于循环遍历儿子节点
.descendants 子孙节点的  迭代类型，包含所有子孙节点，用于循环遍历
'''
print(soup.body.contents) # 标签内部的字符串被当作 字符串节点5
for child in soup.body.children:
    print(child)
# 2.2 上行遍历
'''
属性说明
.parent 节点的父亲标签
.parents 节点先辈标签的迭代类型，用于循环遍历先辈节点
'''
print(soup.html.parent) # html.parent是html标签本身
for parent in soup.a.parents:
    if parent:
        print(parent.name)

# 2.3平行遍历：只能发生在同一个父节点下的各节点间
'''
属性说明
.next_sibling 返回按照HTML文本顺序的下一个平行节点标签
.previous_sibling 返回按照HTML文本顺序的上一个平行节点标签
.next_siblings 迭代类型，返回按照HTML文本顺序的后续所有平行节点标签
.previous_siblings 迭代类型，返回按照HTML文本顺序的前续所有平行节点标签
'''
print(soup.a.next_sibling)  # 兄弟标签不一定是标签类型，可能是字符串！！！
print(soup.a.next_sibling.next_sibling)
print(soup.a.previous_sibling)
print(soup.a.previous_sibling.previous_sibling)
print(soup.a.parent)

# 3.prettify()方法
'''
.prettify()为HTML文本<>及其内容增加更加'\n'
.prettify()可用于标签，方法：<tag>.prettify()
'''
print(soup.prettify())
print('------------------------')
print(soup.a.prettify())

# 4. bs4库的编码
'''
bs4库将任何HTML输入都变成utf‐8编码
Python 3.x默认支持编码是utf‐8,解析无障碍
'''
soup3 = BeautifulSoup("<p>中文</p>","html.parser")
print(soup3.p.string)
print(soup3.prettify())