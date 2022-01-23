"""
3．定义在控制台中打印二维列表的函数
[
[1,2,3,44],
[4,5,5,5,65,6,87],
[7,5]
]

"""
def print_lists(list_temp):
    """
    打印一个二维数组
    :param list_temp: 二维数组
    :return: None
    """
    for i in list_temp:
        for j in i:
            print(j,end=" ")
        print()
list01=[
[1,2,3,44],
[4,5,5,5,65,6,87],
[7,5]
]
print_lists(list01)
