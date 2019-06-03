#coding=utf-8

import unittest
from btc_close_2017 import draw_line
import pygal

class BtcCloseTestCase(unittest.TestCase):
    """用来测试draw_line函数的单元测试类"""

    def test_draw_line_xequip(self):
        """能够正确处理x_data的数据相等的情况"""
        x_data = [1, 1, 1, 1, 1, 1, 1]
        y_data = [1, 2, 3, 4, 5, 6, 7]
        title = "Test"
        y_legend = "haha"
        test_case = draw_line(x_data, y_data, title, y_legend)
        self.assertEqual(type(test_case), type(pygal.Line()))

my_case = BtcCloseTestCase()
my_case.test_draw_line_xequip()