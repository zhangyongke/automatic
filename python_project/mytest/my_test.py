# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 10:39 PM
# @Author  : zyk
# @Email   : zhangyongke1105@163.com
# @File    : my_test.py
# @Software : PyCharm


# # 在列表之间移动元素
# # 首先，创建一个待验证码用户列表，和一个用于存储已验证用户的空列表
# unconfirmed_users = ['alic', 'brian', 'candace']
# confirmed_users = []
# # 验证每个用户，直到没有未验证的用户为止，并将每个验证过的用户都添加到已验证用户列表中
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print("Verifying user: " + current_user.title())
#     confirmed_users.append(current_user)
#
# # 显示所有已验证过的用户
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# # 列表反转,reversed返回一个迭代器，可以使用list将返回的对象转换为列表
# x = [1, 2, 3]
# print(list(reversed(x)))


# 元组和列表之间可以互相转换，使用tuple()转换成元组，使用list()转换成列表


# pow(x, y)该函数表示，执行x的y次方，如下
# a = pow(2, 3)
# b = 10 + pow(2, 3*5)/3.0
# print(a, b)
#
# # abs计算绝对值，round将浮点数圆整为与之最接近的整数,2//3表示向下取整数，如下
# c = abs(-10)
# d = round(2/3)
# e = 2//3
# print(c, d, e)


x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z']
z = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*']
# a = input("请输入企业名称：\n")
# for i in range(0, len(a)):
#     # print(type(a[i]))
#     if a[i] in str(x) or a[i].lower() in y or a[i] in z:
#         print("企业名称输入不能包含数字和字母！请重新输入！")
#         break
flag = True
while flag:
    a = input("请输入企业名称：\n")
    for i in range(0, len(a)):
        # print(type(a[i]))
        if a[i] in str(x) or a[i].lower() in y or a[i] in z:
            print("企业名称输入不能包含数字和字母！请重新输入！")
            flag = False
            break



