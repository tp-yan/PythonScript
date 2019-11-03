#HTML解析器
import re
import urllib.parse
from bs4 import BeautifulSoup

class HtmlParser(object):
    def parse(self, page_url, html_content):
        """解析出"""
        if page_url is None or html_content is None:
            return

        soup = BeautifulSoup(html_content,"html.parser",from_encoding="utf-8")
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)

        return new_urls,new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all("a",href=re.compile(r"/item"))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url,new_url)   #将后者按照前者格式配置为完整的URL
            new_urls.add(new_full_url)
        return  new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        res_data["url"] = page_url
        #<dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find("dd",class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data["title"] = title_node.get_text()
        #print("title:",res_data["title"])
        #print("title:",title_node.get_text())

        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find("div",class_="lemma-summary")
        res_data["summary"] = summary_node.get_text()
       # print("summary:", summary_node.get_text())
        #print("summary:", res_data["summary"])

        return res_data