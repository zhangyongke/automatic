# -*- coding: utf-8 -*-
# @Time : 2020/12/22 10:59
# @Author : zyk
# @Email : zhangyongke1105@163.com
# @File : login.py
# @Software: PyCharm
import time


def login(self, username, password):
    driver = self.driver
    try:
        driver.find_element_by_name("username").clear()
    except BaseException as e:
        print(e)
    else:
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_id("btnSubmit").click()
        time.sleep(2)


def logout(self):
    driver = self.driver
    driver.switch_to.parent_frame()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='page-wrapper']/div[1]/nav/ul/li[2]/a/span").click()
    driver.find_element_by_link_text(u"退出登录").click()
