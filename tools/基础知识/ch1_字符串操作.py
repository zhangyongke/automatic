# -*- coding: utf-8 -*-
# @Time : 2020/11/26 17:16
# @Author : zyk
# @Email : zhangyongke1105@163.com
# @File : ch1_字符串操作.py
# @Software: PyCharm

# # 字符串方法
# # 返回字符串首字母大写  title()方法
# a = 'this is an apple'
# b = a.title()
# print(b)
#
# # 合并序列  join是一个非常重要的字符串方法，其作用与split相反，用于合并序列的元素
# sep = '+'
# seq = ['1', '2', '3', '4', '5']
# a = sep.join(seq)
# print(a)
#
# dirs = '', 'usr', 'bin', 'env'
# b = '/'.join(dirs)
# print(b)
json = ['div/gd', 'tr[1]', 'dvi/div/button/span']
print('/'.join(json))
#
# # 返回字符串的小写版本   lower()
# a = 'Trondheim Hammer Dance'
# b = a.lower()
# print(b)
#
#
# # 将指定子串都替换为另一个字符串，并返回替换后的结果 replace()方法
# a = 'This is a test'
# b = a.replace('is', 'eez')
# print(b)
#
# # 将字符串拆分为序列 split()方法
# a = '1+2+3+4+5'
# b = a.split('+')
# print(b)
#
# a = '/usr/bin/env'
# b = a.split('/')
# print(b)
#
# a = 'Using the default'
# b = a.split()
# print(b)
#
# # 将字符串开头和末尾的空白(不包括中间的空白)删除，并返回删除后的结果 strip()，用rstrip()方法可以把右边的空格去掉，用lstrip()方法
# # 可以把左边的空格去掉。
# a = ' internal whitespace is kept '
# b = a.strip()
# print(b)
#
# # 单字符替换，translate()，然而使用translate前必须创建一个转换表，
# table = str.maketrans('cs', 'kz')
# a = 'this is an incredible test'
# b = a.translate(table)
# print(b)
