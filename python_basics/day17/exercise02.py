"""
    #需求1:在列表中查找所有偶数
    #需求2:在列表中查找所有大于10的数
    #需求3:在列表中查找所有范围在10- -50之间的数
    #使用生成器函数实现以上三个需求
    # 1.将三个函数变化点提取到另外三个函数中
    # 2.将共性提取到另外一个函数中
    # 3.体会函数式变成的“继承”与“多态”
        使用变量隔离变化点，在共性函数中调用变量
    # 4.测试
"""
list01=[43,54,6,5,65,7]

def fun01(list_temp):
    for item in list_temp:
        if item%2==0:
            yield item

for item in fun01(list01):
    print(item)

def fun02(list_temp):
    for item in list_temp:
        if item>10:
            yield item

for item in fun02(list01):
    print(item)

def fun03(list_temp):
    for item in list_temp:
        if 10<=item<=50:
            yield item

for item in fun03(list01):
    print(item)

def find_count1(item):
    return item%2==0

def find_count2(item):
    return item>10

def find_count3(item):
    return 10<=item<=50

def find(find_cont):
    for item in list01:
        if find_cont(item):
            yield item

for item in find(lambda item: 10<=item<=50):
    print(item)