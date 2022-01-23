# Author:Eric
# -*- codeing = utf-8 -*-
# @Time:2021/8/4 20:49
# @Author:Ming
# @Site  :
# @File  :2.9练习.py
# @Software:PyCharm
danjia=float(input("请输入单价："))
count=float(input("请输入数量："))
sum=float(input("请输入总金额："))
if not(sum-danjia*count<0):
    print("共收：%d元，本次消费：%d元，找零为：%d"%(sum,danjia*count,float(sum-danjia*count)))
else:
    print("金额不够，共需%d元，还需补齐%d元"%(danjia*count,-float((sum-danjia*count))))
