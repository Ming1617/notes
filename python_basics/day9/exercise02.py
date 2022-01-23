# dict_students={}
# while True:
#     key=input("请输入学生姓名：")
#     if key=="":
#         break
#     value={}
#     age=int(input("请输入年龄："))
#     value["age"]=age
#     score=int(input("请输入成绩："))
#     value["score"] = score
#     sex=input("请输入性别：")
#     value["sex"] = sex
#     dict_students[key]=value
# print(dict_students)
# for key,value in dict_students.items():
#     print("%s的年龄是%d成绩是%d性别是%s"%(key,value["age"],value["score"],value["sex"]))

class Sutent():
    def __init__(self,name,age,score,sex):
        self.name=name
        self.age=age
        self.score=score
        self.sex=sex
    def print_self_info(self):
        print("%s的年龄是%d成绩是%d性别是%s" % (self.name, self.age, self.score, self.sex))
list_student=[]
while True:
    name=input("请输入学生姓名：")
    if name=="":
        break
    age = int(input("请输入年龄："))
    score = int(input("请输入成绩："))
    sex = input("请输入性别：")
    list_student.append(Sutent(name, age, score, sex))
for stu in list_student:
    # stu.print_self_info()
    print(stu)
info=list_student[0]
info.print_self_info()