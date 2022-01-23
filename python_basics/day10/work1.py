"""
4．定义敌人类
数据:姓名，血量，基础攻击力，防御力--行为:打印个人信息
创建敌人列表(至少4个元素)，并画出内存图
查找姓名是"灭霸"的敌人对象
查找所有死亡的敌人
计算所有敌人的平均攻击力
删除防御力小于10的敌人
将所有敌人攻击力增加50I
"""
class Enemy:
    def __init__(self,name,HP,AKT,AC):
        self.name=name
        self.HP=HP
        self.AKT = AKT
        self.AC = AC
    def print_self_info(self):
        print("name:"+self.name,"HP:"+str(self.HP),"AKT:"+str(self.AKT),"AC:"+str(self.AC))

Enemy_list=[
    Enemy("威震天",1000,20,30),
    Enemy("大大怪",800,20,60),
    Enemy("小小怪",0,20,9),
    Enemy("灭霸",1200,60,80),
]
#打印
for eney in  Enemy_list:
    eney.print_self_info()

#查找姓名是"灭霸"的敌人对象
def find01():
    for eney in Enemy_list:
        if eney.name == "灭霸":
            return eney

if find01():
    find01().print_self_info()

#查找所有死亡的敌人
def find02():
    list_result=[]
    for eney in Enemy_list:
        if eney.HP == 0:
            list_result.append(eney)
    return list_result
list_result=find02()
for item in list_result:
    item.print_self_info()

#计算所有敌人的平均攻击力
def calculate01():
    Enemy_AKT_sum = 0
    for eney in Enemy_list:
        Enemy_AKT_sum += eney.AKT
    return Enemy_AKT_sum

Enemy_AKT_sum=calculate01()
print("平均攻击力为：%d"%(Enemy_AKT_sum/len(Enemy_list)))


#删除防御力小于10的敌人
def delete01():
    global eney
    for eney in range(len(Enemy_list) - 1, -1, -1):
        if Enemy_list[eney].AC < 10:
            del Enemy_list[eney]
delete01()

for eney in  Enemy_list:
    eney.print_self_info()


# 将所有敌人攻击力增加50
def add_atk():
    global eney
    for eney in Enemy_list:
        eney.AKT += 50
add_atk()

for eney in  Enemy_list:
    eney.print_self_info()