"""
定义转几斤几两函数
"""
def conversion_weight(weight):
    """
    从两转换到几斤几两
    :param weight:两
    :return: 几斤几两
    """
    return (weight//16,weight%16)
print(conversion_weight(20))