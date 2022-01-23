"""
    udp 套接字服务端流程
"""
from socket import *

#创建套接字
sockfd=socket(AF_INET,SOCK_DGRAM)

# 绑定地址
server_addr=("127.0.0.1",20113)
sockfd.bind(server_addr)

#循环收发消息
while True:
    data,addr=sockfd.recvfrom(1024)
    print("收到消息:",data.decode())
    sockfd.sendto(b"Thanks",addr)

# 关闭套接字
sockfd.close()