"""
#练习1:在控制台中循环录入学生信息(姓名，年龄,成绩,性别).
#如果名称输入空字符，则停止录入，.
#将所有信息逐行打印出来．

字典套字典
"""
dict_students={}
while True:
    key=input("请输入学生姓名：")
    if key=="":
        break
    value={}
    age=int(input("请输入年龄："))
    value["age"]=age
    score=int(input("请输入成绩："))
    value["score"] = score
    sex=input("请输入性别：")
    value["sex"] = sex
    dict_students[key]=value
print(dict_students)
for key,value in dict_students.items():
    print("%s的年龄是%d成绩是%d性别是%s"%(key,value["age"],value["score"],value["sex"]))