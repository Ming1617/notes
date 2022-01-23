"""
    使用udp完成，
    客户端不断录入学生信息
    将其发送到服务端，在服务端，将学生信息写入到一个文件中，
    每个学生信息占一行

    接收端
"""

from socket import *
import struct

#数据格式1定义
st=struct.Struct('i32sif')

#创建udp套接字
sockfd=socket(AF_INET,SOCK_DGRAM)
# 绑定地址
sockfd.bind(("127.0.0.1",20113))

#打开文件
f=open("student.txt","a")



#循环收发消息
while True:
    data,addr=sockfd.recvfrom(1024)
    #(1,b'Lily',16,80.5)
    data=st.unpack(data)

    #写入文件
    info="%d  %-10s  %d  %.1f\n"%data
    f.write(info)
    f.flush()
# 关闭套接字
sockfd.close()