#!/usr/bin/python
# -*- coding: utf-8 -*-


# 1. 简单示例
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print car.upper()
    elif car == 'Audi':
        print car.lower()
    else:
        print car.title()

# 2. 条件测试
'''
每条 if 语句的核心都是一个值为 True 或 False 的表达式，这种表达式被称为条件测试。
2.1  检查是否相等
    大多数条件测试都将一个变量的当前值同特定值进行比较。
2.2  检查是否相等时考虑大小写
    在 Python 中检查是否相等时区分大小写，例如，两个大小写不同的值不会被视为相等
2.3 检查是否不相等
    要判断两个值是否不等，可以结合使用惊叹号和等号(!=)
2.4 比较数字

2.5 检查多个条件

2.6 检查特定值是否包含在列表中

2.7 检查特定值是否不包含在列表中

2.9 布尔表达式
game_active = True

'''

# 2.3 检查是否不相等
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print 'Hold the anchovies!'


# 2.4 比较数字
age = 18
if age == 18:
    print True

# 2.5 检查多个条件
# 2.5.1 使用 and 检查多个条件
age_0 = 22
age_1 = 18
if age_0 >= 21 and age_1 <= 20:
    print True

# 2.5.2 使用 or 检查多个条件
if age_1 >= 21 or age_1 <= 20:
    print True

# 2.6 检查特定值是否在列表中
request_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in request_toppings:
    print True

# 2.7 检查特定值是否不包含在列表中
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print user.title() + ', you can post a response if you wish.'


# 3. if 语句
# 3.1 简单 if 语句
age = 19
if age >= 18:
    print 'You are old enough to vote!'
    print 'Have you registered to vote yet?'


# 3.2 if-else 语句
age = 17
if age >= 18:
    print 'You are old enough to vote!'
    print 'Have you registered to vote yet?'
else:
    print 'Sorry, you are too young to vote.'
    print 'Please register to vote as soon as you turn 18!'


# 3.3 if-elif-else 结构
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print 'Your admission cost is $' + str(price) + '.'



# 3.4 省略 else 代码



# 4. 使用 if 语句处理列表
# 4.1 检查特殊元素
request_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for request_topping in request_toppings:
    if request_topping == 'green peppers':
        print 'Sorry, we ate out of green peppers right now.'
    else:
        print "Adding " + request_topping + '.'
print '\nFinished making your pizza!'


# 4.2 确定列表不是空的
request_toppings = []
if request_toppings:
    for request_topping in request_toppings:
        print 'Adding ' + request_topping + '.'
    print '\n Finished making your pizza!'
else:
    print 'Are you sure you want a plain pizza?'


# 4.3 使用多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers', 'peperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', ' extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print 'Adding ' + requested_topping + '.'
    else:
        print "Sorry, we don't have" + requested_topping + "."

print '\n Finished making your pizza!'






















