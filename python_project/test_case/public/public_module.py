# coding=utf-8
# @Time : 2020/12/24 17:18
# @Author : zyk
# @Email : zhangyongke1105@163.com
# @File : public_module.py
# @Software: PyCharm
import time
import os


def open_business_white_list_import(self):
    """打开企业白名单导入菜单栏"""
    driver = self.driver
    try:
        driver.find_element_by_link_text(u"企业白名单").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"企业白名单导入").click()
        time.sleep(2)
        iframe = driver.find_element_by_name("iframe1")
        driver.switch_to.frame(iframe)
        time.sleep(2)
    except Exception as e:
        print(e)


def open_xyd_work(self):
    """打开信易贷工作情况菜单栏"""
    driver = self.driver
    try:
        driver.find_element_by_link_text(u"企业白名单").click()
        time.sleep(1)
        driver.find_element_by_link_text(u'“信易贷”工作情况').click()
        time.sleep(2)
    except Exception as e:
        print(e)


def export_work(self):
    """导出功能"""
    driver = self.driver
    driver.find_element_by_link_text(u"导出").click()
    # 点击确认按钮进行导出
    driver.find_element_by_link_text(u"确认").click()
    time.sleep(3)
    # 文件校验,没有设置chrome配置的时候。调用，默认使用下载路劲，C:\user\用户名
    # path = os.path.expanduser('~') + "\\Downloads"
    path = "G:\\Download"
    file_list = []
    for filename in os.listdir(path):
        if filename.endswith(".xlsx"):
            fullname = path + "\\" + filename
            # print(fullname)
            file_list.append((fullname, os.path.getctime(fullname)))
    newest_file = file_list[0]
    # print("newest_file", newest_file)
    # print(len(newest_file))
    for i in range(len(newest_file)):
        if i < (len(file_list)-1) and newest_file[1] < file_list[i+1][1]:
            newest_file = file_list[i+1]
        else:
            continue
    print("最新下载的文件为：", newest_file[0])
    driver.switch_to.parent_frame()
