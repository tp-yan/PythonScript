#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 21:56:58 2019

@author: tangpeng

urllib模块：提供系列用于操作URL的功能
"""

"""
1. GET
urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应

例如，对豆瓣的一个URLhttps://api.douban.com/v2/book/2129650进行抓取，并返回响应：
"""
from urllib import request

def func_get1():
    with request.urlopen(r'https://api.douban.com/v2/book/2129650') as f:
        data = f.read() # 返回的数据部分
        print("status:",f.status,f.reason) # 响应码
        for k,v in f.getheaders():
            print("%s --> %s" % (k,v))
        print("data:",data.decode("utf-8")) # 有可能返回的bytes是其他编码格式


# 要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器
# 例如，模拟iPhone 6去请求豆瓣首页：
def func_get2():
    req = request.Request('http://www.douban.com/')
    req.add_header('User-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36')
    with request.urlopen(req) as f:
        print("status:",f.status,f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', f.read().decode('utf-8'))

"""
2. POST
如果要以POST发送一个请求，只需要把参数data以bytes形式传入。
我们模拟一个微博登录，先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入：
"""
from urllib import parse

def func_post():
    print("Login to weibo.cn...")
    email = input("emial:")
    password = input("password:")
    login_data = parse.urlencode([
        ('username', email),
        ('password', password),
        ('entry', 'mweibo'),
        ('client_id', ''),
        ('savestate', '1'),
        ('ec', ''),
        ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
    ])
    
    req = request.Request('https://passport.weibo.cn/sso/login')
    req.add_header("Origin",'https://passport.weibo.cn')
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
    
    with request.urlopen(req,data=login_data.encode('utf-8')) as f:
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', f.read().decode('utf-8'))
    
"""
3.Handler
如果还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理，示例代码如下：
"""
import urllib
def func_proxy():
    proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
    proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
    proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
    opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
    with opener.open('http://www.example.com/login.html') as f:
        pass

"""
练习
利用urllib读取JSON，然后将JSON解析为Python对象：
"""
import json
def fetch_data(url):
    with request.urlopen(url) as f:
        data = f.read().encode('utf-8')
        print("status:",f.status,f.reason)
    return json.loads(data)

def test():
    # 测试
    URL = r'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
    data = fetch_data(URL)
    print(data)
    assert data['query']['results']['channel']['location']['city'] == 'Beijing'
    print('ok')
    
    
if __name__ == "__main__":
#    func_post()
    test()
    
