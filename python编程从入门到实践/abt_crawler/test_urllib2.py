from urllib import request
import http.cookiejar

'''
测试 urllib 的3中下载网页的方法
'''
url = "http://www.baidu.com"

print("第一种方法：")
with request.urlopen(url) as f:
    print(f.status)
    print("data:",f.read())

print("\n第二种方法：")
req = request.Request(url)
req.add_header('User-Agent', 'Mozilla/6.0')
with request.urlopen(req) as f:
    print(f.status)
    print("data:", f.read())


print("\n第三种方法：")
cj = http.cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cj))
request.install_opener(opener)
with request.urlopen(url) as f:
    print(f.status)
    print(cj)
    print("data:", f.read())