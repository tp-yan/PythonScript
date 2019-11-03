# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 09:52:13 2019

爬虫实例：QS 2020年世界大学排名
    爬取原生表格，并保存到本地
@author: 10841
"""
import requests
import bs4
import os
import numpy as np
from pandas import DataFrame,Series
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r = requests.get(url,timeout=15)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("爬取网页失败！")
        return None

def fillUnivDF(html):
    '''解析HTML内容，以DataFrame格式保存'''
    # 先构建一个二维list
    table = []
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td') # tr下的所有 td标签
            row = []
            for td in tds:
                row.append(td.string.strip().replace('\xa0','-'))
            if len(row) == 11:
                table.append(row)
    cols = table.pop(0) # 表头，列名
    df = DataFrame(np.array(table),columns=cols)
    return df   # 返回的是对象的拷贝，也是一个对象，局部变量df在函数结束后就被销毁

def printUnivDF(df,num):
    headers = df.columns.values
    headers = list(headers)
    headers.append(chr(12288))

    header_tpft = """{0:{11}^10}\t{1:{11}^10}\t{2:{11}^4}\t{3:{11}^4}\t{4:{11}^6}
    \t{5:{11}^8}\t{6:{11}^4}\t{7:{11}^6}\t{8:{11}^6}\t{9:{11}^6}\t{10:{11}^6}"""

    row_tpft = """{:^10}\t{:{ch}^10}\t{:^4}\t{:^4}\t{:^6}\t{:^8}\t{:^4}\t{:^6}\t
    {:^6}\t{:^6}\t{:^6}"""
    # 表头行
    print(header_tpft.format(*headers))
    for row in df[:num].values:
        row = list(row)
        print(row_tpft.format(*row,ch=chr(12288)))

def saveUnivDF2CSV(df,dir_path,filename):
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    df.to_csv(dir_path + "\\" + filename)

def main():
    url = "https://www.cingta.com/detail/11984"
    html = getHTMLText(url)
    if html:
        df = fillUnivDF(html)
        if df is not None:
            saveUnivDF2CSV(df,".//","QS_university_rank_2020.csv")
    else:
        print("未爬取到网页内容")
    printUnivDF(df,2)
            

main()