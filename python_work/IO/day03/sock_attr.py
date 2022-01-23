"""
    套接字属性介绍
"""
from socket import *

#创建套接字
s=socket()

#设置端口可以立即重用,在绑定之前进行设置
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,True)

s.bind(('192.168.226.1',20113))
s.listen(3)
c,addr=s.accept()
#查看地址类型：ipv4/ipv6
print("地址类型",s.family)
#流式套接字/数据报套接字
print("套接字类型",s.type)
#绑定地址 #在linux中默认是('0.0.0.0', 0)，
# Windows中直接使用此函数报错(需要添加s.bind并且是正确的地址)
print("绑定地址：",s.getsockname())
#文件描述符  系统分配
print("文件描述符",s.fileno())
#连接段地址,在没有连接时报错，当前套接字无法调用该属性
# print("连接端地址：",s.getpeername())
# 结果同accept的结果调用
print("连接端地址：",c.getpeername()) #连接网络的地址及端口号