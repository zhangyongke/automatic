# _*_coding:utf-8_*_
# @Time:       2020/11/5  16:44
# @Author:     xmsme  
# @File:       类的继承.py  
# @Software:   PyCharm


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


class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)   # super() 是一个特殊函数， 帮助Python将父类和子类关联起来。 这行代码让Python调
        # 用ElectricCar 的父类的方法__init__() ， 让ElectricCar 实例包含父类的所有属性。 父类也称为超类 （superclass） ， 名称super因此而得名
        self.battery_size = 70

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kwh battery.")


my_tesla = ElectricCar('tesla', 'model', '2016')
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
