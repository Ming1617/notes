"""
从终端输入一个单词
从单词本中找到该单词﹐打印解释内容
如果找不到则打印"找不到”
"""
word = input("Word：")

# 默认r打开
f=open("dict.txt",encoding="utf-8")

#每次获取一行
for line in f:
    w=line.split(" ")[0]
    if w>word:
        print("没有找到该单词")
        break
    elif w == word:
        print(line)
        break
else:
    print("没有该单词")

f.close()