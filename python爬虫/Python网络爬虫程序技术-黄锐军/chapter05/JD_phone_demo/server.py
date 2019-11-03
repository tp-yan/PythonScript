import sqlite3
import flask
import os

app = flask.Flask(__name__,static_folder='images')

@app.route("/")
def show():
    s = "<table border='1' width='800'><tr><th> 编号 </th><th> 品牌 </th><th> 价格</th><th> 说明 </th><th> 图像 </th></tr>"
    try:
        conn = sqlite3.connect("mobiles.db")
        cursor = conn.cursor()
        # 只取20条记录出来
        cursor.execute("select mNo,mMark,mPrice,mNote,mFile from mobiles order by mNo LIMIT 20")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
            s=s+"<tr><td>"+row[0]+"</td><td>"+row[1]+"</td><td>"+str(row[2])+"</td><td>"+row[3]+"</td>"
            s=s+"<td><img width='100' height='100' src='images/"+row[4]+"'></td></tr>"
        conn.close()

    except Exception as err:
        print("操作数据库失败：",err)
    s = s + "</table>"
    return s

if __name__ == "__main__":
    os.chdir(os.path.abspath(os.path.dirname(__file__)))
    app.run()