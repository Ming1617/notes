"""
#练习:列表的全排列
#[“香蕉”，"苹果"，"哈密瓜"]
#[“可乐”,"牛奶"】
"""
list01=["香蕉","苹果","哈密瓜"]
list02=["可乐","牛奶"]
list03=[i+j for i in list01 for j in list02]
print(list03)