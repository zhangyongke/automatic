# -*- coding: utf-8 -*-
# @Time : 2020/11/12 17:00
# @Author : zyk
# @Email : zhangyongke1105@163.com
# @File : 异常测试.py
# @Software: PyCharm
import json
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
