#类
class Wife:
    #数据成员
    def __init__(self,name,sex):
        #self是调用当前方法的对象地址
        self.name=name
        self.sex=sex
    #行为成员
    def play(self):
        """
            一起玩耍
        :return:
        """
        print(self.name+"玩耍")


#创建对象，实际在调用__init__方法
w=Wife("莉莉","女")#自动将对象地址传入方法
#调用对象的行为
w.play()#自动将对象地址传入方法
