"""
    每月多少天
"""
tuple_days=([4,6,9,11],[2])
month=int(input("请输入几月："))
if month<1 or month>12:
    print("输入有误")
elif month in tuple_days[0]:
    print("本月有30天")
elif month in tuple_days[1]:
    print("本月有28天")
else:
    print("本月有31天")
