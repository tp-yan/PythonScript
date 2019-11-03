# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:19:42 2019

Request库实战之：爬取亚马逊页面，更改user-agent字段

@author: 10841
"""

import requests

amazon_url = "https://www.amazon.cn/dp/B07NR2B9HS?ref_=Oct_DLandingSV2_PC_df5d3706_0&smid=A2EDK7H33M5FFG"
# amazon对爬虫有来源审查，需要更改请求头
hd = {'user-agent':'Mozilla/5.0'} # 'Mozilla/5.0'：浏览器的身份标识，可能是任一浏览器
r = requests.get(amazon_url,headers=hd)
if r.status_code == 200:
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
else:
    print("爬取失败！")

print(type(r.request)) # Request对象，包含了发起HTTP请求时的信息
print(r.request.headers) # HTTP请求头
