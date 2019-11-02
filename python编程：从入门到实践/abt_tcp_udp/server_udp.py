import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # SOCK_DGRAM指定了这个Socket的类型是UDP
# 绑定端口,绑定端口和TCP一样，但是不需要调用listen()方法，而是直接接收来自任何客户端的数据：
server.bind(("127.0.0.1", 10000))
print('Bind UDP on 10000...')
while True:
    # 接受数据
    data, addr = server.recvfrom(1024)  # recvfrom()方法返回数据和客户端的地址与端口
    print('Received from %s:%s.' % addr)  # addr包含ip+port
    server.sendto(b"Hello,%s!" % data, addr)    #服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端。
    
