"""
    httpserver v1.0
    基本要求：1.获取来自浏览器的请求
            2.判断如何请求内容是/ 将index.html返回给客户端
            3.如果请求的是其他内容则返回404
"""
from socket import *

#客户端（浏览器）处理
def request(connfd):
    #将获取请求将请求内容提取出来
    data=connfd.recv(4096)#接收请求
    if not data:
        return
    # print(data.decode().split(" ")[1])
    info=data.decode().split(" ")[1]
    #判断是/ 则返回index.html 不是则返回404
    # response=""
    if info=="/":
        with open('index.html',encoding="utf-8")as f:
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += f.read()
    else:
        response = """HTTP/1.1 404 Found
                Content-Type:text/html

                <h1>Sorry......404</h1>
                """
    connfd.send(response.encode())  # 发送响应内容


#搭建tcp网络
sockfd=socket()
#设置端口重用
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

sockfd.bind(("0.0.0.0",8000))
sockfd.listen(3)
while True:
    connfd,addr=sockfd.accept()
    request(connfd) #处理客户端请求