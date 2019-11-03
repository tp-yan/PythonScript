from html.parser import HTMLParser
from html.entities import name2codepoint
from collections import OrderedDict

class MyHTMLParser(HTMLParser):

    def __init__(self):
        super(MyHTMLParser,self).__init__()
        self.conference = OrderedDict()
        self.name_list = list()
        self.date_list = list()
        self.location_list = list()
        self.handing_name = False
        self.handing_date = False
        self.handing_location = False

    def handle_starttag(self, tag, attrs):
        #print('<%s>--handle_starttag' % tag)
        if tag == "a" and attrs:
            if str(attrs[0][1]).find("python-events") > 0:
                self.handing_name = True
        if tag == "time":
            self.handing_date = True
        if tag == "span" and attrs:
            if attrs[0][1] == "event-location":
                self.handing_location = True


       # print("attrs:",attrs)
       # if attrs:
       #     print(attrs[0][0])

    def handle_endtag(self, tag):
        #print('<%s>--handle_endtag' % tag)
        if tag == "html":
            print("============================================")
            for i in range(len(self.date_list)):
                print(self.date_list[i],"\t",self.name_list[i],"\t",self.location_list[i])
            print("============================================")


    def handle_startendtag(self, tag, attrs):
        print('<%s>--handle_startendtag' % tag)

    def handle_data(self, data):
        if self.handing_name:
            self.name_list.append(data)
            self.handing_name = False
        if self.handing_date:
            self.date_list.append(data)
            self.handing_date = False
        if self.handing_location:
            self.location_list.append(data)
            self.handing_location = False
        print(data,"--handle_data")

    def handle_comment(self, data):
        print('<!--', data, '-->','--handle_comment')

    def handle_entityref(self, name):
        print('&%s;' % name,'--handle_entityref')

    def handle_charref(self, name):
        print('&#%s;' % name,'--handle_charref')


