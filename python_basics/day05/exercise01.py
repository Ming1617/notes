
"""
#计算列表最小值
list01=[26,37,77,56,10,11]
list_min=list01[0]
for i in range(1,len(list01)):
    if list01[i]<list_min:
        list_min=list01[i]
print(list_min)

"""
import random
list_temp=[]
for i in range(6):
    list_temp.append(int(random.sample(range(1, 34), 1)[0]))
list_temp.append(random.randint(1,16))
print(list_temp)
list_test=[]
i=1
while True:
    temp=int(input("请输入第"+str(i)+"个红色球："))
    if temp in list_test:
        print("号码已经重复！")
        continue
    if temp >0 and temp<34:
        list_test.append(temp)
        i += 1
    else:
        print("号码不在范围内！")
    if len(list_test)==2:
        temp=int(input("请输入蓝色球："))
        list_test.append(temp)
        break
count=0
for i in list_test:
    if i in list_temp:
        count+=1
print(list_test)
