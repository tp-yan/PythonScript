#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 23:03:47 2019

@author: 10841
处理URL资源的第三方库requests，比python自带的urllib更方便
"""
import requests

# 1.使用GET访问一个页面
def get():
    r = requests.get('https://www.douban.com/')
    print(r.status_code)
    print(r.text)
    
get()

# 2.对于带参数的URL，传入一个dict作为params参数：
def url_with_param():
    r = requests.get('https://www.douban.com/search', params={'q':'python','cat':'1001'})
    print(r.url) # 实际请求的URL
    print(r.encoding) # requests自动检测返回内容的编码
    # 无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象：
    print(r.content)
    print(r.content.decode(r.encoding))
    
url_with_param() # https://www.douban.com/search?q=python&cat=1001

# 3.requests对于特定类型的响应，例如JSON，可以直接获取：
def return_json():
    r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
    print(r.json())
    print(type(r.json()))

#return_json()

# 4.需要传入HTTP Header时，我们传入一个dict作为headers参数：
def input_headers():
    headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
    r = requests.get('https://www.douban.com/', headers=headers)
    print(r.text)
    
input_headers()

# 5.要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据：
# requests默认使用application/x-www-form-urlencoded对POST数据编码
def post():
    data={'form_email': 'abc@example.com', 'form_password': '123456'}
    r = requests.post('https://accounts.douban.com/login',data=data)
    
post()

# 6.如果要传递JSON数据，可以直接传入json参数：
def input_json(url):
    params = {'key':'value'}
    r = requests.post(url,json=params) # 内部自动序列化为JSON
    
# 上传文件需要更复杂的编码格式，但是requests把它简化成files参数：
def upload_file(url):
    #在读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度。
    upload_files = {"file":open("report.xls",'rb')}
    r = requests.post(url,files=upload_files)
    
# 7.把post()方法替换为put()，delete()等，就可以以PUT或DELETE方式请求资源。

# 8.requests对获取HTTP响应的其他信息也非常简单。例如，获取响应头：
def return_headers():
    r = requests.get('https://www.douban.com/')
    print(r.headers)
    print(r.headers['Content-Type'])
    
return_headers()

# 9.requests对Cookie做了特殊处理，使得我们不必解析Cookie就可以轻松获取指定的Cookie：
def get_put_cookie():
    # 要在请求中传入Cookie，只需准备一个dict传入cookies参数：
    cs = {'token': '12345', 'status': 'working'}
    r = requests.get('https://www.douban.com/',cookies=cs)
    print(r.cookies)
    print(r.cookies['bid'])
    print(type(r.cookies))
    
get_put_cookie()

# 要指定超时，传入以秒为单位的timeout参数：
def timeout(url):
    r = requests.get(url,timeout=2.5)# 2.5秒后超时
    
    