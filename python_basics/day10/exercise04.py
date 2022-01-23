"""
    练习∶定义对象计数器。
    定义老婆类﹐创建3个老婆对象。
    可以通过类变量记录老婆对象个数﹐
    可以通过类方法打印老婆对象个数。
"""
class Wife:

    Wife_count=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Wife.Wife_count+=1
    @classmethod
    def print_Wife_info(cls):
        print("老婆一共有："+str(Wife.Wife_count)+"个")

w01=Wife("张三",18)
w02=Wife("李四",19)
w03=Wife("王二",20)

Wife.print_Wife_info()
