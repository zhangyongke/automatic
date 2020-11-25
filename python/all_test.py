# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 10:44 AM
# @Author  : zyk
# @Email   : zhangyongke1105@163.com
# @File    : all_test.py
# @Software : PyCharm
import unittest
import time
from HTMLTestRunner import HTMLTestRunner


def create_suite():
    test_unit = unittest.TestSuite()
    # 定义测试文件查找的目录
    test_dir = "F:\\workplace\\GitWork\\python"     # 各个测试文件存放路径
    # 定义discover方法
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            test_unit.addTests(test_case)
    return test_unit


now = time.strftime("%Y-%m-%d %H_%M_%S")

# 定义报告文件存放路径
filepath = "F:\\workplace\\GitWork\\Report\\"
filename = filepath + now + 'result.html'
fp = open(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(fp, verbosity=1, title='XXX项目测试报告', description=u'用例执行情况')

if __name__ == '__main__':
    all_test_names = create_suite()
    runner.run(all_test_names)
    fp.close()
