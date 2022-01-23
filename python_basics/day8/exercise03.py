"""
方阵转置函数
"""
def matrix_transposition(matrix):
    """
    方阵转置
    :param matrix: 二维方阵
    :return:
    """
    for c in range(1,len(matrix)):
        for r in range(c,len(matrix)):
            matrix[r][c-1],matrix[c-1][r]=matrix[c-1][r],matrix[r][c-1]

matrix01=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
matrix_transposition(matrix01)
print(matrix01)