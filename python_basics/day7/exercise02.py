"""
#练习:["无忌"，"赵敏"，"周芷若"] [ 101,102,103]
# {无忌":101,"赵敏":102,"周芷若":103}
"""
list01=["无忌","赵敏","周芷若"]
list02=[101,102,103]
dict01={}
for i in range(len(list01)):
    dict01[list01[i]]=list02[i]
print(dict01)
dict02={list01[i]:list02[i] for i in range(len(list01))}
print(dict02)
