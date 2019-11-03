# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:09:38 2019

通用爬虫框架：返回给定URL的页面资源
@author: 10841
"""
import requests

def getHTML(url):
    '''返回url指定的网页源码'''
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('爬取网页出错')
        return None