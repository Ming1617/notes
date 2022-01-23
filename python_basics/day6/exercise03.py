"""
练习:在控制台中录入日期(年月)﹐计算这是这一年的第几天
例如∶3月5日
1月天数＋2月天数+5

"""
tuple_days=(31,29,31,30,31,30,31,31,30,31,30,31)
str_date=input("请输入几月几日：")
month=int(str_date.split("月")[0])
day=int((str_date.split("月")[1]).split("日")[0])
# print(tuple_days[0:month-1])
print("这是本年的第%d天"%(sum(tuple_days[0:month-1])+day))
