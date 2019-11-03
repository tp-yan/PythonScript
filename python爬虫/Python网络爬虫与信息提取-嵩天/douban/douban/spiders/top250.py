# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem
from bs4 import BeautifulSoup
import re

class Top250Spider(scrapy.Spider):
    # 以下三行都是自动生产的
    name = 'top250'
    allowed_domains = ['movie.douban.com'] 
    # 添加了 /top250 之后，第一页之后的 URL 都被认为不是 允许域下的URL，故爬虫就终止了
    # 或者在下面的Request方法添加 dont_filter参数
#    allowed_domains = ['movie.douban.com/top250']
    start_urls = ['https://movie.douban.com/top250/']
    
    def parse(self, response):
        soup = BeautifulSoup(response.body.decode('utf-8','ignore'),'lxml')
        ol = soup.find('ol',attrs={'class':'grid_view'})
        for li in ol.findAll('li'):
            tep = []
            titles = []
            for span in li.findAll("span"):
                if span.has_attr('class'):
                    if span.attrs['class'][0] == 'title':
                        titles.append(span.string.strip().replace(',','，'))
                    elif span.attrs['class'][0] == 'rating_num':
                        tep.append(span.string.strip().replace(',','，'))
                    elif span.attrs['class'][0] == 'inq':
                        tep.append(span.string.strip().replace(',','，'))
            tep.insert(0,titles[0])
            while len(tep) < 3:
                tep.append('-')
            tep = tep[:3]
            item = DoubanItem()
            item['name'] = tep[0]
            item['fen'] = tep[1]
            item['words'] = tep[2]
            # yield将函数变生成器，执行函数后返回一个可迭代对象
            # 迭代parse函数时，相当于不断循环执行函数体，遇到yield就停止返回一个值
            # 下次迭代则从yield下行代码继续执行
            yield item # 将一部电影的信息返回
        a = soup.find('a',text=re.compile(r'^后页'))
        if a:
            # Request类是一个http请求的类
            # 通常在Spider中创建这样的一个请求，在Downloader中执行这样的一个请求。
            # callback:回调函数，用于接收请求后的 返回信息（response），若没指定，则默认为parse()函数
            yield scrapy.Request('https://movie.douban.com/top250'+ a.attrs['href'],
                                 callback=self.parse)

            # 或者在Request中添加参数 dont_filter=True
            # 将下一页的URL通过Request对象yield到爬取队列，并制定处理该URL的函数为
            # self.parse，也可以是其他函数
