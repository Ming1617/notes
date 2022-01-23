"""
    文件读取演示
"""

#打开文件
f=open("test1.txt", 'r', encoding="utf-8")
while True:
    # 读取文件结尾返回空字符串
    data=f.read(100)#每次最多读100字符
    if not data: # 读到结尾跳出循环
        break
    print(data)
#关闭
f.close()