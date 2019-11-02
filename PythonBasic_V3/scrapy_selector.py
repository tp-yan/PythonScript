'''
class scrapy.selector.Selector(response=None, text=None, type=None)
    response 是 HtmlResponse 或 XmlResponse 的一个对象，将被用来选择和提取数据。
    text 是在 response 不可用时的一个unicode字符串或utf-8编码的文字。
    type 定义了选择器类型，可以是 "html", "xml" or None (默认).
xpath(query): 返回Selector对象的列表，即SelectorList
寻找可以匹配xpath query 的节点，并返回 SelectorList 的一个实例结果，单一化其所有元素。列表元素也实现了 Selector 的接口。
为了方便起见，response对象以 .selector 属性提供了一个selector,故该方法也可以通过 response.xpath() 调用
css(query)
应用给定的CSS选择器，返回 SelectorList 的一个实例。query 是一个包含CSS选择器的字符串。
在后台，通过 cssselect 库和运行 .xpath() 方法，CSS查询会被转换为XPath查询。
为了方便起见，response对象以 .selector 属性提供了一个selector,故该方法也可以通过 response.css() 调用
extract()：返回字符串列表
串行化并将匹配到的节点返回一个unicode字符串列表。 结尾是编码内容的百分比。

SelectorList对象
class scrapy.selector.SelectorList:是内建 list 类的子类，提供了一些额外的方法。
    xpath(query):对列表中的每个元素调用 .xpath() 方法
    css(query):对列表中的各个元素调用 .css() 方法
    extract():...
'''

from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import requests


# 从字符串构造Selector
body = '''<html>
<body>
    <span>good</span>
    <span>goodness<a>abc</a> word</span>
    <h1>h101</h1>
    <h1>h102</h1>
    <p class=c1 c2>p01</p><p class=c2 c3>p02</p><p class=c3>p03</p>
</body>
</html>'''

s_text = Selector(text=body)
print(s_text.xpath("//span/text()").extract()) # 将所有的 span里面的字符串(不包括子标签里面的)，全部放入一个list
# 1.从HTML响应主体中提取所有的 <h1> 元素
selector_list = s_text.xpath("//h1") # 所有 h1 标签对应的 Selector
print("selector_list:\n",selector_list)
# 2.从HTML响应主体上提取所有 <h1> 元素的文字，返回一个unicode字符串的列表:
all_txt_with_tag = s_text.xpath("//h1").extract() # 包含 h1 标签的字符串列表
all_txt_without_tag = s_text.xpath("//h1/text()").extract()
print("all_txt_with_tag:\n",all_txt_with_tag)
print("all_txt_without_tag:\n",all_txt_without_tag)
# 3.在所有 <p> 标签上迭代，打印它们的类属性:
for pNode in s_text.xpath("//p"): # 返回的每个元素也是 Selector
    print('class:',pNode.xpath("@class").extract())

print("==================================")
response = requests.get("http://doc.scrapy.org/en/latest/_static/selectors-sample1.html")
s_response = Selector(response=response)
print(s_response.xpath("//title/text()"))
print(s_response.xpath("//title/text()").extract())
print(s_response.css("title::text").extract_first())
print(s_response.xpath("//div[@id='images']/a/text()").extract())
print(s_response.xpath("//div[@id='images']/a/text()").extract_first())
print(s_response.xpath("//div[@id='images']/span/text()").extract_first(default='not-found'))
print(s_response.xpath('//base/@href').extract())
print(s_response.css("base::attr(href)").extract())
print(s_response.xpath("//a[contains(@href,'image')]/@href").extract())
print(s_response.css("a[href*=image]::attr(href)").extract())

