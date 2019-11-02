def application(environ,start_response):    #WSGI接口，响应HTTP请求
    """
    :param environ:一个包含所有HTTP请求信息的dict对象；
    :param start_response:一个发送HTTP响应的函数。
    :return:返回header与body
    """
    start_response("200 ok",[("Content-Type","text/html")]) #返回header
    body = "<h1>Hello,%s!</h1>" % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode("utf-8")]   #返回body部分