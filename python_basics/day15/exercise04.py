"""
    练习:敌人类（攻击力0--100 )
        抛出异常的信息∶消息/错误行/攻击力/错误编号

"""
class AtkError(Exception):
    def __init__(self,message,age_value,code_line,error_number):
        super().__init__("出错啦啦啦")
        self.message = message
        self.age_value = age_value
        self.code_line = code_line
        self.error_number = error_number

class Enemy:
    def __init__(self,atk):
        self.atk=atk
    @property
    def atk(self):
        return self.__ark
    @atk.setter
    def atk(self,value):
        if 0<= value <=100:
            self.__atk=value
        else:
            raise AtkError("不符合范围",value,22,1001)

# e01=Enemy(101)
try:
    e01=Enemy(101)
except AtkError as e:
    print("请重新输入")
    print(e.message)
    print(e.age_value)
    print(e.code_line)

