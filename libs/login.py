"""
封装代码：使用函数，还是类？
类：
    封装
    继承
    多态
"""
import requests
from configs.config import HOST
# 封装 登录类，命名规范：首字母大写，使用驼峰法


class Login:
    # 封装--登录接口
    def login(self, body_data):
        # 1、 请求url
        url = f'{HOST}/api/login'
        # 2、请求头：可以不写
        # 3、请求体
        payload = body_data
        # 4、发送请求
        resp = requests.post(url, json=payload)
        # 5、打印响应数据
        return resp.text  # 返回响应数据--字符串类型

    def logout(self):
        pass


if __name__ == '__main__':
    test_date = {"username": "zhangsan", "lisi":"gsd"}
    # 1、使用类去创建实例
    login = Login()
    # 2、调用登录接口
    resp = login.login(test_date)

"""
分析接口特性：
    - 登录接口的密码使用了加密
        -加密方式有哪些？
            - MD5
                - 简单的md5、
                - MD5加盐、
                - MD5双重加盐
            - RSA
                
"""