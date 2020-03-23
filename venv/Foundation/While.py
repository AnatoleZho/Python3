#!/usr/bin/python
# -*- coding: utf-8 -*-

# 用户输入和 while 循环

# 1. 函数 input() 的工作原理
# 下面的程序让用户输入一些文本，再将这些文本呈现给用户：
'''
message = raw_input("Tell me something, and I will repeat it back to you:")
print str(message)
'''


# 1.1. 编写清晰的程序
'''
name = raw_input('Please enter your name:')
print 'Hello, ' + name.title() + '!'
'''

# 1.2 使用 int() 来获取数值输入
'''
height = raw_input('How tail are you, in inches?')
height = int(height)

if height >= 36:
    print "\nYou'are tall enough to ride!"
else:
    print "\nYou'll be able to ride when you're a little older."
'''

# 1.3 求模运算符
'''
number = raw_input("Enter a number, and I'll tell you if it's even or odd:")
number = int(number)

if number % 2 == 0:
    print '\nThe number ' + str(number) + ' is even.'
else:
    print '\nThe number ' + str(number) + ' is odd.'
'''


# 2. while 循环
# while 循环不断运行，直到指定的条件不满足为止

# 2.1 使用 while 循环
'''
current_number = 1
while current_number <= 5:
    print current_number
    current_number += 1

# 2.2 让用户选择何时退出
prompt = '\nTell me something, and I will repeat it back to you:'
prompt += "\nEnter 'quit' to end the program."
message = ''

while message != 'quit':
    message = raw_input(prompt)
    print message
'''

# 2.3. 使用标志
'''
在要求很多条件都满足才继续运行的程序中，可以定义一个变量，用于判断整个程序是否处于活跃状态，这个变量被称为标志
充当了程序的信号灯。可让程序在标志为 True 时继运行，并在任何事件导致标志的值为 False 时让程序停止运行。

在 while 语句中，只需要检查一个条件---标志的当前值是否为 True， 并将所有测试（是否发生了应将标志设置为 False 事件）
都放在其他地方，从而让程序变得更简洁。
'''

'''
prompt = '\nTell me something, and I will repeat it back to you:'
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = raw_input(prompt)

    if message == 'quit':
        active = False
    else:
        print message
'''


# 2.4 使用 break 退出循环
'''
prompt = '\nTell me something, and I will repeat it back to you:'
prompt += "\nEnter 'quit' to end the program."

while True:
    city = raw_input(prompt)

    if city == 'qiut':
        break
    else:
        print "I'd love to go to " + city.title() + '!'

'''

# 2.5 在循环中使用  continue

# 2.6 避免无线循环



# 3. 使用 while 循环来处理列表和字典

# 3.1 在列表中移动元素
# 创建一个待验证的用户列表 和 一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []

# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的用户都移动到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print 'Verifying user: ' + current_user.title()
    confirmed_users.append(current_user)

# 显示所有已验证的用户
print '\nThe following users have been confirmed:'
for confirmed_user in confirmed_users:
    print confirmed_user.title()


# 3.2 删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print pets

while 'cat' in pets:
    pets.remove('cat')

print pets


# 3.3 使用用户输入来填充字典
responses = {}

# 设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    # 提示输入被调查者的名字和回答
    name = raw_input('\nWhat is your name?')
    response = raw_input("which mountain would you like to climb someday?")

    # 将答卷存储在字典中
    responses[name] = response

    # 看看是否还有人要参与调查
    repeat = raw_input('Would you like to let another person responsed?(yes/ no)')
    if repeat == 'no':
        polling_active = False

# 调查结束，显示结果
print '\n--- Poll Results---'
for name, response in responses.items():
    print name.title() + ' would like to climb ' + response.title() + '.'
