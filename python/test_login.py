# -*- coding: utf-8 -*-
# @Time : 2020/12/22 10:15
# @Author : zyk
# @Email : zhangyongke1105@163.com
# @File : test_login.py
# @Software: PyCharm
from selenium import webdriver
import unittest
import time
from python.public import login


class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.0.9.28:8088/admin"
        self.verificationErrors = []
        self.accept_next_alert = True

    # 用户正常登陆系统
    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        # 调用登陆函数
        login.login(self, "admin", "admin123")
        # 获取断言
        iframe = driver.find_element_by_name("iframe0")
        driver.switch_to.frame(iframe)
        time.sleep(3)
        text = driver.find_element_by_xpath("/html/body/div[1]/div").text
        self.assertEqual(text, "欢迎使用全国中小企业融资综合信用服务平台", "用户登陆失败")
        # 调用退出函数
        login.logout(self)

    # 用户名，密码为空
    def test_null(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        # 调用登陆函数
        login.login(self, '', '')
        text = driver.find_element_by_id("username-error").text
        self.assertEqual(text, u"请输入您的用户名", "用户名错误")

    # 输入用户名，密码为空
    def test_password_null(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        # 调用登陆函数
        login.login(self, "admin", "")
        text = driver.find_element_by_id("password-error").text
        self.assertEqual(text, "请输入您的密码", "密码错误")

    # 用户名为空，输入密码
    def test_user_null(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        # 调用登陆函数
        login.login(self, "", "admin123")
        text = driver.find_element_by_id("username-error").text
        self.assertEqual(text, u"请输入您的用户名", "用户名错误")

    # 用户密码错误
    # def test_error(self):
    #     driver = self.driver
    #     driver.get(self.base_url)
    #     driver.maximize_window()
    #     # 调用登陆函数
    #     login.login(self, "admin123", "admin123")
    #     text = driver.find_element_by_xpath("/html/body/div[2]").text
    #     print(text)
    #     # self.assertEqual(text, u"请输入您的用户名", "用户名错误")

    def tearDown(self) -> None:
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == '__main__':
    unittest.main()
