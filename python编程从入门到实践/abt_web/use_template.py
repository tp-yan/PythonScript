from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    return render_template("home.html") #Flask通过render_template()函数来实现模板的渲染

@app.route("/signin",methods=['GET'])
def sigin_form():
    return render_template("form.html")

@app.route("/signin",methods=['post'])
def signin():
    username = request.form['username']
    password = request.form['password']
    print(username,password)
    if username == 'admin' and password == 'password':
        return render_template("signin-ok.html",username=username)
    return render_template("form.html",message='Bad username or password',username=username)

if __name__ == "__main__":
    app.run()

#Flask默认支持的模板是jinja2
#<!--在Jinja2模板中，用{{ name }}表示一个需要替换的变量。很多时候，还需要循环、条件判断等指令语句，在Jinja2中，用{% ... %}表示指令。-->