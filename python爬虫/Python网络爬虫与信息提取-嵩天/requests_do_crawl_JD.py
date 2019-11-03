# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:07:11 2019

Request库实战之：爬取京东商品页面
@author: 10841
"""

from universal_crawler_framework import getHTML

jd_url = "https://item.jd.com/100004364086.html"
text = getHTML(jd_url)
if text:
    print(text[:1000])