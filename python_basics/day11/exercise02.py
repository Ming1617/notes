"""
练习：定义敌人类（姓名。攻击力10---50，血量100---200）
    创建一个敌人对象，可以修改数据，读取数据
"""
class Enemy:
    def __init__(self,name,ATK,HP):
        self.name=name
        self.set_ATK(ATK)
        self.set_HP(HP)
    def get_ATK(self):
        return self.__ATK

    def set_ATK(self,value):
        if value>9 and value<51:
            self.__ATK=value
        else:
            raise ValueError("不符合标准")

    def get_HP(self):
        return self.__HP

    def set_HP(self,value):
        if value>99 and value<201:
            self.__HP=value
        else:
            raise ValueError("不符合标准")

e01=Enemy("灭霸",11,200)
print(e01.get_ATK())
e01.set_HP(150)
print(e01.get_HP())