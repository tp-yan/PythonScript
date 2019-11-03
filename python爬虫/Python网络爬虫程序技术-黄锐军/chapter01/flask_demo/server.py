import flask
import os

'''
服务端程序
'''

app = flask.Flask(__name__) # 以此文件名给flask对象 app命名

@app.route("/")
def index():
    # 显示静态网页
    try:
        f = open("index.html",'rb')
        data = f.read() # 二进制数据
        f.close()
        return data
    except Exception as err:
        return str(err)

@app.route("/hi")
def hi():
    return "Hello,你好！"

if __name__ == "__main__":
    print(__name__)
    print(__file__) # 当前文件的绝对路径，但是 unix路径风格 ‘/’
    parent_dir = os.path.dirname(__file__) # 当前文件的父目录，但是 unix路径风格 ‘/’
    print(os.path.abspath(parent_dir)) # 获取当前路径的绝对路径，是 win风格 '\'
    print(os.getcwd()) # 当前工作路径 win风格
    # 必须将工作路径切换到当前文件的父目录
    os.chdir(os.path.abspath(parent_dir))
    print(os.getcwd())

    with open("server.py",'rb') as f:
        print(f.read().decode())
    app.run()