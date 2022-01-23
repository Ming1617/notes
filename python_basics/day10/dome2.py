"""
    静态方法引入
"""

list01=[
    ["00","01","02","03"],
    ["10","11","12","13"],
    ["20","21","22","23"],

]


class Vector2:
    """
    二维向量
    可以表示位置/方向
    """
    def __init__(self,x,y):
        self.x=x
        self.y=y
##函数：表示左边方向
def left():
    return Vector2(0,-1)

##函数：表示右边方向
def right():
    return Vector2(0,1)

#作用：位置+方向
#
pos01=Vector2(1,2)
lo1=left()
pos01.x+=lo1.x
pos01.y+=lo1.y
print(pos01.x,pos01.y)