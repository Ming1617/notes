"""
#练习1:在控制台中循环录入学生信息(姓名，年龄,成绩,性别).
#如果名称输入空字符，则停止录入，.
#将所有信息逐行打印出来．

#列表套字典
"""
dict_students=[]
while True:
    dict_info = {}
    name=input("请输入学生姓名：")
    if name=="":
        break
    dict_info["name"]=name
    age=int(input("请输入年龄："))
    dict_info["age"]=age
    score=int(input("请输入成绩："))
    dict_info["score"] = score
    sex=input("请输入性别：")
    dict_info["sex"] = sex
    dict_students.append(dict_info)
# print(dict_students)
for dict_info in dict_students:
    print("%s的年龄是%d成绩是%d性别是%s" % (dict_info["name"], dict_info["age"], dict_info["score"], dict_info["sex"]))
dict_info=dict_students[0]
print("第一个录入的是%s，年龄是%d成绩是%d性别是%s" % (dict_info["name"], dict_info["age"], dict_info["score"], dict_info["sex"]))