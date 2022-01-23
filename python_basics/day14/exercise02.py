"""
# 练习：创建Enemy类对象，将对象打印在控制台中(格式自定义)
#      克隆Enemy类对象，体会克隆对象变量的改变不影响原对象。

class Enemy:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
"""


class Enemy:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

    def __str__(self):
        return "我是%s,hp：%d,atk:%d,defense:%d"%(self.name,self.hp,self.atk,self.defense)

    def __repr__(self):
        return "Enemy('%s',%d,%d,%d)"%(self.name,self.hp,self.atk,self.defense)

e01=Enemy("灭霸",1000,100,200)
print(e01)

e02=eval(repr(e01))
print(e02)
e02.name="灰太狼"
print(e02)
print(e01)