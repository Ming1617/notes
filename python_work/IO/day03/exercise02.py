from socket import *

#创建tcp套接字
sockfd=socket()

# 连接服务器
server_addr=('127.0.0.1',20113)
sockfd.connect(server_addr) #连接
file="1.jpg"
f=open(file,"rb")
while True:
    #发送消息
    data = f.read(1024)
    if not data:  # 如果data为空的话说明客户端已经退出
        print("客户端退出")
        break
    sockfd.send(data)
    # 接受消息
    data=sockfd.recv(1024)
    print("Server:",data.decode())#打印收纳内容

#关闭套接字
sockfd.close()