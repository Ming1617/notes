"""
    11:05 上课
    封装数据：老婆(姓名,年龄,性别...)
            敌人(姓名,血量,攻击力,防御力)
            二维向量(x,y)
            优势:更符合人类的思考方式。
                 将数据与对数据的操作整合在一起.

    封装行为：二维列表助手类DoubleListHelper（获取多个元素get_elements）
            向量(向左／向右．．，求模长,求方向..)
            优势:以“模块化”的方式进行编程
                （可以集中精力设计／组织／指挥多个类协同工作）
"""

# 使用方法，封装变量.
class Wife:
    def __init__(self, name, age, weight):
        self.name = name
        # 本质:障眼法(实际将变量名改为：_类名__age)
        # self.__age = age
        self.set_age(age)
        # self.__weight = weight
        self.set_weight(weight)

    # 提供公开的读写方法
    def get_age(self):
        return self.__age

    def set_age(self, value):
        if 21 <= value <= 31:
            self.__age = value
        else:
            raise ValueError("我不要")

    # 提供公开的读写方法
    def get_weight(self):
        return self.__weight

    def set_weight(self, value):
        if 40 <= value <= 60:
            self.__weight = value
        else:
            raise ValueError("我不要")

"""
w01 = Wife("铁锤公主", 87, 87)
# 重新创建了新实例变量(没有改变类中定义的__age)
# w01.__age = 107　
w01._Wife__age = 107  # (修改了类中定义的私有变量)

print(w01.__dict__)# python内置变量,存储对象的实例变量.
"""

w01 = Wife("铁锤公主", 30, 50)
w01.set_age(25)
w01.set_weight(55)
print(w01.get_age())
print(w01.get_weight())