"""
    udp客户端流程
"""

from  socket import *

#创建套接字
sockfd=socket(AF_INET,SOCK_DGRAM)
#服务器地址
ADDR=("127.0.0.1",20113)

#循环收发消息
while True:
    data=input("Msg>>")
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    msg,addr=sockfd.recvfrom(1024)
    print("From server:",msg.decode())
sockfd.close()