# coding=utf-8
# @Time    : 2020/3/8 10:44 AM
# @Author  : zyk
# @Email   : zhangyongke1105@163.com
# @File    : all_test.py
# @Software : PyCharm
import unittest
import time
from BeautifulReport import BeautifulReport


def create_suite():
    test_unit = unittest.TestSuite()
    # 定义测试文件查找的目录
    test_dir = "F:\\workplace\\GitWork\\python_project\\test_case"  # 各个测试文件存放路径
    # 定义discover方法，查找需要执行测试的文件
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py', top_level_dir=None)
    for test_case in discover:
        test_unit.addTests(test_case)
    return test_unit


# 使用beautiful_report形式输入report报告
now = time.strftime("%Y-%m-%d %H_%M_%S")
# 运行所有的测试用例，
all_test_names = create_suite()
runner = BeautifulReport(all_test_names)
report_dir = 'F:\\workplace\\GitWork\\python_project\\Report\\'

if __name__ == '__main__':
    runner.report(u"基础平台功能验证", now+"_BeautifulReport", report_dir=report_dir)


# # 使用HTMLTestReport报告
# now = time.strftime("%Y-%m-%d %H_%M_%S")
# # 定义报告文件存放路径
# filepath = 'F:\\workplace\\GitWork\\Report\\'
# filename = filepath + now + 'result.html'
# fp = open(filename, 'wb')
# runner = HTMLTestRunner(stream=fp, title='XXX项目测试报告', description=u'用例执行情况')
#
# if __name__ == '__main__':
#     all_test_names = create_suite()
#     runner.run(all_test_names)
#     fp.close()
