# -*- coding: utf-8 -*-
# @Time : 2020/12/22 10:15
# @Author : zyk
# @Email : zhangyongke1105@163.com
# @File : test_login.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
from framwork_study.selenium.test_case.public import login
from framwork_study.selenium.test_case.public import file_read


class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.0.9.28:8088/admin"
        self.verificationErrors = []
        self.accept_next_alert = True

    # 验证用户正常登陆系统
    def test_login(self):
        """用户输入正确的用户名和密码，可正常登陆"""
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        # 调用登陆函数
        login.login(self, "admin", "admin123")
        # 获取断言
        # iframe = driver.find_element_by_name("iframe0")
        iframe = driver.find_element(By.name, 'iframe0')
        driver.switch_to.frame(iframe)
        time.sleep(3)
        # text = driver.find_element_by_xpath("/html/body/div[1]/div").text
        text = driver.find_element(By.xpath, "/html/body/div[1]/div").text
        self.assertEqual(text, "欢迎使用全国中小企业融资综合信用服务平台", "用户登陆失败")
        # 调用退出函数
        login.logout(self)

    # 验证用户名，密码为空
    def test_null(self):
        """用户名和密码输入为空，用户登陆失败，系统进行提示。"""
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        username = file_read.user_info(4)[0]
        password = file_read.user_info(4)[1]
        # 调用登陆函数
        login.login(self, username, password)
        text = driver.find_element_by_id("username-error").text
        self.assertEqual(text, u"请输入您的用户名", "用户名错误")

    # 验证输入用户名，密码为空
    def test_password_null(self):
        """输入正确的用户名，密码输入为空，用户登陆失败，系统进行提示。"""
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        username = file_read.user_info(5)[0]
        password = file_read.user_info(5)[1]
        # 调用登陆函数
        login.login(self, username, password)
        text = driver.find_element_by_id("password-error").text
        self.assertEqual(text, "请输入您的密码", "密码错误")
        # 测试跳过用例数据，使用self.skipTest()跳过测试用例的执行
        # self.skipTest(u"测试跳过该测试用例")

    # 验证用户名为空，输入密码
    def test_user_null(self):
        """用户名输入为空，密码输入正确，用户登陆失败，系统进行提示。"""
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        username = file_read.user_info(6)[0]
        password = file_read.user_info(6)[1]
        # 调用登陆函数
        login.login(self, username, password)
        text = driver.find_element_by_id("username-error").text
        self.assertEqual(text, u"请输入您的用户名", "用户名错误")

    # 验证用户密码错误
    def test_error(self):
        """验证用户名和密码输入错误，登陆失败，系统进行提示"""
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        username = file_read.user_info(7)[0]
        password = file_read.user_info(7)[1]
        # 调用登陆函数
        login.login(self, username, password)
        text = driver.find_element_by_xpath("/html/body/div[2]/div").text
        self.assertEqual(text, u"用户不存在/密码错误", "用户名或密码错误")

    def tearDown(self) -> None:
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == '__main__':
    unittest.main()
