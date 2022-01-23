"""
    使用with语句打开文件
"""

with open("day02.txt") as f: # 生成文件对象
    data=f.read()
    print(data)

# with语句快结束 f 对象被自动销毁