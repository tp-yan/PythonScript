import urllib.request
from bs4 import BeautifulSoup


url = "http://127.0.0.1:5000/"

html = urllib.request.urlopen(url)
data = html.read()
html = data.decode()
print(data.decode()) # 只能获取HTML静态内容，无法得到JS和服务器返回的内容

def normal_crawler(html):
    soup = BeautifulSoup(html,'lxml')
    hMsg = soup.find("span",attrs={"id":"hMsg"}).text
    jMsg = soup.find("span",attrs={"id":"jMsg"}).text
    sMsg = soup.find("span",attrs={"id":"sMsg"}).text

    print("hMsg:",hMsg)
    print("jMsg:",jMsg)
    print("sMsg:",sMsg)

normal_crawler(html)
