"""
#练习:在控制台中录入多个人的多个喜好.#例如:请输入姓名∶
#请输入第1个喜好∶
#请输入第2个喜好∶
#. . .
#请输入姓名:
输入空字符停止
最后在控制台打印所有人的所有喜好.

"""
dict_hobby_info={}
while True:
    name=input("请输入姓名:")
    if name == "":
        break
    list_hobby=[]
    while True:
        hobby=input("请输入喜好：")
        if hobby =="":
            break
        list_hobby.append(hobby)
    dict_hobby_info[name]=list_hobby
for key,value in dict_hobby_info.items():
    print("%s的喜好是:" % (key),end='')
    for i in value:
        print(i,end=' ')
    print()
