# -*- coding: utf-8 -*-
# @Time : 2020/11/25 18:01
# @Author : zyk
# @Email : zhangyongke1105@163.com
# @File : 手机app端测试.py
# @Software: PyCharm
from appium import webdriver
import time


def get_size():
    # 获取窗口尺寸
    size = driver.get_window_size()
    x = size['width']
    y = size['height']
    return x, y


def swipe_up():
    # 向上滑动
    size = get_size()
    x1 = int(size[0]*0.5)
    y1 = int(size[1]*0.9)
    y2 = int(size[1]*0.1)
    driver.swipe(x1, y1, x1, y2, 500)


def swipe_down():
    # 向下滑动
    size = get_size()
    x1 = int(size[0]*0.9)
    y1 = int(size[0]*0.1)
    y2 = int(size[0]*0.5)
    driver.swipe(x1, y1, x1, y2, 500)


def swipe_left():
    # 向左滑动
    size = get_size()
    x1 = int(size[0]*0.9)
    x2 = int(size[0]*0.1)
    y1 = int(size[1]*0.5)
    driver.swipe(x1, y1, x2, y1, 500)


def swipe_right():
    # 向右滑动
    size = get_size()
    x1 = int(size[0]*0.1)
    x2 = int(size[0]*0.9)
    y1 = int(size[1]*0.5)
    driver.swipe(x1, y1, x2, y1, 500)

# 初始化信息


desired_caps = {}
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "7.1.2"
desired_caps["deviceName"] = "127.0.0.1:62001"
desired_caps["appPackage"] = "com.ss.android.ugc.aweme.lite"
desired_caps["appActivity"] = "com.ss.android.ugc.aweme.splash.SplashActivity"
# 不需要再次签名
desired_caps['noSign'] = 'True'
# 不需要清理数据，避免重新安装的问题
desired_caps['noReset'] = 'True'

# 打开抖音极速版
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.implicitly_wait(30)

while True:
    now_time = time.strftime("%H_%M")
    print(now_time)
    swipe_up()    # 滑动向上
    time.sleep(20)
    if now_time == '17_07':
        print("时间到！程序退出")
        break
