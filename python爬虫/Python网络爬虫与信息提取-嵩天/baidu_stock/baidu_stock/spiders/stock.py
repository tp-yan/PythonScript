# -*- coding: utf-8 -*-
import scrapy
import re


class StockSpider(scrapy.Spider):
    name = 'stock'
    # allowed_domains = ['baidu.com']
    start_urls = ['http://quote.eastmoney.com/stock_list.html']
    baidu_url = "https://gupiao.baidu.com/stock/"

    """
    Scrapy爬虫支持多种HTML信息提取方法：
    • Beautiful Soup
    • lxml
    • re
    • XPath Selector
    • CSS Selector
    """
    def parse(self, response):
        ''' 
        <HTML>.css('a::attr(href)').extract():获取所有a标签href属性的值
        CSS查询会被转换为XPath查询。
        response实现了 Selector类的 xpath和css方法
        xpath(),css()：都返回 SelectorList 的一个实例结果，单一化其所有元素。列表元素也实现了 Selector 的接口。
        extract()：串行化并将匹配到的节点返回一个字符串列表
        SelectorList 类是内建 list 类的子类
            xpath(query):对列表中的每个元素调用 .xpath() 方法
            css(query):对列表中的各个元素调用 .css() 方法
            extract():对列表中的各个元素调用 .extract() 方法
        '''
        for href in response.css('a::attr(href)').extract():
            try:
                stock = re.findall(r"[s][hz]\d{6}",href)[0]
                # 构造百度股票的URL
                url = self.baidu_url + stock + ".html"
                # Request对象表示一个HTTP请求,由Spider生成，由Downloader执行
                # yield将Request请求放入请求列队中，由scheduler负责调度
                # callback=paser_stock：指定从Downloader返回响应时，调用哪个方法处理返回对象Response
                yield scrapy.Request(url,callback=self.paser_stock)
            except:
                continue

    def paser_stock(self,response):
        # 将每一支股票信息，存于字典后传给 ItemPipeline
        infoDict = {}
        stockInfo = response.css('.stock-bets') # 获取含指定属性值的标签
        # print('stockInfo:',stockInfo)
        '''
        [<Selector xpath="descendant-or-self::*[@class and contains(concat(' ', normalize-space(@class), ' '), ' stock-bets ')]" 
        data='<div class="stock-bets">\n        <h1>\n  '>]
        '''
        name = stockInfo.css('.bets-name').extract()[0]
        # print('name:',name)
        '''
        name: <a class="bets-name" href="/stock/sz002456.html">
            欧菲光 (<span>002456</span>)
            </a>
        '''
        keyList = stockInfo.css('dt').extract()
        valueList = stockInfo.css('dd').extract()
        '''
        ['<dt>今开</dt>', '<dt>成交量</dt>',...]
        ['<dd class="s-down">8.08</dd>', '<dd>78.15万手</dd>',...]
        '''

        for k,v in zip(keyList,valueList):
            try:
                k = re.findall(r'>.*</dt>',k)[0][1:-5]
                v = re.findall(r'\d+\.?.*</dd>',v)[0][0:-5]
                infoDict[k.strip()] = v.strip()
            except:
                infoDict[k.strip()] = '--'
        infoDict.update({'股票名称：': re.findall(r'\s.*\(',name)[0].split()[0] + 
            re.findall(r'\>.*\<',name)[0][1:-1]})
        # 此迭代器由 Item Pipeline 调用，将infoDict传入
        yield infoDict
