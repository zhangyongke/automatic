# -*- coding:utf-8 -*-
# Time:2021/12/11 21:08
# Author:zyk
# FileName:ch2_列表.py
# SoftWare:PyCharm
languages = ['python', 'C', 'C#', 'JAVA', 'go']
for language in languages:
    print(language)

# 1、使用列表中的各个值
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

# 2、修改列表元素
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles[0] = "ducati"
print(motorcycles)

# 3、添加元素，在列表末尾添加元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

# 4、动态创建列表
motorcycles1 = []
motorcycles1.append("honda")
motorcycles1.append("yamaha")
motorcycles1.append("suzuki")
print(motorcycles1)

# 5、在列表中插入元素
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.insert(0, "ducati")
print(motorcycles)

# 6、（1）在列表中删除元素，使用del可删除任何位置的列表元素
motorcycles = ["honda", "yamaha", "suzuki"]
del motorcycles[0]
print(motorcycles)
# （2）使用方法pop()删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
pppped_motorcycle = motorcycles.pop()
print(motorcycles)
print(pppped_motorcycle)

# （3）、根据值删除元素
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

# 7、组织列表，(1)使用sort()方法对列表进行永久性排序，默认按字母正序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# 按与字母顺序相反的顺序排列列表元素，则可以添加参数，reverse = True
cars.sort(reverse=True)
print(cars)

# （2）、使用sorted()方法对列表进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
print(cars)

# 8、倒着打印列表，注意reverse() 不是指按与字母顺序相反的顺序排列列表元素， 而只是反转列表元素的排列顺序：
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

# 9、(1)遍历整个列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
# (2)在for 循环中执行更多的操作
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a greet trick!")

# 10、使用range()创建数字列表，要创建数字列表，可使用函数list()将range()的结果直接转为列表。
numbers = list(range(1, 6))
print(numbers)

# 11、列表解析
squares = [value ** 2 for value in range(1, 6)]
print(squares)

# 12、列表切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
# 13、列表操作
print([1] * 5)

# 13、用队列实现斐波那契数列
count = 5
a, b = 1, 1
ls = []
for i in range(count):
    ls.append(a)
    a, b = b, a+b
print(ls)
