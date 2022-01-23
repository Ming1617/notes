"""
    将一个文件从客户端发送到服务端保存
    *文件可能是文本类型也可能是二进制文件
    exercise01 && exercise02
"""
import socket

#创建tcp套接字
sockfd=socket.socket(socket.AF_INET,
                     socket.SOCK_STREAM)

#绑定地址
sockfd.bind(('0.0.0.0',20113))

#设置监听
sockfd.listen(5)
new_file = "2.jpg"
while True:
    #阻塞等待处理链接
    print("waiting for connect...")
    try:
        connfd,addr=sockfd.accept()
        print("connect from",addr)#打印链接的客户端地址
    except KeyboardInterrupt:
        print("Server exit")
    except  Exception as e:
        print(e)
    new_f = open(new_file, "wb")
    while True:
        # 收发消息
        data=connfd.recv(1024)
        if not data:#如果data为空的话说明客户端已经退出
            break
        new_f.write(data)
        # print(data.decode())
        n=connfd.send(b'Thanks') # 发送字节串
        print("发送%d字节"%n)
    new_f.close()
    connfd.close()
# 关闭套接字
sockfd.close()

