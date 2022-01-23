"""
    编写一个文件拷贝程序，从终端输入一个文件，
    将文件保存在当前目录下
    * 文件类型不确定（可能是文本文件，可能是二进制文件）
"""
file=input("请输入一个路径：")
# file="C:/网络科技.pptx"
print(file)
str_file=file.split("/")
str_file[-1]="new_"+str_file[-1]
new_file="/".join(str_file)
print(new_file)
try:
    f=open(file,"rb")
except  FileExistsError as e:
    f.close()
    print(e)
else:
    new_f=open(new_file,"wb")
    while True:
        # 读取文件结尾返回空字符串
        data=f.read(1024)#每次最多读100字符
        # print(data)
        if not data: # 读到结尾跳出循环
            break
        new_f.write(data)
    # print(data)
#关闭
f.close()
new_f.close()
