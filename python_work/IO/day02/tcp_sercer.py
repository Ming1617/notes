"""

"""
import socket

#创建tcp套接字
sockfd=socket.socket(socket.AF_INET,
                     socket.SOCK_STREAM)

#绑定地址
sockfd.bind(('127.0.0.1',20113))

#设置监听
sockfd.listen(5)

#阻塞等待处理链接
print("waiting for connect...")
connfd,addr=sockfd.accept()
print("connect from",addr)#打印链接的客户端地址

# 收发消息
data=connfd.recv(1024)
print("收到：",data)
n=connfd.send(b'Thanks') # 发送字节串
print("发送%d字节"%n)

# 关闭套接字
connfd.close()
sockfd.close()