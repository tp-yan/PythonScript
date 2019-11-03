# 爬虫调度器
from abt_crawler import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        # 初始化 URL管理器
        self.urls = url_manager.UrlManger()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1

        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("craw %d : %s" % (count, new_url))
                html_content = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_content)
                #print(count,":",new_data)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count >= 10:
                    break
                count += 1
            except:
                print("craw failed")
        self.outputer.output_html()


if __name__ == "__main__":
    # 爬虫入口URL
    root_url = "https://baike.baidu.com/item/Python/407313?fr=aladdin"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)  # 启动爬虫
