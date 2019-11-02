# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class DoubanPipeline(object):
    def __init__(self):
        self.fp = open('TOP250.csv','w',encoding='utf-8')
        print('=============pipeline opening===============')
        self.wrt = csv.DictWriter(self.fp,['name','fen','words'])
        self.wrt.writeheader()
        
    def process_item(self, item, spider):
        self.wrt.writerow(item)
        return item
    
    def close_spider(self, spider):
        # 可选实现，当spider被关闭时，这个方法被调用
        # 就应该在这个方法里，关闭文件读写流 fp
        print('+++++++++++ pipeline closing +++++++++')
        self.fp.close()