"""
    时间处理
"""
import time

# 1.获取当前时间戳(从1970年1月1日到现在经过的秒数)
# 1633355166.6431766
print(time.time())

# 2.时间元组(年，月，日，时，分，秒，一周的第几天，一年的第几天，夏令时)
# 时间戳-->时间元组
print(time.localtime(1633355166))
tuple_time=time.localtime()
for item in time.localtime():
    print(item)
print(time.localtime()[0])#获取年
print(tuple_time.tm_year)

# 时间元组-->时间戳
print(time.mktime(tuple_time))

#时间元组---> str
str_time01=time.strftime("%Y / %m / %d %H：%M：%S",tuple_time)
print(str_time01)

#str--->时间元组
print(time.strptime(str_time01,"%Y / %m / %d %H：%M：%S"))
