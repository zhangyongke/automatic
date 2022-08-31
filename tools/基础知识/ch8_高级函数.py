# -*- coding:utf-8 -*-
# Time:2021/11/24 21:03
# Author:zyk
# FileName:ch8_高级函数.py
# SoftWare:PyCharm


# lambda函数，可以使用lambda函数的语法定义函数，需要注意一下两点
# lambda [arg1 [,arg2,......argn]]:expression
# 1、 冒号（：）之前的arg1,arg2，......表示他们是这个函数的参数。
# 2、匿名函数不需要return来返回值，表达式本身的结果就是返回值。
sayhello = lambda: print("hello world!")
sayhello()

# 例子2
sum = lambda arg1, arg2: arg1 + arg2;
# 调用sum函数
print("相加后的值为：", sum(10, 20))

# map()函数
# map(function, iterable, ...)
# 参数说明如下
# function:是个函数，通过函数以此作用在序列中的每个元素中
# iterable:一个或多个序列，也被称为可迭代对象


def fun(x):
    return x * x


result = map(fun, [1, 2, 3])
print(list(result))

# 对列表中的每个元素加3
result = map((lambda x: x+3), [1, 3, 5, 6])
print(list(result))

# 两个列表的每个元素实现相加的功能
result = map((lambda x, y : x + y), [1, 3, 5], [2, 4, 6])
print(list(result))
