'''
urllib(程序包，这是Python自带的程序包) 程序包访问 web 网站
'''

import urllib.request

url = "http://127.0.0.1:5000"
html = urllib.request.urlopen(url)
html = html.read().decode()

print(html)