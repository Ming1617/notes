"""
    使用property(读取方法,写入方法，封装变量)
"""
class Wife:
    def __init__(self,name,age,weight):
        self.name=name
        #本质:障眼法
        self.age=age
        self.weight=weight

    #提供公开的读写方法
    def get_age(self):
        return self.__age
    def set_age(self,value):
        if 21<= value <=31:
            self.__age=value
        else:
            raise ValueError("我不要")
    #属性 property对象拦截对age类变量的读写操作
    age=property(get_age,set_age)
    def get_weight(self):
        return self.__weight
    def set_weight(self,value):
        if 41<= value <=51:
            self.__weight=value
        else:
            raise ValueError("我不要,太重了")

    weight = property(get_weight, set_weight)

"""

w01=Wife("铁锤公主",87,87)
# 重新创建了新实例变量(没有改变类中定义的__age)
# w01.__age=107
print(w01.name)
w01._Wife__age=107#(修改了类中定义的私有变量)
# print(w01.__age)
print(w01.__dict__)#python内置变量,存储对象的实例变量
# print(w01.weight)

"""
w01=Wife("铁锤公主",24,42)
w01.age=25
w01.weight=45
print(w01.weight)