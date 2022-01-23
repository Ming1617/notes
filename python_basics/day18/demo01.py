from common.list_helper import *
class Enemy:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

    def __str__(self):
        return "%s--%d--%d--%d" % (self.name, self.hp, self.atk, self.defense)


list01 = [
    Enemy("玄冥二老", 86, 120, 58),
    Enemy("成昆", 0, 100, 5),
    Enemy("谢逊", 120, 130, 60),
    Enemy("灭霸", 0, 1309, 690),
]
for i in ListHelper.find_all(list01,lambda item:item.hp==0):
    print(i)

for i in filter(lambda item:item.hp==0,list01):
    print(i)

#2.获取所有敌人的姓名
for i in ListHelper.select(list01,lambda item:item.name):
    print(i)

for i in map(lambda item:item.name,list01):
    print(i)

tuple01=([1,1,1],[2,2],[3,3,3,3])
print(max(tuple01,key=lambda item:len(item)))
# for i in filter(lambda item:max(len(item)),tuple01):
#     print(i)
print(min(tuple01,key=lambda item:len(item)))

for i in map(lambda item:(item.name,item.hp,item.atk),list01):
    print(i)

for i in filter(lambda item:item.atk>100 and item.hp>0,list01):
    print(i)

for i in sorted(list01,key=lambda item:item.atk,reverse=True):
    print(i)