# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 09:10:54 2019

爬虫实例：中国最好大学排名2019
    定向爬虫：仅对输入URL进行爬取，不扩展爬取
    静态网页爬取：无法爬取，JS代码动态生成的网页内容
@author: 10841
"""
import bs4
import requests
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return None

def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,'html.parser')
    tbody = soup.find('tbody')
    for tr in tbody.children:
        if isinstance(tr,bs4.element.Tag): # 可能存在字符串标签，必须进行筛除！！！
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])
    

def printUnivList(ulist,num):
    # 打印前num个学校
    # 优化：解决中文对齐问题
    # 当中文字符宽度不够时，采用西文字符填充；中西文字符占用宽度不同
    # 采用中文字符的空格填充chr(12288)
    tem_format = "{0:^6}\t{1:{4}^10}\t{2:{4}^6}\t{3:^6}"
    print(tem_format.format("排名","学校名称","省市","总分",chr(12288)))
    for i in range(num):
        u = ulist[i]
        if u:
            print(tem_format.format(u[0],u[1],u[2],u[3],chr(12288)))
        
    
def main():
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html"
    html = getHTMLText(url)
    if html:
        ulist = []
        fillUnivList(ulist,html)
        if ulist:
            printUnivList(ulist,20)
            
main()

