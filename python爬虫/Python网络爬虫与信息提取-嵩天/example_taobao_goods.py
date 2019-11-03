# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 16:20:32 2019

淘宝页面商品爬虫：
    获取多个页面列出的商品名称和价格。
    需要登录认证无法获取商品页面信息
@author: 10841
"""

import re
import requests
# 这里没有导入 BeautifulSoup，而是直接使用 正则表达式去匹配、提取想要得到的信息

def getHTMLText(url):
    try:
        hd = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'}
        r = requests.get(url,headers=hd)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.url)
        return r.text
    except:
        print("获取页面源代码失败！")
        None

def parserHTML(rls,html):
    price_regex = r'"view_price":"([\d\.]*)"' 
    title_regex = r'"raw_title":"(.*?)"'
    p_list = re.findall(price_regex,html) # 返回所有匹配字符串的list
    t_list = re.findall(title_regex,html) # 使用了分组匹配后只返回要提取的那部分
    for i in range(len(p_list)):
        price = eval(p_list[i]) # eval：去除字符串的引号
        title = eval(t_list[i])
        rls.append([title,price])
    
    
def printGoods(goodLS):
    count = 0
    tepft = "{:^4}\t{:{ch}^16}\t{:{ch}^8}"
    print(tepft.format("序号","名称","价格",ch=chr(12288)))
    for title,price in goodLS:
        count += 1
        print(tepft.format(count,title,price))

def main():
    goods = "matebook"
    start_url = "https://s.taobao.com/search?q="
    depth = 2   # 爬虫的页面数
    results = []
    for i in range(depth):
        url = start_url + goods + "&s=" + str(44*i)
        html = getHTMLText(url)
        return 
        parserHTML(results,html)
        printGoods(results)
        
main()