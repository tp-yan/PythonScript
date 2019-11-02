from bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# 第一个参数是要解析的html字符串，第二个是指定使用哪个解析器，html.parser：python自带的解析器，第三参数是HTML的编码
soup = BeautifulSoup(html_doc,"html.parser",from_encoding="utf-8")

print("获取所有的链接")
links = soup.find_all("a")  #获取所有的<a>标签
for link in links:
    print(link.name,"\t",link['href'],"\t",link.get_text())

print("获取Lacie的URL")
line_node = soup.find("a",text="Lacie")
print(line_node.name,"\t",line_node['href'],"\t",line_node.get_text())

print("正则匹配")
link_node = soup.find("a",href=re.compile(r"ill"))
print(line_node.name,"\t",line_node['href'],"\t",line_node.get_text())

print("获取P段落")
p_node = soup.find("p",class_="title")
print(p_node.name,"\t",p_node.get_text())
