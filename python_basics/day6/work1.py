"""
将1970年到2050年中的闰年﹐存入列表
"""
list_leapyear=[]
for i in range(1970,2051):
    if (i % 4==0 and i%100 !=0) or i % 400 ==0 :
        list_leapyear.append(i)
print(list_leapyear)

#列表推导式
list_leapyear=[i for i in range(1970,2051) if (i % 4==0 and i%100 !=0) or i % 400 ==0]
print(list_leapyear)