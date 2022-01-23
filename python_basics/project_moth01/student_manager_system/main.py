"""
    项目入口

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
from ui import *
if __name__=="__main__":
    View=StudentManagerView()
    View.main()

