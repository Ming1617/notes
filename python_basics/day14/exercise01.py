"""
    10:50 上课
    定义员工管理器
        1.管理所有员工
        2. 计算所有员工工资

    员工：
        程序员：底薪 + 项目分红
        销售：底薪 + 销售额 * 0.05
        软件测试...
        ...

    要求：增加新岗位，员工管理器不变.
"""


class EmployeeManager:
    def __init__(self):
        self.__employees = []

    def add_employee(self, emp):
        self.__employees.append(emp)

    def get_total_saraly(self):
        total_saraly = 0
        for item in self.__employees:
            # 调用是抽象的员工类
            # 执行是具体的员工(程序员/销售..)
            total_saraly += item.calculate_salary()
        return total_saraly


class Employee:
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

# ---------------------------------------
class Programmer(Employee):
    def __init__(self, base_salary, bonus):
        super().__init__(base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        # return self.base_salary + self.bonus
        # 扩展重写
        return super().calculate_salary()+ self.bonus


class Salesmen(Employee):
    def __init__(self, base_salary, sale_value):
        super().__init__(base_salary)
        self.sale_value = sale_value

    def calculate_salary(self):
        return self.base_salary + self.sale_value * 0.05


# 测试
manager = EmployeeManager()
manager.add_employee(Programmer(200000,500))
manager.add_employee(Salesmen(2000,1000))
print(manager.get_total_saraly())


