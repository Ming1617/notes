"""
    使用udp完成，
    客户端不断录入学生信息
    将其发送到服务端，在服务端，将学生信息写入到一个文件中，
    每个学生信息占一行

    发送端
"""

from socket import *
import struct

#数据格式1定义
st=struct.Struct('i32sif')

#创建套接字
sockfd=socket(AF_INET,SOCK_DGRAM)

# 绑定地址
ADDR=("192.168.1.100",20113)


#循环收发消息
while True:
    print('====================')
    id=int(input("ID:"))
    name=input("Name：").encode()
    age=int(input("Age:"))
    score=float(input("Score:"))
    #打包数据发送
    data=st.pack(id,name,age,score)
    sockfd.sendto(data,ADDR)
# 关闭套接字
sockfd.close()