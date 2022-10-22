# -*- coding: utf-8 -*-
# @Time      ：2022/10/22  22:04
# @Author    ：zhangyongke
# @Email     :zhangyongke1105@163.com 
# @File      ：handle_excel.PY
# @Software  ：PyCharm
import xlrd
"""
功能需求：获取excel文件指定数据
入参：
    - 文件路径（路径+文件名+文件格式）
    - 读取指定的sheet页
    - 读取指定的单元格
        
出参： 函数使用者需要什么类型！
    - 返回数据是什么
        - 请求体 body
        - 预期响应结果
        - 描述
    - 返回数据的类型
        - 元组
        - 字典
        - 列表
        - 字符串
        - 集合
"""
# libs文件夹和data文件夹同级，所以要取data下数据的时候，可以使用../data。其中..表示返回当前目录的上一层目录


def get_excel_data(file_path, sheet_name, case_name):
    res_list = []  # 存放获取单元格的数据
    # 1.文件在磁盘---读取到--内存
    # formatting_info = True----保持文件格式原样式(如底色，json格式等)
    work_book = xlrd.open_workbook(file_path, formatting_info=True)
    # 获取所有的sheet页
    # print(work_book.sheet_names())
    # 2.选择对应的sheet
    work_sheet = work_book.sheet_by_name(sheet_name)  # 对应的sheet页对象

    # 获取一行数据
    # print(work_sheet.row_values(0))
    # 获取一列数据
    # print(work_sheet.col_values(0))

    # 单元格数据
    # print(work_sheet.cell(1,6).value)

    # 获取需要的数据
    row_index = 1  # 初始行编号
    for one in work_sheet.col_values(0):
        if case_name in one:  # login in login001,通过指定用例名称进行过滤数据
            # 请求体
            req_body = work_sheet.cell(row_index, 6).value  # cell(行编号，列编号)
            exp_data = work_sheet.cell(row_index, 8).value
            # [(req_body1,exp_data1),(req_body2,exp_data2)]
            res_list.append((req_body, exp_data))
            row_index += 1
    return res_list  # 返回列表里面包含元组


if __name__ == '__main__':
    res = get_excel_data('../data/exam.xls', '登录模块', 'login')
    print(res)
