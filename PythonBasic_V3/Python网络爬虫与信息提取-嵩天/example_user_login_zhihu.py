# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 17:10:24 2019

爬虫之利用cookies跳过网站登录
尝试爬取知乎首页
@author: 10841
"""

# 1.设置请求头
agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'
headers = {
        'HOST':"www.zhihu.com",
        'Referer':"http://www.zhihu.com",
        'User-Agent':agent,
        }

cookies = {
        '_gads':'ID=8b3459932b7c8256:T=1561108602:S=ALNI_MaMsj9kEcJkbVOelI8Ps-d-v5Tt7A',
        '_xsrf':'eNeshhGjYalc943eRhic9nkAFL7wQKYe',
        '_zap':'11c0b6df-b0d2-401e-baee-aabe1e52215b',
        'capsion_ticket':'2|1:0|10:1560927609|14:capsion_ticket|44:OGVmN2JlYTBmODU4NGQ3M2JhOThjZTVhMTJmY2I4Yjg=|133ca971c200416685bb9562a9b4c03dc6f186c62c592789574acb8b8d53c4ca',
        'd_c0':'ANAt9A8amQ-PTs-6iq1YERQq2Mk2fojJ6VQ=|1560752526',
        'q_c1':'4ecb9778e6c742e69ec548d60f5ae0f1|1560752527000|1560752527000',
        'tst':'r',
        'z_c0':"2|1:0|10:1560927620|4:z_c0|92:Mi4xbTFZMkFnQUFBQUFBMEMzMER4cVpEeVlBQUFCZ0FsVk5oQ3YzWFFBTW5YYlZNcFZ6SnN4czFXbjJubGZIMEJyT3h3|d55b6917809e87cf9cd1c722d8e5558ce212c3ceadbe7806b2c3402fc5589543",
        'tgw_l7_route':'116a747939468d99065d12a386ab1c5f',
        }

# 2.创建session对象
import requests

session = requests.session()
session.headers = headers
# session.cookies必须是<class ‘requests.cookies.RequestsCookieJar’>，
# 所以要利用requests.utils.add_dict_to_cookiejar进行赋值。 
requests.utils.add_dict_to_cookiejar(session.cookies,cookies)

# 3.爬取
url = "https://www.zhihu.com"
r = session.get(url)

with open("zhihu.html","wb") as f:
    f.write(r.text.encode('utf-8'))

