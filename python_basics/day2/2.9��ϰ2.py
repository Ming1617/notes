# Author:Eric
# -*- codeing = utf-8 -*-
# @Time:2021/8/4 21:12
# @Author:Ming
# @Site  :
# @File  :2.9练习2.py
# @Software:PyCharm
day=int(input("请输入天数："))
hour=int(input("请输入小时："))
minute=int(input("请输入分钟："))
print("共计%d秒"%((day*24*60+hour*60+minute)*60))