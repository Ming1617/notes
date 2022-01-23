"""
#练习1:在控制台中循环录入学生信息(姓名，年龄,成绩,性别).
#如果名称输入空字符，则停止录入，.
#将所有信息逐行打印出来．

字典套列表
"""
dict_shoop={}
while True:
    key=input("请输入学生姓名：")
    if key=="":
        break
    value=[]
    value.append(int(input("请输入年龄：")))
    value.append(int(input("请输入成绩：")))
    value.append(input("请输入性别："))
    dict_shoop[key]=value
for key,value in dict_shoop.items():
    print("%s的年龄是%d成绩是%d性别是%s"%(key,value[0],value[1],value[2]))
