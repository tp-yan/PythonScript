# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BaiduStockPipeline(object):
    def process_item(self, item, spider):
        return item

'''
自定义ItemPiepeline
记得在 setting.py中注册自己的类 
ITEM_PIPELINES = {
   'baidu_stock.pipelines.BaiduStockInfoPipeline': 300,
}
'''
class BaiduStockInfoPipeline(object):
    """Pipeline类应该实现如下3个方法"""
    def open_spider(self,spider):
        '''启动spider时调用'''
        self.f = open("BaiduStockInfo.txt",'w')
        spider.log('--------------open_spider--------------')

    def close_spider(self,spider):
        """关闭spider时调用"""
        self.f.close()
        spider.log('--------------close_spider--------------')
    
    def process_item(self,item,spider):
        # 处理从 paser_stock 生成器 传过来的 字典
        try:
            line = str(dict(item)) + "\n"
            self.f.write(line)
        except:
            pass
        # 若如果其他函数需要，则返回
        return item 

