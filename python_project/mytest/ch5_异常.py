# -*- coding: utf-8 -*-
# @Time : 2020/11/12 17:00
# @Author : zyk
# @Email : zhangyongke1105@163.com
# @File : ch5_异常.py
# @Software: PyCharm
# 使用try:
# except Exception as e方式对异常对象进行检查，这样做将让不是从Exception派生而来的为数不多的异常成为漏网之鱼
# try-except-else 代码块的工作原理大致如下： Python尝试执行try代码块中的代码；只有可能引发异常的代码才需要放在try 语句中。有时候有一些仅在try 代码块成功
# 执行时才需要运行的代码；这些代码应放在else 代码块中。except代码块告诉Python，如果它尝试运行try 代码块中的代码时引发了指定的异常，该怎么办。
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst_number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond_number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

# 处理FileNotFoundError异常
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        content = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + "does not exist."
    print(msg)

