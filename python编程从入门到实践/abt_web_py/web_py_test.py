import web
import pymysql

#使用模板须声明
render = web.template.render("templates")   #参数为模板的目录

urls = (
    "/index","index",   #精确，完全匹配
    "/article","article",
    "/blog/\d+","blog", #模糊匹配
    '/(.*)', 'hello'    #带组匹配，匹配到的URL请求，交给hello处理，可匹配任何URL，大范围的匹配放在后面
)
app = web.application(urls, globals())

class index:
    def GET(self):
        query = web.input() #获取请求参数
        #URL跳转
        return web.seeother("/article") #也可以是绝对URL：http://www.baidu.com
        # return query

class blog:
    def GET(self):
        return web.ctx.env
    def POST(self):
        data = web.input()
        return data

class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return render.hello2(name)  #使用模板目录中的html,调用html文件名，还可以向模板传参
        # return open("demo1/2.html","r").read()
        # return 'Hello, ' + name + '!'   #返回给浏览器的内容

class article:
    def GET(self):
        conn = pymysql.connect(host="localhost",user="root",password="2014112217",db="test_python",port=3306)
        cursor = conn.cursor()
        cursor.execute("select * from user")
        r = cursor.fetchall()
        cursor.close()
        conn.close()
        print(r)
        return render.article(r)

if __name__ == "__main__":
    app.run()