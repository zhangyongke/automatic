# -*- coding: utf-8 -*-
# @Time : 2020/11/11 18:03
# @Author : zyk
# @Email : zhangyongke1105@163.com
# @File : 接口请求测试.py
# @Software: PyCharm


import requests
import json
base_url = "http://10.0.9.28:8088/client"
tokenurl = "/api/getToken"      # 请求token的地址
# 请求报文加密
encrypturl = "http://10.0.252.220:8800/getRequestParam"    # 加密请求地址
headers = {"Content-Type": "application/json; charset=UTF-8"}
data = {"appId": "831e85e26740492ca73819cd9a3591e5",
        "appKey": "shanghaishi",
        "appSecret": "831e85e26740492ca73819cd9a3591e51604892182069"
        }
encrytres = requests.post(url=encrypturl, data=json.dumps(data), headers=headers)
print(encrytres.text)

# 请求获取token
url = base_url + tokenurl
headers = {"Content-Type": "application/json; charset=UTF-8"}
gettokenres = requests.post(url=url, data=encrytres.text, headers=headers)
print(gettokenres.text)

# 解密请求地址
decrypturl = "http://10.0.252.220:8800/getDecryptData"  # 解密url
headers = {"Content-Type": "application/json; charset=UTF-8"}
decryptres = requests.post(url=decrypturl, data=gettokenres.text, headers=headers)
print(decryptres.text)
