# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:30:03 2019

Request库实战之：向百度、360搜索引擎提交搜索字段并搜索
@author: 10841
"""

import requests

baidu_url = "http://www.baidu.com/s" # ?wd=keyword
_360_url = "https://www.so.com/s" # ?q=keyword

kw_baidu = {'wd':'xiaomi air'}
kw_360 = {'q':'matebook 14'}

r_baidu = requests.get(baidu_url,params=kw_baidu)
r_360 = requests.get(_360_url,params=kw_360)

if r_baidu.status_code == 200:
    r_baidu.encoding = r_baidu.apparent_encoding
    print(r_baidu.text[:10000])
else:
    print("百度搜索失败！")
print(r_baidu.request.url) # 真正请求的URL
print('网页大小：',len(r_baidu.text),'Kb')

print('=========================')
if r_360.status_code == 200:
    r_360.encoding = r_360.apparent_encoding
    print(r_360.text[:10000])
else:
    print("360搜索失败！")