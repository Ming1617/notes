"""
3．请用面向对象思想﹐描逑以下场景∶
张无忌 教 赵敏 九阳神功
赵敏 教 张无忌 化妆
张无忌 上班 挣了 10000
赵敏 上班 挣了 6000
思考∶变化点是数据的不同还是行为的不同。

"""
class Person:
    def __init__(self,name,meney,gong):
        self.name=name
        self.meney=meney
        self.gong=gong

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def meney(self):
        return self.__meney

    @meney.setter
    def meney(self, value):
        self.__meney = value

    @property
    def gong(self):
        return self.__gong

    @gong.setter
    def gong(self, value):
        self.__gong = value


    def teach_info(self,type):
        print(self.__name,"教",type.name,self.gong)

    def be_on_duty(self,value):
        print(self.__name,"上班挣了",value)
        self.meney+=value

wj=Person("无忌",0,"九阳神功")
zm=Person("赵敏",0,"化妆")

wj.teach_info(zm)
zm.teach_info(wj)
zm.be_on_duty(5000)
wj.be_on_duty(10000)
print(wj.meney)