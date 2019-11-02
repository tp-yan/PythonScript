import os
import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    try:
        with open("index.html",'rb') as f:
            data = f.read()
            return data
    except Exception as err:
        return str(err)

@app.route("/show")
def show():
    return "Server Message"

if __name__ == "__main__":
    print("工作目录：\n",os.getcwd())
    app.run()