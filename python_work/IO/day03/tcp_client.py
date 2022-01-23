"""
    tcp客户端
"""
from socket import *

#创建tcp套接字
sockfd=socket()

# 连接服务器
server_addr=('192.168.226.1',20113)
sockfd.connect(server_addr) #连接
while True:
#发送消息
    data=input("Msg>")
    if not data:  # 如果data为空的话说明客户端已经退出
        break
    sockfd.send(data.encode())
    # 接受消息
    data=sockfd.recv(1024)
    print("Server:",data.decode())#打印收纳内容

#关闭套接字
sockfd.close()