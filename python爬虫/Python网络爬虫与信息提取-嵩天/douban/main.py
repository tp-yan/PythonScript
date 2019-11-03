
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from douban.spiders.top250 import Top250Spider

# 获取setting模块的设置
settings = get_project_settings()
process = CrawlerProcess(settings=settings)

# 可以添加多个spider
#process.crawl(Spider1)
#process.crawl(Spider2)
process.crawl(Top250Spider)

# 启动爬虫，会阻塞程序，直至爬虫结束
process.start()