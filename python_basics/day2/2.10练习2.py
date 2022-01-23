# Author:Eric
# -*- codeing = utf-8 -*-
# @Time:2021/8/4 21:49
# @Author:Ming
# @Site  :
# @File  :2.10练习2.py
# @Software:PyCharm
distance=float(input("请输入距离："))
initial_velocity=float(input("请输入初速度："))
time=float(input("请输入时间："))
print("加速度为：%f"%((distance-initial_velocity*time)*2/time**2))