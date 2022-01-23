"""
定义计算四位整数，每位相加和的函数
"""
def Sum_Fourinteger(int_Number):
    """
    计算四位整数，每位相加和
    :param int_Number: 四位整数
    :return: 每位相加和
    """
    result=int_Number%10
    #累加十位
    result+=int_Number//10%10
    #累加百位
    result+=int_Number//100%10
    #累加千位
    result+=int_Number//1000
    return result
print(Sum_Fourinteger(1234))
