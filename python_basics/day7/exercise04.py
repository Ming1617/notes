"""
练习:矩阵转置将二维列表的列，变成行.
第一列变成第一行
第二列变成第二行
第三列变成第三行
第四列变成第四行

"""
list01=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
list02=[]
for i in range(len(list01)):
    list_temp=[]
    for j in range(len(list01[i])):
        list_temp.append(list01[j][i])
    list02.append(list_temp)
print(list02)