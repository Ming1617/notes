"""
    沾包演示
"""

from socket import *
from time import sleep
#创建tcp套接字
sockfd=socket()
#绑定地址
sockfd.bind(('0.0.0.0',20113))
#设置监听
sockfd.listen(5)

connfd,addr=sockfd.accept()

while True:
    # sleep(1)
    data=connfd.recv(1024)
    if not data:
        break
    print(data.decode())