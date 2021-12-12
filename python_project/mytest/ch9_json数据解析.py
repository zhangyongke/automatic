# -*- coding:utf-8 -*-
# Time:2021/11/23 22:09
# Author:zyk
# FileName:ch9_json数据解析.py
# SoftWare:PyCharm
import json

"""json模块中json.dumps()函数将python对象编码成JSON字符串"""
# 使用json.dump()和json.load()
# 第一个程序将使用json.dump()来存储这组数字，而第二个程序将使用json.load() 。函数json.dump()接受两个实参：要存储的数据以及可用于存储数据的文件对象。

numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)    # 使用函数json.dump() 将数字列表存储到文件numbers.json中


filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)    # 使用函数json.load()加载存储在numbers.json中的信息，并将其存储到变量numbers 中
print(numbers)

# 如果以前存储了用户名， 就加载它
# 否则， 就提示用户输入用户名并存储它
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")
