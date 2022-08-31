#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/1/9 15:30
# @Author  : ZYK
# @Email   : zhangyongke1105@163.com
# @File    : create_phone.py
# @Software: PyCharm
import random
import datetime
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = "F:\\WorkPlace\\python_project\\files\\"
DC_PATH = BASE_DIR + "districtcode.txt"


def create_phone():
    """随机生成手机号码1"""
    pre_list = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152", "153",
                "155", "156", "157", "158", "159", "176", "177", "182", "186", "187", "188", "189"]
    return random.choice(pre_list)+"".join(random.choice("0123456789") for i in range(8))


# 随机生成身份证号
def get_district_code():
    with open(DC_PATH) as file:
        data = file.read()
        district_list = data.split('\n')
    for node in district_list:
        if node[10:11] != ' ':
            state = node[10:].strip()
        if node[10:11] == ' ' and node[12:13] != ' ':
            city = node[12:].strip()
        if node[10:11] == ' ' and node[12:13] == ' ':
            district = node[14:].strip()
            code = node[0:6]
            code_list.append({"state": state, "city": city, "district": district, "code": code})


def generator():
    global code_list
    code_list = []
    if not code_list:
        get_district_code()
    id = code_list[random.randint(0, len(code_list))]['code']  # 地区项
    id = id + str(random.randint(1930, 2013))  # 年份项
    da = datetime.date.today()+datetime.timedelta(days=random.randint(1, 366))  # 月份和日期项
    id = id + da.strftime('%m%d')
    id = id + str(random.randint(100, 300))  # 顺序号简单处理
    # i = 0
    count = 0
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2] # 权重项
    check_code = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5', '9':'3','10':'2'} #校验码映射
    for i in range(0, len(id)):
        count = count + int(id[i])*weight[i]
        id = id + check_code[str(count % 11)]  # 算出校验码
        return id


# print(create_phone())
# print(generator())