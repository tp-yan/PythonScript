# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 18:46:22 2019

网络爬虫：按照一定的规则，自动爬取Web信息的程序或脚本
网络爬虫执行流程：1.获取网页源码 2.从源码中提取信息 3.进行数据存储
@author: 10841
"""

# 1.获取网页源码
# 由内置的 urllib.request模块 获取网页的字节码，再解码后得到源码字符串
from urllib import request
import chardet
import sqlite3

url = 'http://www.nuc.edu.cn'
fp = request.urlopen(url)
content = fp.read()
fp.close()
print(type(content)) # 读到的是字节码
# 字节码解码为 str
html = content.decode() # 默认utf-8解码，但不一定网页都是utf-8编码的
print(html)

# 根据 chardet 判断网页编码格式
det = chardet.detect(content)
if det['confidence'] > 0.8: # 如果置信度大于0.8，则以它认为的方式解码
    html = content.decode(det['encoding'])
    print(det['encoding'])
else:
    html = content.decode('gbk')
    print(det['encoding'])

# 2.从源码提取信息：借助爬虫工具，BeautifulSoup
# BeautifulSoup：专门用于从HTML，XML文件中提取数据的Python库
from bs4 import BeautifulSoup as bs

# BeautifulSoup自动将输入的文档转换为Unicode编码，输出文档时转换为utf-8
soup = bs(html) # 没有指定解析器，默认使用Python自带的"lxml"解析器来解析HTML，可忽略警告
print('====================================')
print(soup.prettify())  # 以人类可读的格式展示源代码
print('====================================')

for a in soup.findAll(name='a'):    # 找出所有的 a 标签
    print('attrs:',a.attrs)
    print('string:',a.string)
    print('---------------------')
    
for tag in soup.findAll(attrs={'target':'target='}):
    # 找出 属性target='target='的所有标签
    print('tag:',tag.name)    
    print('attrs:',tag.attrs)    
    print('string:',tag.string)
    print('+++++++++++++++++++++++++')
    
for tag in soup.findAll(name='a',text='校友会'):
    # a标签中内容含有'校友会'
    print('tag:',tag.name)    
    print('attrs:',tag.attrs)    
    print('string:',tag.string)
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^')
    
import re
for tag in soup.findAll(attrs = {'stat':re.compile(r'sslink\-\d')}):
    # 用正则表达式找出 所有 stat为 sslink-数字 的标签
    print(tag)

for a in soup.findAll('a',text=re.compile(r'.*?会$')):
    # 内容以 '会' 结尾的a标签
    print(a)
    
# 自定义解析函数：定义自己的筛选规则
def my_parser(tag):
    # 相当于对 所有标签进行筛选
    if tag.name == 'a' and tag.attrs:
        return True
    
for tag in soup.findAll(my_parser):
    print(tag)
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

# 3.数据存储
# 3.1 保存为csv文件
data_csv = '''id,name,score
1,xiaoming,23
2,zhangsan,28
3,lisi,29
'''

with open('export_csv_01.csv','w') as f:
    f.write(data_csv)

# 3.2保存到数据库
# 使用Python原生支持的sqlite3数据库
import sqlite3 as base
# 数据库文件存在时直接开打，不存在则创建数据库文件，再打开数据库连接
db = base.connect('test_sqlite3.db')
# 获取游标
cursor = db.cursor()
# 建表,执行SQL语句
try:
    cursor.execute('''create table info2 (
            id text,
            name text,
            score int)'''
        )
except sqlite3.OperationalError as e:
    print(e)
    
db.commit()
# 添加数据
cursor.execute("insert into info2 values ('1','xiaohua',23)")
cursor.execute("insert into info2 values ('2','zhangsan',28)")
cursor.execute("insert into info2 values ('3','lisi',22)")
db.commit()

cursor.close()
db.close()
