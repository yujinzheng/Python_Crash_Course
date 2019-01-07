#coding=utf-8

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """用来测试Employee类的函数"""

    def setUp(self):
        self.employee = Employee("金正", "于", 120000)
        self.customRaise = 10000

    def test_give_default_raise(self):
        """测试默认加薪是否正确"""
        salary = self.employee.salary
        self.employee.give_raise()
        self.assertEqual(salary+5000, self.employee.salary)

    def test_give_custom_raise(self):
        """测试自定义的加薪是否正确"""
        salary = self.employee.salary
        self.employee.give_raise(self.customRaise)
        self.assertEqual(salary+self.customRaise, self.employee.salary)

unittest.main()