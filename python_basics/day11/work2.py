"""
4. 请用面向对象思想，描述以下场景：
    玩家(攻击力)攻击敌人(血量)，敌人受伤(掉血)，还可能死亡(掉装备，加分)。
    敌人(攻击力)攻击玩家，玩家(血量)受伤(掉血/碎屏),还可能死亡(游戏结束)。
    体会：类区别行为的不同
"""
class Player:
    def __init__(self,hp,atk):
        self.hp=hp
        self.atk=atk

    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self,value):
        self.__hp=value

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        self.__atk = value

    def damge(self, value):
        print("玩家受伤了")
        self.hp -= value
        if self.hp <= 0:
            self.__die()

    def __die(self):
        print("玩家死亡")
        print("游戏结束")

    def attack(self, other):
        print("玩家攻击敌人")
        other.damge(self.__atk)


class Enemy:
    def __init__(self,hp,atk):
        self.hp=hp
        self.atk=atk

    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self,value):
        self.__hp=value

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        self.__atk = value

    def damge(self,value):
        print("敌人受伤了")
        self.hp-=value
        if self.hp<=0:
            self.__die()

    def __die(self):
        print("敌人死亡")
        print("累计积分")
        print("掉落装备")

    def attack(self,other):
        print("敌人攻击玩家")
        other.damge(self.__atk)

p01 = Player(1000, 100)
e01 = Enemy(200, 10)
p01.attack(e01)
e01.attack(p01)

p01.attack(e01)