# 练习
# 请利用SAX编写程序解析Yahoo的XML格式的天气预报，获取天气预报：
from xml.parsers.expat import ParserCreate
from urllib import request
from datetime import datetime

class MySAXHandler(object):
    def __init__(self):
        self.my_dict = dict()
        self.forecast_list = list()
    def start_element(self,name,attrs):
        if name == "yweather:location":
            self.my_dict['city'] = attrs['city']
        if name == "yweather:forecast":
            self.forecast_list.append(forecast_dict(attrs['date'],attrs['high'],attrs['low']))

    def end_element(self, name):
        if name == "results":
            self.my_dict['forecast'] = self.forecast_list
            print(self.my_dict)

    def char_data(self,text):
        pass



def forecast_dict(date_str,high,low):
    dt = datetime.strptime(date_str, "%d %b %Y")
    dt_str = dt.strftime("%Y-%m-%d")
    return {
        'date':dt_str,
        'high':high,
        'low':low
    }

def parseXml(xml_str):
    #print(xml_str)
    handler = MySAXHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)
    return handler.my_dict

# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
print(result)
assert result['city'] == 'Beijing'
print("ok")