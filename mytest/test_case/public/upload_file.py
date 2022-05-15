#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/1/9 15:28
# @Author  : ZYK
# @Email   : zhangyongke1105@163.com
# @File    : upload_file.py
# @Software: PyCharm
import time
import pywinauto
from pywinauto.keyboard import send_keys


def upload_file(file_path, filename):
    # 调用外部库，实现上传文件操作，file_path:需要上传的文件路径， filename：上传的文件名称
    app = pywinauto.Desktop()  # 使用pywinauto来选择文件
    dlg = app["打开"]  # 选择文件上传的窗口
    dlg["Toolbar3"].click()  # 选择文件地址输入框
    time.sleep(2)
    send_keys(file_path)
    send_keys("{VK_RETURN}")  # 键盘输入回车，打开该路径
    time.sleep(1)
    dlg["文件名(&N):Edit"].type_keys(filename)  # 选中文件名输入框，输入文件名
    time.sleep(2)
    dlg["打开(&O)"].click()  # 点击打开
    time.sleep(1)

