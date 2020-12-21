# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 10:39 PM
# @Author  : zyk
# @Email   : zhangyongke1105@163.com
# @File    : test.py
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

# 列表反转,reversed返回一个迭代器，可以使用list将返回的对象转换为列表
x = [1, 2, 3]
print(list(reversed(x)))
# 元组和列表之间可以互相转换，使用tuple()转换成元组，使用list()转换成列表


#
# # 函数关键字实参
# def describe_pet(animal_type, pet_name):
#     """显示宠物信息"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
#
# describe_pet(animal_type='hamster', pet_name='hungry')
#
#
# # 函数默认值
# def describe_pet(pet_name, animal_type='dog'):
#     """显示宠物信息"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
#
# describe_pet(pet_name='willie')
# describe_pet('willie')
#
#
# # 函数返回值
# # def get_format_name(first_name, last_name):
# #     """返回完整的姓名"""
# #     full_name = first_name + ' ' + last_name
# #     return full_name.title()
# #
# #
# # musician = get_format_name('jimi', 'hendrix')
# # print(musician)
#
#
# # 让实参变成可选的
# def get_format_name(first_name, last_name, middle_name=''):
#     """返回整个的姓名"""
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()
#
#
# musician = get_format_name('jimi', 'hendrix')
# print(musician)
# musician = get_format_name('john', 'hooker', 'lee')
# print(musician)
#
#
# # 返回字典
# def build_person(first_name, last_name, age=''):
#     """返回一个字典，其中包含一个人的信息"""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
#
#
# musician = build_person('jimi', 'hendrix', age='17')
# print(musician)
#
#
# # 结合使用函数和while循环
# def get_format_name(first_name, last_name, middle_name=''):
#     """返回整个的姓名"""
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()
#
#
# # 这是一个循环
# # 向函数传递列表
# def greet_users(names):
#     """向列表中的每位用户都发出简单的问候"""
#     for name in names:
#         msg = "Hello," + name.title() + "!"
#         print(msg)
#
#
# usernames = ['hannah', 'try', 'margot']
# greet_users(usernames)
#
#
# # 传递任意数量的实参
# def make_pizza(*toppings):   # 形参名*toppings中的星号让python创建一个名为toppings的空元组，并将收到的所有值都封装到这个元组中
#     """概述要制作的披萨"""
#     print("\nMake a pizza with the following toppings:")
#     for topping in toppings:
#         print("- " + topping)
#
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')
#
#
# # 使用任意数量的关键字实参
# def build_profile(first, last, **user_info):     # 形参**user_info中的两个星号让python创建一个名为user_info的空字典，并将收到的所有名称-值对都封装到这个字典中
#     """创建一个字典，其中包含我们知道的有关用户的一切"""
#     profile = {'first_name': first, 'last_name': last}
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile
#
#
# user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
# print(user_profile)

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

