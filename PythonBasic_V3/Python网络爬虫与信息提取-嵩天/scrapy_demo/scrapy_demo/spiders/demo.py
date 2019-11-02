# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo' # 爬虫名，一个scrapy项目可以有多个爬虫
    # allowed_domains = ['python123.io'] # 可选
    start_urls = ['http://python123.io/ws/demo.html']

    def parse(self, response):
        '''parse()用于处理响应，解析内容形成字典，现新的URL爬取请求'''
        fname = response.url.split('/')[-1]
        with open(fname,'wb') as f:
            f.write(response.body)
            self.log('Saved file %s.' % fname)
    # 在控制台输入：scrapy crawl demo ， 启动此爬虫
