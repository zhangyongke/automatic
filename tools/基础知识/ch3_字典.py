# -*- coding: utf-8 -*-
# @Time : 2020/11/27 16:26
# @Author : zyk
# @Email : zhangyongke1105@163.com
# @File : ch3_字典.py
# @Software: PyCharm


# 一个将人名用作键的字典。每个人都用一个字典表示
# people = {
#     'Alice': {
#         'phone': '22341',
#         'addr': "Foo drive 23"
#     },
#     'Beth': {
#         'phone': '9102',
#         'addr': 'Bar street 42'
#     },
#     'Cecil': {
#         'phone': '3158',
#         'addr': 'Baz avenue 90'
#     }
# }
#
# # 电话号码和地址的描述性标签，供打印输出时使用
# labels = {'phone': 'phone number', 'addr': 'address'}
#
# name = input('Name: ')
#
# # 要查找电话号码还是地址
# request = input('Phone number(p) or address(a)?')
# # 使用正确的键：
# if request == 'p':
#     key = 'phone'
# if request == 'a':
#     key = 'addr'
# # 仅当名字是字典的时候
# if name in people:
#     print("{}'s {} is {}." .format(name, labels[key], people[name][key]))

# 统计一个列表中，每个元素出现的次数
languages = ['python', 'java', 'python', 'c', 'c++', 'go', 'c#', 'c++', 'lisp', 'c', 'javascript', 'java', 'python', 'matlab', 'python', 'go', 'java']
stat = {}
for language in languages:
    if language not in stat:
        stat[language] = 1
    else:
        stat[language] += 1
print(stat)
