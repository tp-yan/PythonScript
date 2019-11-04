#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 16:25:53 2019

@author: tangpeng

HTMLParser：解析HTML字符串
"""

# Python提供了HTMLParser来非常方便地解析HTML，只需简单几行代码：
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHtmlParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print("<%s>" % tag)
        print("attrs:",attrs)
    
    def handle_endtag(self,tag):
        print("</%s>" % tag)
        
    def handle_startendtag(self,tag,attrs):
        print("<%s/>" % tag)
        print("attrs:",attrs)
        
    def handle_data(self,data):
        print(data,"-->",type(data))
        
    def handle_comment(self,data):
        print("<!--",data,"-->")
    
    # 处理特殊字符：英文表示的&nbsp;
    def handle_entityref(self,name):
        print("&%s" % name)
    # 处理特殊字符：数字表示的&#1234;
    def handle_charref(self,name):
        print("&#%s;" % name)
        
parser = MyHtmlParser()
# feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')


"""
练习
找一个网页，例如https://www.python.org/events/python-events/，用浏览器查看源码并复制，
然后尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点。
"""
from urllib import request
import re

def get_page_code(url):
    with request.urlopen(url) as f:
        print("status:",f.status,f.reason)
        return f.read().decode("utf-8")

class Event:
    def __init__(self,date=None,name=None,addr=None):
        self.date = date
        self.name = name
        self.addr = addr
        
    def __str__(self):
        return "Name:" + self.name +"\t" + "Date:"+self.date+"\t"+"Addr:"+self.addr
        
    
class PythonEventsParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.cur_tag = None
        self.title_1 = None
        self.title_2 = None
        self.upcoming_events = []
        self.just_missed = []
        self.during = False
        self.cur_event = None
        self.cur_tag = None
        self.upcoming = True
        self.counter = 0
        
    
    def handle_starttag(self,tag,attrs):
        self.cur_tag = tag
        attrs = dict(attrs)
        print(tag,"-->",attrs)
        
        if "widget-title" in attrs.values() and not self.title_1:
            print("title_1")
            self.during = True
        
        if "widget-title just-missed" in attrs.values() and not self.title_2:
            print("title_2")
            self.upcoming = False
            self.during = True
        
        if tag == "a" and "href" in attrs:
            regx = r"/events/python-events/\d{3}/"
            if re.match(regx,attrs['href']):
                self.cur_tag = "a"
                self.cur_event = Event()
                self.during = True
        if tag == "time":
            self.during = True
            
        if tag == "span" and "event-location" in attrs.values():
            self.during = True
    
    def handle_endtag(self,tag):
        pass
        
    def handle_data(self,data):
        if self.during:
            if self.cur_tag == "a":
                self.cur_event.name = data
                
            if self.cur_tag == "time":
                self.cur_event.date = data
            
            if self.cur_tag == "span":
                print(data)
                if not self.title_1 and self.upcoming:
                    self.title_1 = data
                    self.during = False
                    return
                
                self.cur_event.addr = data
                if self.upcoming:
                    self.upcoming_events.append(self.cur_event)
                    self.counter += 1
                    print("counter:",self.counter)
                else:
                    self.just_missed.append(self.cur_event)
                    self.counter += 1
                    print("counter:",self.counter)
                    
                self.cur_event = None
            
            if self.cur_tag == "h3" and not self.upcoming:
                self.title_2 = data
                
            self.during = False
        
    # 处理特殊字符：英文表示的&nbsp;
    def handle_entityref(self,name):
        print("&%s" % name)
    # 处理特殊字符：数字表示的&#1234;
    def handle_charref(self,name):
        print("&#%s;" % name)
    
def parse_html(html_str):
    parser = PythonEventsParser()
    parser.feed(html_str)
    
    print("============================")
    print(parser.title_1)
    for event in parser.upcoming_events:
        print(event)
    print("----------------------------")
    print(parser.title_2)
    for event in parser.just_missed:
        print(event)
    
html_str = get_page_code("https://www.python.org/events/python-events/")
print(html_str)
parse_html(html_str)

    
    
    
    