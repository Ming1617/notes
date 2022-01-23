"""
    请以面向对象的思想，描述下列场景
    小明在招商银行取钱
"""
class Person:
    def __init__(self,name,money):
        self.name=name
        self.money=money

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name=value
    @property
    def meney(self):
        return self.__meney
    @meney.setter
    def meney(self,value):
        self.__meney=value

class Bank:
    def __init__(self,name,meney):
        self.name = name
        self.meney=meney

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
    def meney(self,value):
        self.__meney=value

    def draw_money(self,person,value):
        """
            取钱
        :param person:
        :param value:
        :return:
        """
        self.meney-=value
        person.money+=value
        print(person.name+"取了%d"%value)

xm=Person("小明",0)
gs=Bank("工商银行",10000)
gs.draw_money(xm,1000)