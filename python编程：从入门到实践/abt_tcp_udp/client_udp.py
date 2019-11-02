import socket

#客户端使用UDP时，首先仍然创建基于UDP的Socket
#不需要调用connect()，直接通过sendto()给服务器发数据
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    #发送数据
    client.sendto(data,("127.0.0.1",10000))
    #接受数据
    print(client.recv(1024).decode("utf-8"))    #从服务器接收数据仍然调用recv()方法。
client.close()
