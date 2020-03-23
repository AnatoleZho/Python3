#!/usr/bin/python
# -*- coding: utf-8 -*-


#  类

# 1.创建和使用类

#1.1 创建 Dog 类
'''Python 中首字母大写的名称指的是类。'''
class Dog(object):
    '''一次模拟小狗的简单尝试'''
    def __init__(self, name, age):
        '''初始化属行 name 和 age'''
        self.name = name
        self.age = age

    def sit(self):
        '''模拟小狗被命令时坐下'''
        print self.name.title() + ' is now sitting.'

    def roll_over(self):
        '''模拟小狗被命令时打滚'''
        print self.name.title() + ' rolled over!'


'''
1. 方法 __init__() 
   类中的函数称为方法；有关函数的一切都适用于方法，就目前唯一的差别就是调用的方式。__init__()
   是一个特殊的方法，每当根据类创建实例时，Python都会自动运行它。这个方法的名称开头和结尾都
   使用两个下划线，旨在避免 Python 默认方法与普通方法发声名称上的冲突。
   __init__() 定义成了包含三个形参：self、name 和 age。在这个方法中形参必不可少的，且必须
   放在其他的形参前面。
'''


# 1.2 根据类创建实例
my_dog = Dog('willie', 6)


'''1.访问属性'''
print "My dof's name is " + my_dog.name.title() + '.'

print 'My dog is ' + str(my_dog.age) + ' years old.'


'''2.调用方法'''
my_dog.sit()

my_dog.roll_over()


'''3.创建多个实例'''
your_dog = Dog('lucy', 3)
your_dog.sit()
your_dog.roll_over()



# 2. 使用类和实例

# 2.1 Car 类

class Car(object):
    '''一次模拟汽车的简单尝试'''
    def __init__(self, make, model, year):
        '''初始化描述汽车的属行'''
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        '''返回整洁的描述性信息'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

my_new_car = Car('audo', 'a4', 2016)

print my_new_car.get_descriptive_name()


# 2.2 给属行指定默认值

class Car(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


    def read_odometer(self):
        print 'This car has ' + str(self.odometer_reading) + ' miles in it.'


    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print "You can't roll back an odometer!"

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles


my_used_car = Car('bwm', 'x5', 2016)
print my_used_car.get_descriptive_name()

my_used_car.read_odometer()


# 2.3 修改属行的值
'''
可以通过三种不同的方式修改属行的值：1.接通过实例进行修改； 2. 通过方法进行设置；
                               3. 通过方法递增（增加特定的值）
'''

'''1. 直接修改属行的值'''
my_used_car.odometer_reading = 23
my_used_car.read_odometer()


'''2.通过方法修改属行的值'''
my_used_car.update_odometer(2200)
my_used_car.read_odometer()


'''3.通过方法对属性的值进行递增'''
my_used_car.increment_odometer(100)
my_used_car.read_odometer()



# 3. 继承

# 3.1 子类的方法 __init__()
class ElectricCar(Car):
    '''电动汽车的独特之处'''
    def __init__(self, make, model, year):
        '''初始化父类的属行'''
        super(ElectricCar, self).__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print my_tesla.get_descriptive_name()


# 3.2 给子类定义属行和方法
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)
        self.battery_size = 70


    def describe_battery(self):
        print "This car has a " + str(self.battery_size) + '-kWh battery.'


    def get_descriptive_name(self):
        long_name = 'sub ' + str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print my_tesla.get_descriptive_name()

my_tesla.describe_battery()


# 3.3 重写父类方法
'''
对于父类方法，只要它不符合子类模拟的实物的行为，都可以对其重写。因此，子类中可以定一个方法名与
要重写父类方法同名。 这样只会关注子类中定义的相应方法。
'''

print my_tesla.get_descriptive_name()


# 3.4 将实例用作属行

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print "This car has a " + str(self.battery_size) + '-kWh battery.'


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)
        self.battery = Battery()


    def describe_battery(self):
        print "This car has a " + str(self.battery_size) + '-kWh battery.'


    def get_descriptive_name(self):
        long_name = 'sub ' + str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()



my_tesla = ElectricCar('tesla', 'model s', 2016)
print my_tesla.get_descriptive_name()

my_tesla.battery.describe_battery()




# 4. 导入类

# 4.1 导入单个类
'''from car import Car'''

# 4.2 在一个模块中存储多个类

# 4.3 从一个模块中导入多个类
'''❶ from car import Car, ElectricCar'''

# 4.4 导入整个模块
'''import car'''

# 4.5 导入模块中的所有类
'''from module_name import *'''

# 4.6 在一个模块中导入另一个模块



#  5.类编码风格
'''驼峰命名法'''

