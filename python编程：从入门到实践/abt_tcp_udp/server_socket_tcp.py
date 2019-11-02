import socket
import time
import threading


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b"Welcome")  # 服务器首先发一条欢迎消息，然后等待客户端数据
    while True:
        data = sock.recv(1024)  # 获取client端发过来的数据
        time.sleep(1)
        if not data or data.decode("utf-8") == "exit":
            break
        sock.send(("hello,%s!" % data.decode("utf-8")).encode("utf-8"))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

#创建一个基于IPv4和TCP协议的Socket：

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#然后，我们要绑定监听的地址和端口
#127.0.0.1是一个特殊的IP地址，表示本机地址，如果绑定到这个地址，客户端必须同时在本机运行才能连接，也就是说，外部的计算机无法连接进来。
#端口号需要预先指定。因为我们写的这个服务不是标准服务，所以用9999这个端口号。请注意，小于1024的端口号必须要有管理员权限才能绑定：

# 监听端口:
server.bind(("127.0.0.1",9999))
#紧接着，调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量：
server.listen(5)
print('Waiting for connection...')
#接下来，服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接:
while True:
    #接受一个新连接
    sock,addr = server.accept()
    #创建新线程来处理TCP请求,每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接：
    t = threading.Thread(target=tcplink,args=(sock,addr))
    t.start()


