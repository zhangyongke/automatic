# _*_coding:utf-8_*_
# @Time:       2020/11/6  10:36
# @Author:     xmsme  
# @File:       文件测试.py  
# @Software:   PyCharm

filepath = "F:\\workplace\\GitWork\\python\\文件\\pi_digits.txt"
with open(filepath) as file_object:
    contents = file_object.read()
    print(contents.rstrip())      # rstrip()方法可以删除多出来的空行

with open(filepath) as file_object:
    for line in file_object:
        print(line.rstrip())


# 创建一个包含文件各行内容的列表
# 使用关键字with 时， open() 返回的文件对象只在with 代码块内可用。 如果要在with 代码块外访问文件的内容，可在with 代码块内将文件的各行存储在
# 一个列表中， 并在with 代码块外使用该列表： 你可以立即处理文件的各个部分， 也可推迟到程序后面再处理。
filepath1 = "F:\\workplace\\GitWork\\python\\文件\\pi_digits.txt"
with open(filepath1) as file_object1:
    lines = file_object1.readlines()

for line1 in lines:
    print(line1.rstrip())

# 使用文件的内容：将文件读取到内存中后，就可以在任何方式使用这些数据了，
filename = 'F:\\workplace\\GitWork\\python\\文件\\pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))
