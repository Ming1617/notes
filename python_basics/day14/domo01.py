"""
    内置可重写函数
    练习:exercise01.py
"""
class StudentModel:
    def __init__(self,name="",age=0,score=0,id=0):
        self.name=name
        self.age=age
        self.score=score
        self.id=id

    def __str__(self):
        return "我叫%s,编号是%d,年龄是%d,成绩是:%d"%(self.name,self.id,self.age,self.score)

    def __repr__(self):
        return "StudentModel('%s',%d,%d,%d)"%(self.name,self.age,self.score,self.id)

s01=StudentModel("无忌",20,80,1001)
print(s01)
print(str(s01))
print(repr(s01))

print(eval("1+1"))
s02=eval(repr(s01))
print(s02.name)