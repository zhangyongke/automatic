# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 10:39 PM
# @Author  : zyk
# @Email   : zhangyongke1105@163.com
# @File    : test.py
# @Software : PyCharm
from selenium import webdriver


# 在列表之间移动元素
# 首先，创建一个待验证码用户列表，和一个用于存储已验证用户的空列表
unconfirmed_users = ['alic', 'brian', 'candace']
confirmed_users = []
# 验证每个用户，直到没有未验证的用户为止，并将每个验证过的用户都添加到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# 显示所有已验证过的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


# 函数关键字实参
def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(animal_type='hamster', pet_name='hunry')


# 函数默认值
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(pet_name='willie')
describe_pet('willie')


# 函数返回值
# def get_formatterd_name(first_name, last_name):
#     """返回完整的姓名"""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
#
#
# musician = get_formatterd_name('jimi', 'hendrix')
# print(musician)


# 让实参变成可选的
def get_formatterd_name(first_name, last_name, middle_name=''):
    """返回整个的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatterd_name('jimi', 'hendrix')
print(musician)
musician = get_formatterd_name('john', 'hooker', 'lee')
print(musician)

# 返回字典




