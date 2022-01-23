"""
    发送请求，展现请求结果
"""
from  socket import *

#创建套接字
sockfd=socket(AF_INET,SOCK_DGRAM)
#服务器地址
ADDR=("192.168.226.1",20113)

#循环收发消息
while True:
    data=input("Word>>")
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR) #发送单词
    msg,addr=sockfd.recvfrom(1024) #得到返回的单词解释
    print("From server:",msg.decode())
sockfd.close()