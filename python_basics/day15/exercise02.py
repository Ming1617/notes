"""
    练习2
    根据生日（年月日），计算活了多少天
"""
import time
def get_live_days(year,momth,day):
    """
        根据生日计算活了多少天
    :param year: 年
    :param momth: 月
    :param day: 日
    :return: 活的天数
    """
    # print(time.time())
    return int(((time.time())-time.mktime(time.strptime("%d%d%d"%(year,momth,day),"%Y%m%d")))/3600/24//1)

print(get_live_days(1998,5,19))