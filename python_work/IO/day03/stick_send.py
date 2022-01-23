

from socket import *
from time import sleep
#创建tcp套接字
sockfd=socket()

# 连接服务器
server_addr=('127.0.0.1',20113)
sockfd.connect(server_addr) #连接

for i in range(10):
    # sleep(0.1)
    sockfd.send(b"msg"+b"#")