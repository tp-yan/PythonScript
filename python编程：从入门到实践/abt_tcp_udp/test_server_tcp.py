#此client端是为了测试 server_socket中创建的服务器端
import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",9999))
#接收欢迎信息
print(client.recv(1024).decode("utf-8"))

for data in [b'Michael', b'Tracy', b'Sarah']:
    #发送数据
    client.send(data)
    print(client.recv(1024).decode("utf-8"))
client.send(b"exit")
client.close()