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

other_url = "/api/creditInquiry/administrativeLicensing"

request_url = base_url + other_url
headers = {"Content-Type": "application/json; charset=UTF-8"}

publicKey = '0429C374822DF3B6EE94B47AB0D35F692C10F3545DA1EB5D2C28C24CC6BFD407DA3C6843C47FD3510DA2D43D39E0F4BEEC106CDFFF54D03EAA98F05BB5FE8A26BE'


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


# 获取token请求
def get_token():
    data = {"appId": "cea72a86f5a948f0a8551d028c11a6ad",
            "appKey": "anhuihuangshan",
            "appSecret": "cea72a86f5a948f0a8551d028c11a6ad1609326968161"
            }
    # 请求token前先对用户信息数据加密
    request_body = encrypt_data(data)
    # 进行token请求
    response_body = requests.post(url=token_url, data=request_body, headers=headers)
    json_date = json.loads(response_body.text)    # 将字符串格式转换为字典格式，其中response_body.text表示接口请求的返回结果信息
    if json_date['success']:
        # 返回数据进行解密
        token = decrypt_data(response_body)
        return token
    else:
        print("token请求失败，请确认用户信息")


a = get_token()
# print(a)


# 公开信息汇总查询接口
def public_information():
    request_data = {"requestData": "{\"enterpriseName\": \"厦门中小在线信息服务有限公司\"}", "publicKey": publicKey, 'token': a}
    return_res = requests.post(url=request_url, data=json.dumps(request_data), headers=headers)  # 把请求转换成json格式的编码
    return return_res.text


b = public_information()
print(b)



# # 企业填报接口
# request_data = [{
#     "uniscId": "91310000695772014M",
#     "enterpriseName": "上海正帆科技股份有限公司",
#     "address": "上海市沈河区万柳塘路38号",
#     "industry": "1",
#     "province": "上海市",
#     "city": "上海市",
#     "area": "闵行区",
#     "registeredCapital": 120,
#     "businessScope": "日用塑料制品制造;塑料零件制造;其他未列明金属制品制造(不含须经前置审批许可的项目);其他金属制日用品制造;",
#     "operatingTimeLimitType": 2,
#     "operatingTimeLimitDateBegin": "2020-11-09 10:21:15",
#     "operatingTimeLimitDateEnd": "9999-12-31 10:21:15",
#     "approvalDate": "2019-09-30 10:21:15",
#     "settlingTime": "2020-11-10 10:21:15",
#     "externalSystemId": "11112"
# }]
#
# # EncryptData(request_data)
# ba = eval(encrypt_data(request_data))  # 转换成字典格式，eval函数可以实现list、dict、tuple与str之间的转化
# ba['token'] = token  # 请求中添加token信息
# # print(json.dumps(ba))

# # 请求填报信息
# qytbsj_res = requests.post(url=request_url, data=json.dumps(ba), headers=headers)  # json.dumps把请求转换成json格式的编码
# print(qytbsj_res.text)


# 请求信用中国-公开信息汇总查询接口
# request_data = {
#     "requestData": "{\"enterpriseName\": \"厦门中小在线信息服务有限公司\"}",
#     "publicKey": publicKey
# }

# 请求信用中国-注册登记信息查询
# request_data = {
#     "requestData": "{\"enterpriseName\": \"厦门中小在线信息服务有限公司\",\"uniscId\": \"91350200761733778F\"}",
#     "publicKey": publicKey
# }

# 请求信用中国-行政许可
# request_data = {
#     "requestData": "{\"enterpriseName\": \"厦门中小在线信息服务有限公司\",\"uniscId\": \"91350200761733778F\"}",
#     "publicKey": publicKey
# }

# 请求信用中国-行政处罚
# request_data = {
#     "requestData": "{\"enterpriseName\": \"厦门中小在线信息服务有限公司\",\"uniscId\": \"91350200761733778F\"}",
#     "publicKey": publicKey
# }

# 请求信用中国-失信惩戒查询接口
# request_data = {
#     "requestData": "{\"enterpriseName\": \"厦门中小在线信息服务有限公司\"}",
#     "publicKey": publicKey
# }

# 请求信用中国-授信激励查询接口
# request_data = {
#     "requestData": "{\"enterpriseName\": \"厦门中小在线信息服务有限公司\"}",
#     "publicKey": publicKey
# }

# 生产环境授权id:007d86c0589e4311aae71cc429537b55
# 测试环境授权id:d677e088dcfa4565b26aa89c95c68cfa

# 请求授权查询-法人纳税接口
# request_data = {
#     "requestData": "{\"enterpriseName\": \"厦门中小在线信息服务有限公司\",\"uniscId\": \"91350200761733778F\","
#                    "\"licenseId\": \"619b0c39687f4b4189edb3e954c1ecb6\"}",
#     "publicKey": publicKey
# }

