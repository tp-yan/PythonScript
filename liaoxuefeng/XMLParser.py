#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 09:16:33 2019

@author: tangpeng

XML
操作XML有两种方法：DOM和SAX。
DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。
正常情况下，优先考虑SAX，因为DOM实在太占内存。

在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，
准备好这3个函数，然后就可以解析xml了。

举个例子，当SAX解析器读到一个节点时：

<a href="/">python</a>
会产生3个事件：
start_element事件，在读取<a href="/">时；
char_data事件，在读取python时；
end_element事件，在读取</a>时。
"""

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler:
    def start_element(self,name,attrs):
        print('sax:start_element: %s, attrs: %s' % (name,str(attrs)))
        print(type(attrs))
        
    def end_element(self,name):
        print('sax:end_element: %s' % name)
        
    def char_data(self,text):
        print('sax:char_data: %s' % text)
        
def func_xml():
    xml = r'''<?xml version="1.0"?>
                <ol>
                    <li><a href="/python">Python</a></li>
                    <li><a href="/ruby">Ruby</a></li>
                </ol>
            '''
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)

# 生成XML: 最简单也是最有效的生成XML的方法是拼接字符串
def func_generate_xml():
    L = []
    L.append(r'<?xml version="1.0"?>')
    L.append(r'<root>')
    L.append("text-content")
    L.append(r'</root>')
    return "".join(L)
    

"""
练习
请利用SAX编写程序解析Yahoo的XML格式的天气预报，获取天气预报：
https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml
参数woeid是城市代码，要查询某个城市代码，可以在weather.yahoo.com搜索城市，浏览器地址栏的URL就包含城市代码。
"""
from urllib import request

class WeatherSaxHandler:
    def __init__(self):
        self.city = None
    
    def start_element(self,name,attrs):
        print('sax:start_element: %s, attrs: %s' % (name,str(attrs)))
        if not attrs['city']:
            self.city = attrs['city']
            
    def end_element(self,name):
        pass
    
    def char_data(self,text):
        pass
            
def parseXml(xml_str):
    print(xml_str)
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)
    
    return {
        'city': handler.city,
        'forecast': [
            {
                'date': '2017-11-17',
                'high': 43,
                'low' : 26
            },
            {
                'date': '2017-11-18',
                'high': 41,
                'low' : 20
            },
            {
                'date': '2017-11-19',
                'high': 43,
                'low' : 19
            }
        ]
    }
        
        
def test():
    # 测试:
    URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'
    
    with request.urlopen(URL, timeout=4) as f:
        data = f.read()
    
    result = parseXml(data.decode('utf-8'))
    assert result['city'] == 'Beijing'
    
    
    

if __name__ == "__main__":
    func_xml()
    print(func_generate_xml())
    test()