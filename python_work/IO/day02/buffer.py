"""
    文件读写缓冲机制

    缓冲区刷新条件：
    1.缓冲区满了
    2.行缓冲区换行时会自动刷新
    3.程序运行结束或者文件close关闭
    4。调用flush（）函数
"""

f= open("test.txt","w")

while True:
    data=input(">>")
    if not data:
        break
    f.write(data)
    f.flush() # 刷新缓冲

f.close()