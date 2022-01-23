class Person:
    def say(self):
        print("说话")

class Student(Person):
    def study(self):
        print("学习")
class Teacher(Person):
    def teach(self):
        print("讲课")
#子类独享可以调用子类成员，也可以调用父类成员
s01=Student()
s01.study()
s01.say() #父类成员

p01=Person()
#父类对象只可以调用父类成员，不能调用子类成员
p01.say()

t01=Teacher()

# pythn 内置函数
# 1.判断对象是否属于一个类型
#"老师对象”是一个老师类型
print(isinstance(t01,Teacher))#True
#"老师对象”不是一个学生类型
print(isinstance(t01,Student))#Flase
#"老师对象”是一个人类型
print(isinstance(t01,Person))#True

#2.判断一个类型是否属于另一个类型
#"老师类型"不是一个学生类型
print(issubclass(Teacher,Student))#Flase
#"老师类型”是一个人类型
print(issubclass (Teacher,Person))#True
#"人类型”是一个老师类型
print ( issubclass ( Person, Teacher) )# True
