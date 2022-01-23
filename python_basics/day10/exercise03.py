class Sutent():
    def __init__(self,name,age,score,sex):
        self.name=name
        self.age=age
        self.score=score
        self.sex=sex
    def print_self_info(self):
        print("%s的年龄是%d成绩是%d性别是%s" % (self.name, self.age, self.score, self.sex))

# while True:
#     name=input("请输入学生姓名：")
#     if name=="":
#         break
#     age = int(input("请输入年龄："))
#     score = int(input("请输入成绩："))
#     sex = input("请输入性别：")
#     list_student.append(Sutent(name, age, score, sex))
# for stu in list_student:
#     # stu.print_self_info()
#     print(stu)
# info=list_student[0]
# info.print_self_info()
list01=[Sutent("张三",20,89,"男"),
              Sutent("李四",21,81,"女"),
              Sutent("王二",24,85,"男"),
              Sutent("苏大强",28,90,"女"),
              Sutent("麻子",30,87,"男")]
"""
#练习1:定义函数，在list01中查找name是"苏大强"的对象.
#将名称与年龄打印在控制台中

"""
def find01():
    for lis in list01:
        if lis.name=="苏大强":
           return lis
# stu=find01()
# print(stu.name,stu.age)
"""
#练习2:定义函数，在list01中查找sex是"女"的对象.
#将名称与年龄打印在控制台中
"""
def find02():
    list_woman=[]
    for lis in list01:
        if lis.sex == "女":
            list_woman.append(lis)
    return list_woman
# list_woman=find02()
# for stu in list_woman:
#     print(stu.name, stu.sex)

"""
#练习3:定义函数，查找年龄>=24的学生数量
"""
def fun03():
    sum=0
    for lis in list01:
        if lis.age >=  24:
            sum+=1
    return sum
# sum=fun03()
# print(sum)

"""
#练习4:定义函数，将list01中所有学生的成绩归零.
"""
def fun04():
    for lis in list01:
        lis.score=0
# fun04()
# for item in list01:
#     print(item.score,item.name)

"""
#练习5:获取list01中所有学生的名字
"""
def fun05():
    list_std_name=[]
    for item in list01:
        list_std_name.append(item.name)
    return list_std_name
# list_std_name=fun05()
# print(list_std_name)

"""
#练习6:定义函数﹐在list01中查找年龄最大的学生对象
"""
def find06():
    min_object=list01[0]
    for item in list01:
        if min_object.age<item.age:
            min_object=item
    return min_object
min_object=find06()
min_object.print_self_info()
