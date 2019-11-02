# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 11:35:50 2019

Request库实战之：获取IP地址归属地
由第三网站的IP库来查询，故需要调用第三方网站的API
@author: 10841
"""
import requests

IP_API = 'http://m.ip138.com/ip.asp?ip=' # ip=ipaddress
ipaddr = "10.0.15.226"
r = requests.get(IP_API + ipaddr)
r.raise_for_status()
print(r.text[-500:])
ipaddr = "10.0.15.226"
print("===================================================")
baidu_ip = "115.239.211.112"
r = requests.get(IP_API + baidu_ip)
r.raise_for_status()
print(r.text[-500:])
