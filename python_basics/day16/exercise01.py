"""
    #练习1∶使用迭代器原理﹐遍历元组.
    #（“铁扇公主"，"铁锤公主"，“扳手王子")
    #练习2：不使用for，获取字典所有数据
    #{“铁扇公主":101，"铁锤公主":102，“扳手王子":103}
"""
tuple_item=("铁扇公主","铁锤公主","扳手王子")
iterator=tuple_item.__iter__()
while True:
    try:
        item=iterator.__next__()
        print(item)
    except StopIteration:
        break

dict_item={"铁扇公主":101,"铁锤公主":102,"扳手王子":103}
iterator=dict_item.values().__iter__()
while True:
    try:
        item=iterator.__next__()
        print(item)
    except StopIteration:
        break