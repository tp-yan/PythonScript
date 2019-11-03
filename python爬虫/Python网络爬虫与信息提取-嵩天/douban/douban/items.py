# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 定义需要抓取目标的内容,以项目名称开头
class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
     name = scrapy.Field()  # 电影名
     fen = scrapy.Field()   # 评分
     words = scrapy.Field() # 评语
