"""
    继承 -- 设计(2)
    练习:exercise03.py
"""


# 需求：老张开车去东北
# 变化：    坐飞机
#          坐火车
#          骑车
#          ...

class Vehicle:
    """
        交通工具,代表所有具体的交通工具(火车/飞机..)
        继承：隔离子类变化,将子类的共性(坐/飞..)提取到父类(运输)中.
    """

    def transport(self, str_position):
        # 因为父类太过于抽象，所以写不出方法体.
        pass


# 客户端代码，用交通工具。
class Person:
    def __init__(self, name):
        self.name = name

    def go_to(self, vehicle, str_position):
        # 多态：调用父，执行子.
        # 调用的是交通工具的运输方法
        # 执行的是飞机的运输方法或者汽车的运输方法
        vehicle.transport(str_position)


# -------以上是架构师完成的--以下是程序员完成的-----
class Car(Vehicle):
    def transport(self, str_position):
        print("汽车开到", str_position)


class Airplane(Vehicle):
    def transport(self, str_position):
        print("飞机飞到", str_position)


p01 = Person("老张")
c01 = Car()
a01 = Airplane()
p01.go_to(c01, "东北")
p01.go_to(a01, "东北")
