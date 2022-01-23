"""
    学生管理系统
    项目计划：
            1.完成数据模型StudentModel
            2.创建逻辑控制类StudentManagerController
            3.完成数据：学生列表 __stu_list
            4.行为：获取列表 stu_list，
            5.添加学生方法 add_student
            6.根据编号删除学生remove_student，
            7.根据编号修改学生信息update_student
            8.在界面视图类中,根据编号删除学生.

"""
class StudentModel:
    """
        学生信息模型
    """
    def __init__(self,name="",age=0,score=0,id=0):
        """
            创建学生对象
        :param name:姓名，str类型
        :param age:年龄，int类型
        :param score:成绩，float类型
        :param id: 编号（该学生对象的唯一标识）
        """
        self.name=name
        self.age=age
        self.score=score
        self.id = id

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,value):
        self.__id=value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        # print("name:",value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        if value >=0 and value< 100:
            self.__age = value
        else:
            raise ValueError("年龄不合格")

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if value>=0 and value<=150:
            self.__score = value
        else:
            raise  ValueError("成绩输入错误")

class StudentManagerController:
    """
        学生管理控制器，负责业务逻辑处理
    """
    # 类变量，表示初始编号。
    __init_id=1000
    def __init__(self):
        self.__stu_list=[]
    # def get_stu_list(self):
    #     return self.__stu_list
    @property
    def stu_list(self):
        """
            学生列表
        :return: 存储学生对象的列表
        """
        return self.__stu_list

    def add_student(self,stu_info):
        """
            添加一个新学生
        :param stu_info: 没有编号的学生信息
        """
        stu_info.id=self.__generate_id()
        self.__stu_list.append(stu_info)

    def __generate_id(self):
        """
            生产一个唯一编号id
        :return: 编号id
        """
        StudentManagerController.__init_id += 1
        return StudentManagerController.__init_id

    def remove_student(self,id):
        """
            根据编号移除学生信息
        :param id: 编号
        :return:
        """
        for item in self.__stu_list:
            if item.id==id:
                self.__stu_list.remove(item)
                return True# 表示移除成功
        return  False# 表示移除失败

    def update_student(self,stu_info):
        """
            更新学生信息
        :param stu_info: 传入的修改的学生对象
        :return: True/False
        """
        #根据str_info_id修改其他信息
        for item in self.__stu_list:
            if item.id == stu_info.id:
                item.name=stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True
        return False

    def order_by_score(self,list_stu):
        """
            按照升序排序学生信息
        :param list_stu: 传入排序列表
        :return: 排序后列表
        """
        list_order_by_score=list_stu[::] #切片生成新列表
        for item in range(len(list_order_by_score)):
            for jtem in range(item+1,len(list_order_by_score)):
                if list_order_by_score[item].score > list_order_by_score[jtem].score:
                    temp=list_order_by_score[item]
                    list_order_by_score[item]=list_order_by_score[jtem]
                    list_order_by_score[jtem]=temp
        return list_order_by_score

"""
    测试添加学生功能
manager=StudentManagerController()
s01=StudentModel("ZS",24,100,0)
manager.add_student(s01)
for item in manager.stu_list:
    print(item.name)
"""

"""
#测试删除学生
manager=StudentManagerController()
manager.add_student(StudentModel("zs"))
manager.add_student(StudentModel("ls"))
for item in manager.stu_list:
    print(item.id)
print(manager.remove_student(1001))
for item in manager.stu_list:
    print(item.id)
"""

"""
#测试删除学生
manager=StudentManagerController()
manager.add_student(StudentModel("zs",20,30))
manager.add_student(StudentModel("ls"))
for item in manager.stu_list:
    print(item.id,item.name,item.age,item.score)
print(manager.update_student(StudentModel("cc",20,90,1001)))
print("修改后...")
for item in manager.stu_list:
    print(item.id,item.name,item.age,item.score)
"""

"""
 # 测试排序学生功能
manager=StudentManagerController()
s01=StudentModel("ZS",24,90,0)
s02=StudentModel("Zz",24,100,0)
s03=StudentModel("Zi",24,80,0)
manager.add_student(s01)
manager.add_student(s02)
manager.add_student(s03)
list_order_by_score=manager.order_by_score(manager.stu_list)
for item in list_order_by_score:
    print(item.name,item.score)
for item in manager.stu_list:
    print(item.name,item.score)
"""


class StudentManagerView:
    """
        学生管理器视图
    """
    def __init__(self):
        self.__manager=StudentManagerController()
    def __display_menu(self):
        print("1）添加学生")
        print("2）显示学生")
        print("3）删除学生")
        print("4）修改学生")
        print("5）按照成绩升序显示学生")

    def __select_menu(self):
        item=input("请输入：")
        if item == "1":
            self.__input_student()
        elif item=="2":
            self.__output_students(self.__manager.stu_list)
        elif item=="3":
            self.__delete_student()
        elif item=="4":
            self.__modify_student()
        elif item=="5":
            self.__output_student_by_score(self.__manager.stu_list)

    def main(self):
        """
            界面视图入口
        :return:
        """
        while True:
            self.__display_menu()
            self.__select_menu()
    def __input_student(self):
        """
            添加学生
        :return:
        """
        name=input("请输入姓名:")
        age = int(input("请输入年龄:"))
        score = float(input("请输入成绩:"))
        stu=StudentModel(name,age,score)
        self.__manager.add_student(stu)

    def __output_students(self,list_output):
        """
            打印学生信息
        :param list_output:
        :return:
        """
        for item in list_output:
            print(item.id,item.name,item.age,item.score)

    def __delete_student(self):
        """
            删除学生信息
        :return:
        """
        id=int(input("请输入删除学生的编号："))
        if self.__manager.remove_student(id):
            print("删除成功")
        else:
            print("删除失败")
    def __modify_student(self):
        """
            修改学生信息
        :return:
        """
        id=int(input("请输入需要修改的编号："))
        name = input("请输入新的学生姓名:")
        age = int(input("请输入新的学生年龄:"))
        score = float(input("请输入新的学生成绩:"))
        stu = StudentModel(name, age, score,id)
        if self.__manager.update_student(stu) :
            print("修改成功")
        else:
            print("修改失败")
    def __output_student_by_score(self,list_output):
        """
            按照成绩升序显示学生
        :param list_output: 原始列表
        """
        self.__output_students(self.__manager.order_by_score(list_output))

View=StudentManagerView()
View.main()




