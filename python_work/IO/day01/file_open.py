#打开文件
try:
    # fd=open("a.py","r")# 以只读打开
    # fd=open("a.py","w")
    fd=open("a.py","r")
    """
    普通的文本文件
    既可以使用文本方式打开也可使用二进制方式打开
    二进制文件则必须以二进制方式打开
    """
    print(fd.read(2))
    print(fd)
except Exception as e:
    fd.close()
    print(e)

# 读写文件

# 关文件