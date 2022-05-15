# coding=utf-8
# @Time : 2020/12/22 18:18
# @Author : zyk
# @Email : zhangyongke1105@163.com
# @File : test_business_white_list.py
# @Software: PyCharm
from selenium import webdriver
import unittest
from framwork_study.selenium.test_case.public import public_module, check_data, file_read
from framwork_study.selenium.test_case.public import login
import time


class TestBusinessWhiteList(unittest.TestCase):
    """测试企业白名单模块的各个功能"""
    def setUp(self) -> None:
        # 创建Chrome浏览器配置对象
        chrome_options = webdriver.ChromeOptions()
        # 设定下载文件的保存目录为G盘的G:\downloadFile；如果该目录不存在则直接创建
        prefs = {"download.default_directory": "G:\\Download"}
        # 将自定义设置添加到chrome配置对象实例中
        chrome_options.add_experimental_option("prefs", prefs)
        # 启动带有自动义设置的Chrome浏览器
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        # self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.base_url = "http://10.0.9.28:8088/admin"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_batches_search(self):
        """批次条件查询功能验证"""
        driver = self.driver
        driver.get(self.base_url)
        try:
            sheet = file_read.open_fie("F:\\workplace\\GitWork\\python_project\\test_data\\查询条件.xlsx", "企业白名单")
            user_info = sheet.cell(4, 3).value
            username, password = user_info.split("，")
            # 调用登陆函数进行登陆
            login.login(self, username, password)
            # 打开菜单选项
            public_module.open_business_white_list_import(self)
            # 获取测试数据
            for i in range(6, 10):
                batch = str(sheet.cell(i, 3).value).rstrip()
                if batch == "null" or batch == "None":
                    batch = ""
                try:
                    # 进行条件检索
                    driver.find_element_by_name("batch").clear()
                    driver.find_element_by_name("batch").send_keys(batch)
                    driver.find_element_by_link_text(u"搜索").click()
                    time.sleep(2)
                    check_data.check_date(self)
                    time.sleep(2)
                except Exception as e:
                    print(e)
            login.logout(self)
        except Exception as e:
            print(e)
            raise Exception

    def test_company_name(self):
        """企业名称字段查询功能验证"""
        driver = self.driver
        driver.get(self.base_url)
        try:
            sheet = file_read.open_fie("F:\\workplace\\GitWork\\python_project\\test_data\\查询条件.xlsx", "企业白名单")
            user_info = sheet.cell(4, 3).value
            username, password = user_info.split("，")
            # 调用登陆函数进行登陆
            login.login(self, username, password)
            # 打开企业白名单导入功能
            public_module.open_business_white_list_import(self)
            # 获取测试数据
            for i in range(10, 14):
                enterprise_name = str(sheet.cell(i, 3).value).rstrip()
                if enterprise_name == "null" or enterprise_name == "None":
                    enterprise_name = ""
                driver.find_element_by_name("enterpriseName").clear()
                driver.find_element_by_name("enterpriseName").send_keys(enterprise_name)
                # time.sleep(2)
                driver.find_element_by_link_text(u"搜索").click()
                time.sleep(2)
                check_data.check_date(self)
                time.sleep(2)
            # 调用退出函数
            login.logout(self)

        except Exception as e:
            print(e)
            raise Exception

    def test_credit_code(self):
        """统一社会信用代码字段查询功能验证"""
        driver = self.driver
        driver.get(self.base_url)
        try:
            sheet = file_read.open_fie("F:\\workplace\\GitWork\\python_project\\test_data\\查询条件.xlsx", "企业白名单")
            user_info = sheet.cell(4, 3).value
            username, password = user_info.split("，")
            # 调用登陆函数进行登陆
            login.login(self, username, password)
            # 打开企业白名单导入功能
            public_module.open_business_white_list_import(self)
            # 获取测试数据
            for i in range(14, 18):
                credit_code = str(sheet.cell(i, 3).value).rstrip()
                if credit_code == "null" or credit_code == "None":
                    credit_code = ""
                driver.find_element_by_name("uniscId").clear()
                driver.find_element_by_name("uniscId").send_keys(credit_code)
                # time.sleep(2)
                driver.find_element_by_link_text(u"搜索").click()
                time.sleep(2)
                check_data.check_date(self)
                time.sleep(2)
            # 调用退出函数
            login.logout(self)

        except Exception as e:
            print(e)
            raise Exception

    def test_export_function(self):
        """导出功能验证"""
        driver = self.driver
        driver.get(self.base_url)
        try:
            sheet = file_read.open_fie("F:\\workplace\\GitWork\\python_project\\test_data\\查询条件.xlsx", "企业白名单")
            user_info = sheet.cell(4, 3).value
            username, password = user_info.split("，")
            # 调用登陆函数进行登陆
            login.login(self, username, password)
            # 打开企业白名单导入功能
            public_module.open_business_white_list_import(self)
            # 进行数据导出
            public_module.export_work(self)
            # time.sleep(3)
            # 调用退出函数
            login.logout(self)

        except Exception as e:
            print(e)
            raise Exception

    def tearDown(self) -> None:
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == '__main__':
    unittest.main()
