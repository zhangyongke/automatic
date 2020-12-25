# -*- coding: utf-8 -*-
# @Time : 2020/12/22 13:50
# @Author : zyk
# @Email : zhangyongke1105@163.com
# @File : check_data.py
# @Software: PyCharm
# 查询记录结果校验
import time


def check_date(self):
    driver = self.driver
    try:
        menu_table = driver.find_element_by_xpath("//*[@id='bootstrap-table']/tbody")
    except Exception as f:
        print(f)
    else:
        rows = menu_table.find_elements_by_tag_name('tr')
        # 获取第一页的条数
        result = len(rows)
        text = driver.find_element_by_xpath("//*[@id='bootstrap-table']/tbody/tr/td").text
        if result == 1 and text == "没有找到匹配的记录":
            print("查询记录结果为空")
        else:
            print(u"当前页记录条数为：%d" % result)
        time.sleep(2)
