from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sqlite3
import os
import threading
import urllib.request
import datetime
import scrapy # 使用 scrapy中的 selector


class MySpider:
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'}
    # 保存爬取的图片文件夹
    imagePath = "images"

    def initWork(self):
        '''初始化工作：
        1.创建Chrome浏览器
        2.初始化变量 threads，No
        3.创建数据库和表以及数据库连接和游标
        4.创建图片文件夹
        '''
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--diable-gpu")
        self.webBrowser = webdriver.Chrome(options=chrome_options)
        # 用于管理线程
        self.threads = []
        # 计数器
        self.No = 0 

        # 初始化数据库
        try:
            # 连接数据库
            self.conn = sqlite3.connect("mobiles.db")
            self.cursor = self.conn.cursor()
            try:
                # 如果存在 mobiles表则删除
                self.cursor.execute("drop table mobiles")
            except:
                pass
            try:
                # 创建新表mobiles
                sql = "create table mobiles ( mNo varchar(32) primary key,mMark varchar(256),mPrice float,mNote varchar(1024),mFile varchar(32) )"
                self.cursor.execute(sql)
            except Exception as err:
                print("建表失败：",err)
        except Exception as err:
            print(err)

        # 创建存放图片的文件夹
        try:
            if not os.path.exists(MySpider.imagePath):
                os.mkdir(MySpider.imagePath)
            images = os.listdir(MySpider.imagePath)
            # 删除原来的所有图片
            for img in images:
                s = os.path.join(MySpider.imagePath,img)
                os.remove(s)
        except Exception as err:
            print(err)

    def closeConn(self):
        try:
            self.conn.commit()
            self.conn.close()
        except Exception as err:
            print(err)

    def insertDB(self,mNo,mMark,mPrice,mNote,mFile):
        try:
            sql = "insert into mobiles (mNo,mMark,mPrice,mNote,mFile) values(?,?,?,?,?)"
            self.cursor.execute(sql,(mNo,mMark,mPrice,mNote,mFile))
        except Exception as err:
            print(err)

    def showDB(self):
        try:
            tmpt = "{:8} {:16} {:8} {:16} {}"
            print(tmpt.format("No","Mark","Price",'Image','Note'))
            self.cursor.execute("select mNo,mMark,mPrice,mFile,mNote from mobiles order by mNo")
            rows = self.cursor.fetchall()
            for row in rows:
                print(tmpt.format(*(row[:5])))
        except Exception as err:
            print(err)

    def parserItem(self,selector,url):
        '''
        使用selector解析当前url页面
        '''
        try:
            lis = selector.xpath("//div[@id='J_goodsList']//li[@class='gl-item']")
            for li in lis:
                # 解析图片
                #We find that the image is either in src or in data lazy img attribute
                # 提取a标签下的img标签的src属性值，即img的URL
                image = li.xpath(".//div[@class='p-img']//a//img/@src").extract_first()
                if not image: # 另一种可能的URL
                    image = li.xpath(".//div[@class='p-img']//a//@data-lazy-img").extract_first()
                if image: # 拼接img的URL，自带 ‘//’
                    image = "http:" + image
                # div下的i标签的 text属性，只提取第一个元素
                price = li.xpath(".//div[@class='p-price']//i//text()").extract_first()
                note = li.xpath(".//div[@class='p-name p-name-type-2']//em/text()").extract()
                mark = note[0].split(" ")[0]
                # 计算器+1
                self.No = self.No + 1
                # 图片名称编号
                no = str(self.No)
                while len(no) < 6:
                    no = "0" + no
                # 把所有的信息字段拼接
                note = ",".join(note)

                if image: # 根据URL查看是否有图片后缀名
                    if(image[len(image)-4] == '.'): # .jpg
                        ext = image[len(image)-4:]
                    else :
                        ext = ""
                    mFile = no + ext
                    # 创建一个线程下载一张图片，image:URL,mFile:保存到数据库中的图片名称
                    T = threading.Thread(target=self.downloadImage,args=(image,mFile))
                    T.setDaemon(False)
                    # 立即启动线程，爬取图片
                    T.start()
                    self.threads.append(T)
                else: # 没有图片就保存空
                    mFile = ""
                
                self.insertDB(no,mark,float(price),note,mFile)
        except Exception as err:
            print(err)

    def downloadImage(self,url,mFile):
        '''根据图片url下载图片，mFile:图片名称'''
        try:
            req = urllib.request.Request(url,headers=MySpider.headers)
            response = urllib.request.urlopen(req,timeout=20)
            data  = response.read()
            with open(os.path.join(MySpider.imagePath+"\\",mFile),"wb") as f:
                f.write(data)
        except Exception as err:
            print(mFile + " " + str(err) + " url="+url)

    def processSpider(self,url):
        '''
        获得网页源码并解析
        '''
        print(url)
        try:
            self.webBrowser.get(url)
            selector = scrapy.Selector(text=self.webBrowser.page_source)
            # 解析源码，提取信息，一次解析一页
            self.parserItem(selector,url)
            # 尝试获取最后一页的下一页按钮
            lastPage = selector.xpath("//span[@class='p-num']//a[@class='pn-next disabled']").extract()
            if not lastPage:
                nextPage = self.webBrowser.find_element_by_xpath("//span[@class='p-num']//a[@class='pn-next']")
                # 点击下一页
                nextPage.click()
                # 递归调用
                self.processSpider(self.webBrowser.current_url)
        except Exception as err:
            print(err)

    def executeSpider(self,url):
        starttime = datetime.datetime.now()
        print("-------- spider start --------")
        self.initWork()
        self.processSpider(url)
        self.showDB()
        self.closeConn()
        # 等待所有线程结束
        for t in self.threads:
            t.join()

        print("-------- spider completed --------")
        endtime = datetime.datetime.now()
        elapsed = (endtime-starttime).seconds
        print("Total ",elapsed, " seconds elapsed")

if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    os.chdir(dir)
    print('工作目录：\n',os.getcwd())
    url = 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf--8&wq=%E6%89%8B8&wq=%E6%89%8B%E6%9C%BA&pvid=0e1426ee068f4cfe94656dbb0949875f%22%E6%9C%BA&pvid=0e1426ee068f4cfe94656dbb0949875f'
    spider = MySpider()
    spider.executeSpider(url)