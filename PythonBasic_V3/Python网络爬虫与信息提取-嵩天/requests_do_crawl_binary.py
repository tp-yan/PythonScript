# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:43:40 2019

Request库实战之：爬取任何二进制资源
@author: 10841
"""
import os
import requests
import time

def getAnyContent(url,dir_path,name):
    """此方法以二进制格式读取爬虫的内容，故可以爬取并保存任何资源，如图片，动图，
    视频、音频，普通页面等"""
    try:
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
#        hd = {'user-agent':}
        r = requests.get(url)
        r.raise_for_status()
        with open(dir_path + name,'wb') as fp:
            fp.write(r.content)
    except Exception as e:
        print("爬取失败")
        print(e)
        


if __name__ == '__main__':
    # 图片来源：国家地理网
    img_url = "http://img0.dili360.com/ga/M00/48/F7/wKgBy1llvmCAAQOVADC36j6n9bw622.tub.jpg"
    # time.localtime():本地当前时间
    # time.time():返回 1970.1.1至今的时间戳，秒为单位的浮点数
    # time.strftime:格式化日期
    time_now = time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime())
    getAnyContent(img_url,r"./",'img_'+time_now+".jpg")
    
    gif_url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1560924179612&di=5833027f889bb0c3ab16930e68794090&imgtype=0&src=http%3A%2F%2Fphotocdn.sohu.com%2F20151113%2Fmp41523318_1447397103426_1.gif"
    suffix = gif_url.split('.')[-1]
    getAnyContent(gif_url,r"./",'img_'+time_now + "." + suffix)
    
    video_url = """https://vd4.bdstatic.com/mda-ijw6i1ex1wmmsw3t/hd/mda-ijw6i1ex1wmmsw3t.mp4?auth_key=1560916573-0-0-38581a766105f6ba500e7bf26572e65a&bcevod_channel=searchbox_feed&pd=bjh&abtest=all"""
    getAnyContent(video_url,r"./",'video_'+ time_now + ".mp4")
    
    web_url = "http://www.baidu.com"
    getAnyContent(web_url,r"./",'web_'+ time_now + ".html")
    
    print('爬虫结束！')