# 请求授权查询-法人纳税接口
# request_data = {
#     "requestData": "{\"enterpriseName\": \"厦门中小在线信息服务有限公司\",\"uniscId\": \"91350200761733778F\","
#                    "\"licenseId\": \"619b0c39687f4b4189edb3e954c1ecb6\"}",
#     "publicKey": publicKey
# }

# 请求授权查询-法人社保缴费信息查询
# request_data = {
#     "requestData": "{\"enterpriseName\": \"厦门中小在线信息服务有限公司\",\"uniscId\": \"91350200761733778F\","
#                    "\"licenseId\": \"619b0c39687f4b4189edb3e954c1ecb6\"}",
#     "publicKey": publicKey
# }

# 请求授权-法人社保欠费查询
# request_data = {
#     "requestData": "{\"enterpriseName\": \"厦门中小在线信息服务有限公司\",\"uniscId\": \"91350200761733778F\","
#                    "\"licenseId\": \"619b0c39687f4b4189edb3e954c1ecb6\"}",
#     "publicKey": publicKey
# }

# 请求授权-法人公积金缴存信息查询
# request_data = {
#     "requestData": "{\"enterpriseName\": \"厦门中小在线信息服务有限公司\",\"uniscId\": \"91350200761733778F\","
#                    "\"licenseId\": \"619b0c39687f4b4189edb3e954c1ecb6\"}",
# #     "publicKey": publicKey
# }

# 请求授权-公共资源交易记录查询
# request_data = {
#     "requestData": "{\"enterpriseName\": \"厦门中小在线信息服务有限公司\",\"uniscId\": \"91350200761733778F\",\"year\":\"2020\","
#                    "\"type\":\"00\",\"pageIndex\":\"1\",\"pageSize\":\"10\","
#                    "\"licenseId\": \"619b0c39687f4b4189edb3e954c1ecb6\"}",
#     "publicKey": publicKey
# }

# ba = request_data
# ba['token'] = token  # 请求中添加token信息

# # 融资统计回传接口
# request_data = [{
#     "province": "安徽省",
#     "city": "黄山市",
#     "area": "",
#     "areaCode": "341000",
#     "registeredEnterpriseNum": 3000,
#     "creditEnterpriseNum": 3800,
#     "loanEnterpriseNum": 3500,
#     "creditLoanEnterpriseNum": 3300,
#     "financingNeedsEnterpriseNum": 3850,
#     "creditAmount": 20211,
#     "creditNum": 465,
#     "loanAmount": 18000,
#     "loanNum": 430,
#     "creditLoanAmount": 6112,
#     "creditLoanNum": 410,
#     "financingNeedsAmount": 20111,
#     "financingNeedsNum": 480,
#     "dockingNum": 30,
#     "overdueNum": 10,
#     "averageLendingRate": 5.8,
#     "fullBusinessProcessAveragePeriod": 5,
#     "creditAveragePeriod": "5",
#     "loanAveragePeriod": "5",
#     "creditLoanAveragePeriod": "10",
#     "settledInFinancialInstitutionNum": 15,  # //入驻金融机构数
#     "financialProductsNum": 25,               # //发布金融产品数
#     "nearlyYearLoanAmount": 1580.86,        # //近一年放款金额
#     "nearlyYearLoanNum": 1300,                  # //近一年放款笔数
#     "nearlyYearLoanEnterpriseNum": 652,       # //近一年放款企业数
#     "nearlyYearCreditLoanAmount": 1255.96,  # //近一年信用放款金额
#     "nearlyYearCreditLoanNum": 1280,           # //近一年信用放款笔数
#     "nearlyYearCreditLoanEnterpriseNum": 642,  # //近一年信用放款企业数
#     "nearlyYearFinancingNeedsAmount": 1200.89,   # //近一年融资需求金额
#     "nearlyYearFinancingNeedsNum": 10,       # //近一年融资需求笔数
#     "statisticsBeginTime": "2019-11-11 10:21:15",  # //统计开始时间
#     "statisticsEndTime": "2020-12-30 14:21:15",    # //统计截止时间
#     "externalSystemId": "111111"                    # 外部系统id
# }]
#
# ba = eval(encrypt_data(request_data))  # 转换成字典格式，eval函数可以实现list、dict、tuple与str之间的转化
# ba['token'] = token  # 请求中添加token信息

# 信用中国接口-查询
# return_res = requests.post(url=request_url, data=json.dumps(ba), headers=headers)  # json.dumps把请求转换成json格式的编码
# print(return_res.text)
