from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from normalClient import normal_crawler

url = "http://127.0.0.1:5000/"

# 引入 chrome 程序的选择项目 Options
chrome_options = Options()
# 设置启动chrome 时不可见：既不会打开本机的Chrome浏览器
chrome_options.add_argument('--headless') 
chrome_options.add_argument('--disable-gpu')
# 创建Chrome浏览器，并像真是浏览器一样会自动执行JS脚本
chrome = webdriver.Chrome(options=chrome_options)
chrome.get(url)
html = chrome.page_source
print(html)

normal_crawler(html)