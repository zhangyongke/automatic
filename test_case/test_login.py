# -*- coding: utf-8 -*-
# @Time      ：2022/10/22  23:30
# @Author    ：zhangyongke
# @Email     :zhangyongke1105@163.com 
# @File      ：test_login.PY
# @Software  ：PyCharm
"""
测试用例获取
登录接口发送请求
"""

from libs.login import Login
from libs.handle_excel import get_excel_data
import pytest


# 测试类
class TestLogin:
    # 测试方法--接口
    # 数据渠道
    @pytest.mark.parametrize('req_body,exp_data', get_excel_data('../data/exam.xls', '登录模块', 'login')) # 引用pytest框架
    def test_login(self, req_body, exp_data):
        res = Login().login(req_body)
        assert res['message'] == exp_data['message']


if __name__ == '__main__':
    pytest.main([__file__, '-s'])  # __file__表示当前的文件名


"""
测试反馈：
    - 列下标是写死的，如果需要获取其他列，怎么办？--直接改代码
    - 单元格数据不一定是Json格式，有些不能转字典
    - 不能获取其他多列数据
"""
