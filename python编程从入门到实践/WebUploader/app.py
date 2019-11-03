import os
import json
import web
from datetime import datetime

urls = (
    '/','UploadFile',
)

app = web.application(urls,globals())
web.config.debug = True

render = web.template.render("templates/",cache=False)

class UploadFile:
    """文件上传处理"""
    def GET(self):
        # return render.test()
        return render.file_upload()

    def POST(self):
        """
        x = web.input(myfile={})
        if 'myfile' in x:
            filepath = x.myfile.filename.replace('//', '/')  # 客户端为windows时注意
            filename = filepath.split('/')[-1]  # 获取文件名
            ext = filename.split('.', 1)[1]  # 获取后缀
            if ext == 'jpg':  # 判断文件后缀名
                homedir = os.getcwd()
                filedir = '%s/static/uploads' % homedir  # 要上传的路径
                now = datetime.now()
                t = "%d%d%d%d%d%d" % (now.year, now.month, now.day, now.hour, now.minute, now.second)  # 以时间作为文件名
                filename = t + '.' + ext
                fout = open(filedir + '/' + filename, 'wb')
                fout.write(x.myfile.file.read())
                fout.close()
                message = u'OK!'
                error = False
            else:
                message = u'请上传jpg格式的文件!'
                error = True
        return message
        """
        data = web.input()
        filename= data.get("Filename")
        filedata = data.get("Filedata")
        fullname = os.path.join("static/uploads",filename)
        try:
            fout = open(fullname,"wb")
            fout.write(filedata)
            fout.close()
        except Exception as e:
            print(e)
            return json.dumps({'success': 0, 'msg': u'文件上传失败！ %s...' % e[1]})
        else:
            return json.dumps({'success': 1, 'msg': u'文件上传成功！'})

    def handle(self):
        pass

if __name__ == "__main__":
    app.run()