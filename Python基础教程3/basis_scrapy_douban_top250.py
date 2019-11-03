# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 20:02:34 2019

网页爬虫之实战：爬取豆瓣Top250电影
@author: 10841
"""

# 1.手工实现网络爬虫
from urllib import request
from bs4 import BeautifulSoup
from chardet import detect
import re

# 1.1 获取网页源码
def getSoup(url):
    with request.urlopen(url) as fp:
        content = fp.read()
        det = detect(content)
        return BeautifulSoup(content.decode(det['encoding']),'lxml')
    
# 1.2解析数据
def getData(soup):
    '''获取一页的所列出的影片信息'''
    data = []
    # 找到影片列表的容器标签,返回一个满足要求属性的'ol'标签
    ol = soup.find('ol',attrs={'class':'grid_view'}) # 只返回匹配的第一个标签
    for li in ol.findAll('li'): # 返回所有 name='li'的Tag对象
        tep = [] # [名称...]+评分+评论
        titles = [] # 中英文电影名
        for span in li.findAll('span'):
            if span.has_attr('class'):
                if span.attrs['class'][0] == 'title': # class可能是多值
                    #print('/\xa0' in span.string,span.string)
                    titles.append(span.string.strip().replace('/\xa0','')) # 有些内容会有空格
                elif span.attrs['class'][0] == 'rating_num': # 评分
                    tep.append(span.string.strip())
                elif span.attrs['class'][0] == 'inq': # 评论
                    tep.append(span.string.strip())
        tep.insert(0,titles)
        data.append(tep)    # 一部电影的相关信息
    return data

# 1.3获取下一页链接
def nextUrl(soup):
    '''获取下一页链接'''
    a = soup.find('a',text=re.compile(r'^后页'))
    if a:
        return a.attrs['href']
    else:
        return None
                 
# 1.5 保存爬取的数据
def save_movies(movies):
    '''将一页的电影信息保存'''
    with open('douban_top250.txt','a+',encoding='utf-8') as f: 
        # a+:追加内容，文件不存在时创建。
        for movie in movies:
            f.write(str(movie))
            f.write('\n')
    
# 1.4 组织代码结构开始爬虫
if __name__ == '__main__':
    url = "https://movie.douban.com/top250"
    soup = getSoup(url)
    movie_data = getData(soup)
    save_movies(movie_data)
    print(movie_data) # 打印本页的电影
    next_page = nextUrl(soup) # 获取当前页的 '后页' 链接
    
    while next_page:
        soup = getSoup(url + next_page)
        movie_data = getData(soup)
        save_movies(movie_data)
        #print(movie_data)
        next_page = nextUrl(soup)

