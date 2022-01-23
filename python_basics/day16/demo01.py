"""
    迭代
"""
list_item=[45,34,2,15,56]
# 迭代原理
# 面试题：for循环的原理是什么？
#        答：1. 获取迭代器
#           2. 循环获取下一个元素
#           3. 遇到异常停止迭代

#        可以被for的条件是什么？
#        答：能被for的对象必须具备__iter__方法
#        答：能被for的对象是可迭代对象
iterable=list_item.__iter__()

while True:
    try:
        item=iterable.__next__()
        print(item)
    except StopIteration:
        break