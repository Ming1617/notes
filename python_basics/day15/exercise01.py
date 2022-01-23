"""
    练习1：定义函数，根据年月日，返回星期数
    “星期一”
    “星期二”
    “星期三”
    。。。
"""
import time
def get_week(year, momth, day):
    """
        获取星期几
    :param year: 年
    :param momth: 月
    :param day: 日
    :return: str 星期几
    """
    str_temp=str(year)+str(momth)+str(day)
    str_wday=["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
    return str_wday[time.strptime(str_temp,"%Y%m%d")[6]]
print(get_week(2021, 10, 4))