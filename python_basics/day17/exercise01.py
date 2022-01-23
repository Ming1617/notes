"""
    #练习:定义生成器函数my_zip,实现下列现象.
    #将多个列表的每个元素合成一个元组.
"""
list01=["孙悟空","猪八戒","唐僧","沙僧"]
list02=[1001,1002,1003,1004]
for item in zip(list01,list02):
    print(item)

def my_zip(list1,list2):
    try:
        for item in range(len(list1)):
            yield (list1[item],list2[item])
    except IndexError:
        pass

my_zip01=my_zip(list01,list02)
for item in my_zip01:
    print(item)