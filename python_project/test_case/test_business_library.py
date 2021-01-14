# coding=utf-8
# @Time : 2020/12/28 15:29
# @Author : zyk
# @Email : zhangyongke1105@163.com
# @File : test_business_library.py
# @Software: PyCharm
from selenium import webdriver
import unittest
from python_project.test_case.public import login, public_module, check_data, file_read
import time


class TestBusinessLibrary(unittest.TestCase):
    """测试中小企业共享库"""
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.base_url = "http://10.0.9.28:8088/admin"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_company_name(self):
        """企业名称字段查询功能验证"""
        driver = self.driver
        driver.get(self.base_url)
        try:
            sheet = file_read.open_fie("F:\\workplace\\GitWork\\python_project\\test_data\\查询条件.xlsx", "中小企业共享库")
            user_info = sheet.cell(4, 3).value
            username, password = user_info.split("，")
            # 调用登陆函数进行登陆
            login.login(self, username, password)
            # 打开企业档案模块
            public_module.open_business_library(self)
            # 获取测试数据
            for i in range(6, 10):
                enterprise_name = str(sheet.cell(i, 3).value).rstrip()
                if enterprise_name == "null" or enterprise_name == "None":
                    enterprise_name = ""
                driver.find_element_by_name("qymc").clear()
                driver.find_element_by_name("qymc").send_keys(enterprise_name)
                # time.sleep(2)
                driver.find_element_by_link_text(u"搜索").click()
                time.sleep(2)
                check_data.check_date(self)
                time.sleep(2)
            # 调用退出函数
            login.logout(self)

        except Exception as e:
            print(e)
            raise Exception

    def test_credit_code(self):
        """统一社会信用代码字段查询功能验证"""
        driver = self.driver
        driver.get(self.base_url)
        try:
            sheet = file_read.open_fie("F:\\workplace\\GitWork\\python_project\\test_data\\查询条件.xlsx", "中小企业共享库")
            user_info = sheet.cell(4, 3).value
            username, password = user_info.split("，")
            # 调用登陆函数进行登陆
            login.login(self, username, password)
            # 打开企业档案功能
            public_module.open_business_library(self)
            # 获取测试数据
            for i in range(10, 14):
                credit_code = str(sheet.cell(i, 3).value).rstrip()
                if credit_code == "null" or credit_code == "None":
                    credit_code = ""
                driver.find_element_by_name("tyshxydm").clear()
                driver.find_element_by_name("tyshxydm").send_keys(credit_code)
                # time.sleep(2)
                driver.find_element_by_link_text(u"搜索").click()
                time.sleep(2)
                check_data.check_date(self)
                time.sleep(2)
            # 调用退出函数
            login.logout(self)

        except Exception as e:
            print(e)
            raise Exception

    def tearDown(self) -> None:
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == '__main__':
    unittest.main()
