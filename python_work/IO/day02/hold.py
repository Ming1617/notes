"""
    空洞文件
"""

f=open("test2.txt","wb")

f.write(b'star')
f.seek(1024*1024,2)# 从结尾向后移动1k
f.write(b"end")
f.close()