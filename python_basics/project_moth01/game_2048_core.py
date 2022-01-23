"""
2048 游戏核心算法
"""
list_merge=None


#1.零元素移到末尾
#     [2,0,2,0]--->[2,2,0,0]
#     [2,0,0,2]--->[2,2,0,0]
def zero_to_end():
    """
        零元素移动到末尾
    :return:
    """
    #从后往前，如果发现0元素，删除并追加
    #-1 -2 -3 -4
    for i in range(-1,-len(list_merge)-1,-1):
        if list_merge[i]==0:
            del list_merge[i]
            list_merge.append(0)
# zero_to_end()
# print(list_merge)


#1.零元素移到末尾
#     [2,2,0,0]--->[4,0,0,0]
#     [2,2,0,2]--->[4,2,0,0]

def merge():
    """
        合并
    :return:
    """
    #先将中间的零元素移到末尾
    #再合并相邻元素
    # print(list_merge)
    zero_to_end()
    for i in range(len(list_merge)-1):
        # if list_merge[i]==0 or list_merge[i+1]==0:
        #     break
        if list_merge[i]==list_merge[i+1]:
            list_merge[i]+=list_merge[i+1]
            del list_merge[i+1]
            list_merge.append(0)
# merge(list_merge)
# print(list_merge)

#练习3：地图想左移动
map=[
    [2,0,0,2],
    [2,4,2,2],
    [8,2,0,2],
    [2,4,0,4],
]
def move_left():
    """
        左移
    :return:
    """
    #思想：从二维列表中每行交给merge函数进行操作
    # global map
    for line in map:
        global list_merge
        list_merge=line
        # print(line)
        merge()
# for i in map:
#     merge(i)
# move_left()
# print(map)

def move_right():
    """
        向右移动
    :return:
    """
    #思想:将二维列表的没行（从右向左）交给merge函数操作
    for line in map:
        #global list_merge
        #从右向左取出数据 形成新列表
        list_merge=line[::-1]
        # print(list_merge)
        merge()
        #从右向左接受 合并后的数据
        line[::-1] = list_merge
# move_right()
# print(map)

#练习4：向上移动，向下移动
#提示：利用方阵转置函数
def matrix_transposition(matrix):
    """
    方阵转置
    :param matrix: 二维方阵
    :return:
    """
    for c in range(1,len(matrix)):
        for r in range(c,len(matrix)):
            matrix[r][c-1],matrix[c-1][r]=matrix[c-1][r],matrix[r][c-1]

def move_up():
    """
        向上移动
    :return:
    """
    matrix_transposition(map)
    move_left()
    matrix_transposition(map)

# move_up()
# print(map)


def move_down():
    """
        向下移动
    :return:
    """
    matrix_transposition(map)
    move_right()
    matrix_transposition(map)

move_down()
print(map)






# def move_up():
#     """
#         向上移动
#     :return:
#     """
#     # global map
#     for i in range(len(map)):
#         global list_merge
#         list_merge=[]
#         for j in range(len(map)):
#             list_merge.append(map[j][i])
#         merge()
#         # print(list_merge)
#         for j in range(len(list_merge)):
#             map[j][i]=list_merge[j]
# # move_up()
# # print(map)
# def move_down():
#     """
#         向下移动
#     :return:
#     """
#     for i in range(len(map)):
#         global list_merge
#         list_merge=[]
#         for j in range(-1,-len(map)-1,-1):
#             list_merge.append(map[j][i])
#         print(list_merge)
#         merge()
#         # print(list_merge)
#         for j in range(len(list_merge)):
#             map[j][i]=list_merge[-j-1]
# # move_down()
# # print(map)
