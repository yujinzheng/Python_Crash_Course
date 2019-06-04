#coding=utf-8

import unittest
import python_repos

class PythonReposTestCase(unittest.TestCase):
    def test_status_code(self):
        """查看返回的值是否正确"""
        self.assertEqual(python_repos.r.status_code, 200)

test = PythonReposTestCase()
test.test_status_code()