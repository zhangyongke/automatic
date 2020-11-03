# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 10:39 PM
# @Author  : zyk
# @Email   : zhangyongke1105@163.com
# @File    : test.py
# @Software : PyCharm
from selenium import webdriver


def greet_user(username):
    print("Hello, " + username.title() + "!")


greet_user('jess')
