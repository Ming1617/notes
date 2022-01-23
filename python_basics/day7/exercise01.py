"""
#练习:["无忌"，"赵敏”，"周芷若"]
##->{"无忌":2,"赵敏":2,"周芷若":3}
"""
list01=["无忌","赵敏","周芷若"]
dist01={}
for item in list01:
    dist01[item]=len(item)
dist02={item:len(item) for item in list01}
print(dist01)
print(dist02)