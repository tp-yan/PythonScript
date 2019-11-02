# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 17:24:34 2019

JD搜索指定商品并爬取商品名称和价格
@author: 10841
"""

import requests
from bs4 import BeautifulSoup
import bs4

def makeSession(headers,cookies):
    session = requests.session()
    session.headers = headers
    requests.utils.add_dict_to_cookiejar(session.cookies,cookies)
    return session        


def getHTMLText(url):
    agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'
    headers = {
        'User-Agent':agent
        }
    cookies = {
            '__jdc':'122270672',
            "shshshsID":"67f65ff54849d729f46918efcc5ceed3_3_1561110816629",
            "__jdb":"122270672.5.15609101556861376832155|4.1561110127",
            "areaId":"1",
            "_tp":"8V9McOt4L44yCAaxxIpLaLnSrmXr2tRQKV1fpVakm%2Bs%3D",
            "pin":"jd_60da2de5e9a44",
            "thor":"48173928D0BE78BC3BBEE1D2AE80FE522788B8489EBB3F2CE261FC4D1F35DF1E2C9E557C0E3FAC919165580B3FCA3971C2316F91B25FE8E93B09B29D9E175E74425B122688B871F5579909CE9AEBD67296D34A09DBC4477297129B1BABA25761C23D340A83957E3624ED218C472F41248F9FC1AE47BD4898E46136004960951A0A3F45B8DB45DB0F71F192AFD31F91FCD3731493255C74A4D0AEB1FB9BF7FFF8",
            "_pst":"jd_60da2de5e9a44",
            "pinId":"nbBzXwC4DLGW_uFiVhCdbbV9-x-f3wj7",
            "unick":"%E5%BF%83%E6%98%AF%E8%8F%A9%E6%8F%90%E6%A0%91%E8%BA%AB%E4%B8%BA%E6%98%8E%E9%95%9C%E5%8F%B0",
            "shshshfpb":"hMzLEyjSCqhljKHcM4fjoyQ%3D%3D",
            "TrackID":"1nHMZFtCAU74Br9J-wiIE9ZypwxZmYaBZsGNWjvwLXyO0nFmSR5-CxCuZ7BpO3PimKZQS19d3rj9V049_0sfaPB8PCwvPZeaxO6YWKlMs-2I",
            "unpl":"V2_ZzNtbUYEE0FxWxEGeRpYVmJUQggRBRAXdQsUU3kfXQJnAEEKclRCFX0UR1NnGl0UZwcZXEtcQRFFCEdkeB5fA2AFEFlBZxVLK14bADlNDEY1WnwHBAJfFXYPR1Z6EVgBVzMRXXJXQiV1DEFVcxldBWMHFVRFV0ETcgFEV3sdWDVXBCJtclVDFnAORGR6KV01JVdOWURVQhRxRUZQfBhUBWYDFllFXkQVdw5BXXkaXAFjMxNtQQ%3d%3d",
            "PCSYCityID":"1",
            "shshshfp":"05bed9e906ba5ebf93f97aac770561d2",
            "__jda":"122270672.15609101556861376832155.1560910156.1561022118.1561110127.4",
            "__jdu":"15609101556861376832155",
            "ipLoc-djd":"1-2812-51125-0",
            "cn":"0",
            "user-key":"fff2e67c-0ee1-4367-b239-fdf67f09057f",
            "__jdv":"122270672|google-search|t_262767352_googlesearch|cpc|kwd-126030955_0_5bae5bfc325b4fadbcb312c6370612bf|1561014515731",
            "ceshi3.com":"201",
            "shshshfpa":"8d6c69e2-1ea6-286c-fb3b-4d34c0fa05e3-1560910156",
            "aud_ver":"2",
            "aud":"aba1a6d9ee266d6335862c96b20c688a",
            "avt":"4",
            "asn":"5",
            "_t":"ne2TRpEvCQ3r9AGoQshP95+C9p89XtjV17gaMVppFHk=",
            "DeviceSeq":"0c04576e622d478881099b3c981c385f",
            "alc":"+EMt75ejcc/on1kEj+VpVg==",
            "o2Control":"webp|lastvisit=20",
    }
    try:
        session = makeSession(headers,cookies)
        r = session.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
#        print(len(r.text))
        return r.text
    except:
        print("获取页面源代码失败！")
        None
        
def parserHTML(rls,html):
    soup = BeautifulSoup(html,'html.parser')
    div = soup.find('div',id="J_goodsList")
#    print(div)
    for li in div.find('ul').children:
        try:
            # li 对应一个商品单元
            div_price = li.find('div',attrs={"class":"p-price"})
            price = div_price.find('i').string
            div_title = li.find('div',attrs={"class":"p-name p-name-type-2"})
            em = div_title.find('a').find('em')
            title = ""
            for tag in em.children:
                if isinstance(tag,bs4.element.Tag):
                    title += tag.string
                elif isinstance(tag,str):
                    title += tag.strip()
            rls.append([title,price])
        except:
            continue
    
def printGoods(pList):
    count = 0
    tepft = "{:^4}\t{:{ch}^20}\t{:{ch}^8}"
    print(tepft.format("序号","名称","价格",ch=chr(12288)))
    for title,price in pList:
        try:
            count += 1
            price = price or '---'
            print(tepft.format(count,title,price,ch=chr(12288)))
        except:
            print('error:',count,title,price)

def main():
    goods = "matebook14"
    start_url = "https://search.jd.com/Search?keyword="
    depth = 2
    p_info_lt = []
    
    for i in range(depth):
        html = getHTMLText(start_url+ goods + "&s=" + str(59*i))
        parserHTML(p_info_lt,html)
        
    printGoods(p_info_lt)

main()