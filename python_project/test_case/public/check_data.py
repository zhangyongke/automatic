# -*- coding: utf-8 -*-
# @Time : 2020/12/22 13:50
# @Author : zyk
# @Email : zhangyongke1105@163.com
# @File : check_data.py
# @Software: PyCharm
# 查询记录结果校验
import time


def check_date(self, data):
    driver = self.driver
    try:
        menu_table = driver.find_element_by_xpath("//*[@id='bootstrap-table']/tbody")
    except Exception as f:
        print(f)
    else:
        rows = menu_table.find_elements_by_tag_name('tr')
        result = len(rows)
        text = driver.find_element_by_xpath("//*[@id='bootstrap-table']/tbody/tr/td").text
        if result == 1 and text == "没有找到匹配的记录":
            print("查询记录结果为空")
        else:
            # 模糊查询，判断输入的查询条件，是否在查询结果列表中。
            name = driver.find_element_by_xpath("//*[@id='bootstrap-table']/tbody/tr/td[1]").text
            if data in name:
                print(u"条件在查询结果列表中！！")
            print(u"当前查询记录为：%d" % result)
        # driver.switch_to.parent_frame()
        time.sleep(3)
