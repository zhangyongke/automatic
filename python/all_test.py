# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 10:44 AM
# @Author  : zyk
# @Email   : zhangyongke1105@163.com
# @File    : all_test.py
# @Software : PyCharm
import unittest, time
import HTMLTestRunner_PY3
def createsuite():
    testunit = unittest.TestSuite()
    ##定义测试文件查找的目录
    test_dir = u'XXX路径'
    ##定义discover方法
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py',top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
    return testunit
now = time.strftime("%Y-%m-$d %H_%M_%S")

##定义报告文件存放路径
filename = '路径地址' + now + 'result.html'    ##如'E:\\workplace\\python\\result\\'
fp = open(filename, 'wb')
runner = HTMLTestRunner_PY3.HTMLTestRunner(fp, verbosity=1, title='XXX项目测试报告', description=u'用例执行情况')

if __name__=='__main__':
    alltestnames = createsuite()
    runner.run(alltestnames)
    fp.close()