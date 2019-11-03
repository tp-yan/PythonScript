# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:02:36 2019

basis_scarpy_build.py:完成网页爬虫前的初始化工作,创建爬虫项目
@author: 10841
"""

import os

pname = input('项目名称：')
# os.system:调用shell，生成subshell执行脚本
os.system("Scrapy startproject " + pname) # 在当前目录下调用Scrapy生成一个项目
os.chdir(pname) # 用于改变当前工作目录到指定的路径，即爬虫项目目录下
wname = input('爬虫名:')   # 完成爬虫的py程序名称
site = input('网址：')     # 域名

# 在此之前 spiders目录下只有 __init__.py
# 通过预定义模板，生成新的spider：即Top250Spider(scrapy.Spider)类 继承自scrapy.Spider类
# 生成 top250.py
os.system("Scrapy genspider " + wname + " " + site)

runc = """
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from {0}.spiders.{1} import {2}

# 获取setting模块的设置
settings = get_project_settings()
process = CrawlerProcess(settings=settings)

# 可以添加多个spider
#process.crawl(Spider1)
#process.crawl(Spider2)
process.crawl({2}) # 传入的是类Top250Spider：包含了parse方法

# 启动爬虫，会阻塞程序，直至爬虫结束
process.start()
""".format(pname,wname, wname.title()+'Spider')

# 在项目根目录下生成 main.py 程序运行主入口
with open('main.py','w',encoding='utf-8') as f:
    f.write(runc)
input('end')

'''
scrapy.cfg:项目的配置文件
items:抓取内容描述
pipelines.py：管道，用于数据的清洗与存储
top250.py:爬虫文件
settings.py:配置文件
middlewares.py:中间件
'''

