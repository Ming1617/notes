#列表推导式

#练习:使用range生成1--10之间的数字，将数字的平方存入listo1中
# #将list01中所有奇数存入list02
#将list01中所有偶数存入list03
#将listo1中所有偶数大于5的数字增加1后存入list04

list01=[i**2 for i in range(1,11)]
list02=[item for item in list01 if item%2==1]
list03=[item for item in list01 if item%2==0]
list04=[item+1 for item in list01 if item%2==0 and item>5]
print(list01)
print(list02)
print(list03)
print(list04)