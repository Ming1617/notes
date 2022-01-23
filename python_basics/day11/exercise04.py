"""
练习：定义敌人类（姓名。攻击力10---50，血量100---200）
    创建一个敌人对象，可以修改数据，读取数据
    使用property封装变量
"""
class Enemy:
    def __init__(self,name,ATK,HP):
        self.name=name
        self.ATK=ATK
        self.HP=HP
    @property  #创建property对象，只负责拦截读取数据
    def ATK(self):
        return self.__ATK
    @ATK.setter #只负责拦截修改数据
    def ATK(self,value):
        if value>9 and value<51:
            self.__ATK=value
        else:
            raise ValueError("不符合标准")
    @property
    def HP(self):
        return self.__HP
    @HP.setter
    def HP(self,value):
        if value>99 and value<201:
            self.__HP=value
        else:
            raise ValueError("不符合标准")

e01=Enemy("灭霸",11,200)
print(e01.ATK)
print(e01.__dict__)