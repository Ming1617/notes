"""
练习：定义敌人类（姓名。攻击力10---50，血量100---200）
    创建一个敌人对象，可以修改数据，读取数据
    使用property函数
"""
class Enemy:
    def __init__(self,name,ATK,HP):
        self.name=name
        self.ATK=ATK
        self.HP=HP
    def get_ATK(self):
        return self.__ATK
    def set_ATK(self,value):
        if value>9 and value<51:
            self.__ATK=value
        else:
            raise ValueError("不符合标准")
    ATK=property(get_ATK,set_ATK)

    def get_HP(self):
        return self.__HP
    def set_HP(self,value):
        if value>99 and value<201:
            self.__HP=value
        else:
            raise ValueError("不符合标准")
    HP = property(get_HP, set_HP)
e01=Enemy("灭霸",11,200)
print(e01.ATK)
print(e01.__dict__)