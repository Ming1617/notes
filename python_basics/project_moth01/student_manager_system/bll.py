"""
    控制逻辑
"""
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