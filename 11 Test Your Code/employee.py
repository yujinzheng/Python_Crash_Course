#coding=utf-8

class Employee():
    """一个用来存储员工的类"""

    def __init__(self, ming, xing, salary):
        """初始化函数，接收名、姓和年薪"""
        self.ming = ming
        self.xing = xing
        self.salary = salary

    def give_raise(self, num = 5000):
        """增加薪水的函数，默认增加的薪水为5000"""
        self.salary += num
