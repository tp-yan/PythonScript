# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 20:33:29 2019

爬虫实例之爬取股票信息
@author: 10841
"""
import requests
import re
from bs4 import BeautifulSoup
import traceback


def getHTMLText(url,encoding="utf-8"):
    # 尤其在定向爬虫时，可以手动查看网页编码
    try:
        agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'
        hd = {
        'User-Agent':agent
        }
        r = requests.get(url,headers=hd,timeout=15)
        r.raise_for_status()
        r.encoding = encoding # 这里没有使用 apparent_encoding:因为其需要解析网页内容来判断编码，耗时多
        return r.text
    except:
        print(url,":获取网页失败 ")
        return None
        
def getStockCodeList(slt,url):
    '''从东方财富网上获取股票的代码'''
    html = getHTMLText(url,encoding='gb2312')
    with open("./caifu.html","wb") as f:
        f.write(html.encode('utf-8'))
        
    if html:
        soup = BeautifulSoup(html,'html.parser')
        for a in soup.find_all('a'):
            try:
                href = a.attrs['href']
                pattern = r'[s][hz]\d{6}'
                result = re.findall(pattern,href)
                if result:
                    slt.append(result[0])
            except:
                continue

def getStockInfo(slt,url,fpath):
    """从百度股票获取每一股票的详细信息"""
    count = 0
    for stock in slt:
        try:
            html = getHTMLText(url+stock+".html")
            if html:
                soup = BeautifulSoup(html,'html.parser')
                div = soup.find('div',attrs={'class':"stock-bets"})
                if not div:
                    continue
                dt_list = div.find_all('dt')
                dd_list = div.find_all('dd')
                stock_info = {}
                name = div.find_all('a',attrs={'class':"bets-name"})[0]
                if count == 0:
                    print("===================")
                    print(name.text) # 将该标签下的所有文本内容提取出来，不含嵌套标签信息
                    print(name.string) # 
                    print("===================")
                stock_info.update({'股票名称':name.text.split()[0]})
                for dt,dd in zip(dt_list,dd_list):
                    stock_info[dt.text] = dd.text
                with open(fpath,'a',encoding='utf-8') as f:
                    f.write(str(stock_info)+"\n")
                    count += 1
                    print("\r当前进度：{:.2f}%".format(count*100/len(slt)),end="")
        except:
            traceback.print_exc()
            count += 1
            print("\r当前进度：{:.2f}%".format(count*100/len(slt)),end="")
            continue
            
    
def main():
    stock_list_url = "http://quote.eastmoney.com/stock_list.html"
    stock_info_url = "https://gupiao.baidu.com/stock/"
    filename = "./sotck_info.txt"
    stock_list = []
    getStockCodeList(stock_list,stock_list_url)
    getStockInfo(stock_list,stock_info_url,filename)
    
main()
    