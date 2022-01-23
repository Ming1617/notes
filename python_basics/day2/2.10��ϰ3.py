# Author:Eric
# -*- codeing = utf-8 -*-
# @Time:2021/8/4 22:06
# @Author:Ming
# @Site  :
# @File  :2.10练习3.py
# @Software:PyCharm
"""
    练习：
    在控制台录入一个四位数：1234
    计算每位相加和   1+2+3+4
    显示结果
"""
number=int(input("输入一个四位数："))
units_digit=number%10
ten_digit=number//10%10
hundreds_digit=number//100%10
thousand_digit=number//1000
print(str(number)+"的结果是%d"%(units_digit+ten_digit+hundreds_digit+thousand_digit))