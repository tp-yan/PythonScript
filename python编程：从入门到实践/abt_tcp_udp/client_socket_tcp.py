import socket

# 创建一个socket:AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    #SOCK_STREAM指定使用面向流的TCP协议
# 建立连接: #客户端要主动发起TCP连接，必须知道服务器的IP地址和端口号,新浪网站的IP地址可以用域名www.sina.com.cn自动转换到IP地址
#新浪提供网页服务的服务器必须把端口号固定在80端口，因为80端口是Web服务的标准端口
#其他服务都有对应的标准端口号，例如SMTP服务是25端口，FTP服务是21端口，等等。端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用。
s.connect(("www.sina.com.cn",80))

# 发送数据: 向新浪服务器发送请求，要求返回首页的内容    #发送的文本格式必须符合HTTP标准
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#TCP连接创建的是双向通道，双方都可以同时给对方发数据。但是谁先发谁后发，怎么协调，要根据具体的协议来决定。例如，HTTP协议规定客户端必须先发请求给服务器，服务器收到后才发数据给客户端。

# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)    #接收数据时，调用recv(max)方法，一次最多接收指定的字节数
    if d:               #在一个while循环中反复接收，直到recv()返回空数据，表示接收完毕，退出循环。
        buffer.append(d)
    else:
        break

data = b''.join(buffer) #将字节串联成一整体
# 关闭连接:
s.close()

#接收到的数据包括HTTP头和网页本身，我们只需要把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件：
header,html = data.split(b'\r\n\r\n', 1)
print(header.decode("utf-8"))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)

