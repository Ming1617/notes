"""
    定义父类
        动物（行为∶叫)
    定义子类
        狗（行为∶跑)
        鸟（行为∶飞)
    创建三个类型的对象
    体会: isinstance(对象，类型)
    体会: issubclass(类型，类型）

"""
class Animal:
    def cry(self):
        print("叫")

class Dog(Animal):
    def runing(self):
        print("跑")

class Bird(Animal):
    def fly(self):
        print("飞")

