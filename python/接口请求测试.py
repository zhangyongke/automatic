# -*- coding: utf-8 -*-
# @Time : 2020/11/11 18:03
# @Author : zyk
# @Email : zhangyongke1105@163.com
# @File : 接口请求测试.py
# @Software: PyCharm


import requests
import json

base_url = "http://10.0.9.28:8088/client"  # 服务器请求地址
encrypt_url = "http://10.0.252.220:8800/getRequestParam"  # 加密请求地址
decrypt_url = "http://10.0.252.220:8800/getDecryptData"  # 解密请求地址

token_url = base_url + "/api/getToken"  # 请求token_url
qytb_url = base_url + "/api/upload/enterprises"  # 企业填报url
rzxqxx_url = base_url + "/api/upload/financingRequirements"  # 融资需求信息回传url
rztj_url = base_url + "/api/upload/financingStatistics"  # 融资统计回传url
jrjg_url = base_url + "/api/upload/financialInstitutions"  # 金融机构信息回传url
jrcp_url = base_url + "/api/upload/financialProducts"  # 金融产品信息回传url
zcxx_url = base_url + "/api/upload/policies"  # 政策信息回传url
xyfwjg_url = base_url + "/api/upload/creditServiceAgencies"  # 信用机构信息回传url
xycp_url = base_url + "/api/upload/creditProductStatistics"  # 信用产品信息回传url

headers = {"Content-Type": "application/json; charset=UTF-8"}


# 请求加密方法
def encrypt_data(body):
    # json.dumps()是将一个Python数据类型列表进行json格式的编码(可以理解为：将字典形式的数据转化为字符串）
    # json.loads()是将json格式数据转换为字典(可以理解为：将字符串形式的数据转化为字典)
    # json.dump()函数的使用，将json信息写进文件
    # json.load()函数的使用，将读取json信息
    encrypt_res = requests.post(url=encrypt_url, data=json.dumps(body), headers=headers)
    return encrypt_res.text


# 解密方法
def decrypt_data(body):
    decrypt_res = requests.post(url=decrypt_url, data=body, headers=headers)
    return list(eval(decrypt_res.text).values())[0]  # 可以通过eval函数转换成dict格式，获取token的值


# gettoken请求
data = {"appId": "831e85e26740492ca73819cd9a3591e5",
        "appKey": "shanghaishi",
        "appSecret": "831e85e26740492ca73819cd9a3591e51604892182069"
        }
# 请求token前先对用户信息数据加密
request_body = encrypt_data(data)

# 进行token请求
response_body = requests.post(url=token_url, data=request_body, headers=headers)

# 返回数据进行解密
token = decrypt_data(response_body)
# print(token)


# # 企业填报接口
request_data = [{
    "uniscId": "91310000695772014M",
    "enterpriseName": "上海正帆科技股份有限公司",
    "address": "上海市沈河区万柳塘路38号",
    "industry": "1",
    "province": "上海市",
    "city": "上海市",
    "area": "闵行区",
    "registeredCapital": 120,
    "businessScope": "日用塑料制品制造;塑料零件制造;其他未列明金属制品制造(不含须经前置审批许可的项目);其他金属制日用品制造;",
    "operatingTimeLimitType": 2,
    "operatingTimeLimitDateBegin": "2020-11-09 10:21:15",
    "operatingTimeLimitDateEnd": "9999-12-31 10:21:15",
    "approvalDate": "2019-09-30 10:21:15",
    "settlingTime": "2020-11-10 10:21:15",
    "externalSystemId": "11112"
}]

# EncryptData(request_data)
ba = eval(encrypt_data(request_data))  # 转换成字典格式，eval函数可以实现list、dict、tuple与str之间的转化
ba['token'] = token  # 请求中添加token信息
# print(json.dumps(ba))

# 请求填报信息
qytbsj_res = requests.post(url=qytb_url, data=json.dumps(ba), headers=headers)  # json.dumps把请求转换成json格式的编码
print(qytbsj_res.text)
