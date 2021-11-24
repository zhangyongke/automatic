# _*_coding:utf-8_*_
# @Time:       2020/11/5  11:20
# @Author:     xmsme  
# @File:       ch4_类.py
# @Software:   PyCharm


# 创建类,类中的函数叫方法
class Dog:
    """一次模拟小狗的简单尝试"""
    # 定义构造方法
    def __init__(self, name, age):
        # 为何必须在方法定义中包含形参self 呢？ 因为Python调用这个__init__() 方法来创建Dog 实例时， 将自动传入实参self 。
        # 每个与类相关联的方法调用都自动传递实参self ，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。
        self.name = name        # 以self 为前缀的变量都可供类中的所有方法使用，我们还可以通过类的任何实例来访问这些变量。
        self.age = age

    def sit(self):
        """模拟小狗被命令"""
        print(self.name.title() + "is now sitting.")

    def roll_over(self):
        """模拟小狗打滚"""
        print(self.name.title() + " rolled over!")


# 使用类和实列
class Car:
    """一次模拟描述汽车的属性"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整个车的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + "miles on it.")

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值"""
        if mileage > self.odometer_reading:     # 检查公里数是否合法
            self.odometer_reading = mileage   # 这个方法接受一个里程值，并将其存储到self.odometer_reading中。
        else:
            print("You can not roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加到制定的变量中"""
        self.odometer_reading += miles


# 初始化对象
my_car = Car('audi', 'A4', '2014')
print(my_car.get_descriptive_name())
my_car.read_odometer()
my_car.update_odometer(23)
my_car.increment_odometer(10)
my_car.read_odometer()
