"""
    练习 使用udp客户端查询单词，得到单词的解释，
    如果没有该单词则得到“没有单词”。客户端可以循环输入
    单词，直到输入空退出

    服务端提供逻辑和数据处理
"""
from socket import *

#创建套接字
sockfd=socket(AF_INET,SOCK_DGRAM)

# 绑定地址
server_addr=("0.0.0.0",20113)
sockfd.bind(server_addr)


def find_word(word):
    # 默认r打开
    f = open("dict.txt", encoding="utf-8")
    # 每次获取一行
    for line in f:
        w = line.split(" ")[0]
        # 如果遍历到的单词已经大于word就结束查找
        if w > word:
            f.close()
            return "没有找到该单词"
        elif w == word:
            # print(line)
            f.close()
            return line
    else:
        f.close()
        return "没有该单词"


#循环收发消息
while True:
    data,addr=sockfd.recvfrom(1024)
    #查单词
    word = data.decode()
    data=find_word(word)
    sockfd.sendto(data.encode(),addr)

# 关闭套接字
sockfd.close()