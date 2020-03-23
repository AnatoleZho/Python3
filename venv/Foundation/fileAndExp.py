#!/usr/bin/python
# -*- coding: utf-8 -*-


#   文件与异常

# 1. 从文件中读取数据

# 1.1 读取整个文件
'''执行文件与 pi_digits,txt 在同一个文件夹下'''

'''
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print contents.rstrip()
'''



# 1.2 文件路径
'''使用相对路径，text_files 文件夹与执行文件在同一个目录下'''
'''
with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
    print  contents

'''

'''使用绝对路径'''
'''/Users/anatole/Desktop/Python/venv/Foundation/text_files/pi_digits.txt'''

with open('/Users/anatole/Desktop/Python/venv/Foundation/text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
    print contents


# 1.3 逐行读取
file_name = 'pi_digits.txt'
file_path = 'text_files/' + file_name
with open(file_path) as file_object:
    for line in file_object:
        '''在文件中，每行的末尾都有一个看不见的换行符， 使用 rstrip() 消除'''
        print line.rstrip()



# 1.4 创建一个包含文件各行内容的列表
'''
使用关键字with 时，open() 返回的文件对象只在with 代码块内可用。如果要在with 代码块外访问文
件的内容，可在with 代码块内将文件的各行存储在一个列表中，并
在with 代码块外使用该列表:你可以立即处理文件的各个部分，也可推迟到程序后面再处理
'''
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print line.rstrip()


# 1.5 使用文件的内容
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print pi_string
print len(pi_string)



# 1.6 包含一百万位的大型文件
file_name = "pi_million_digits.txt"
file_path = 'text_files/' + file_name

with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

'''去掉中间空格'''
print pi_string[:52].replace(' ', '') + '...'
print len(pi_string)



# 1.7 圆周率值中包含你的生日吗
'''
birthday = raw_input('Enter your birthday, in the form mmddyy:')
if  birthday in pi_string:
    print 'Your birthday appears in the first million digits of pi.'
else:
    print 'Your birthday does not appear in the first million digit of pi!'

'''


# 2. 写入文件

# 2.1 写入空文件
file_name = 'programming.txt'
file_path = 'text_files/' + file_name
'''如果写入的文件不存在，open() 函数则会自动创建文件'''
'''
打开文件模式时，可指定读取模式（'r'）、写入模式（w）、附加模式（a）或能过读取和写入的文件模式（r+）。
如果省略了模式实参，Python 将会以默认的只读模式打开文件。
'''
with open(file_path, 'w') as file_object:
    file_object.write("I love programming!")


# 2.2 写入多行
with open(file_path, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write('I love creating new games.\n')


# 2.3 附加到文件
with open(file_path, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write('I love creating apps that can run in a browser.\n')




# 3. 异常

# 3.1 处理 ZeroDivisionError 异常
'''一个数字除以0'''
'''
print 5/0
'''


# 3.2 使用 try-except 代码块
try:
    print 5/0
except ZeroDivisionError:
    print "You can't divide by zero!"



# 3.3 使用异常避免崩溃
'''
print "Give me two numbers, and I'll divide them."
print "Enter 'q' to quit."

while True:
    first_number = raw_input('\nFirst number:')
    if first_number == 'q':
        break

    second_number = raw_input('Second number:')
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print "You can't divide by 0!"
    else:
        print answer
'''


# 3.4 处理 IOError 异常
file_name = 'alice.txt'

try:
    with open(file_name) as f_obj:
        contents = f_obj.read()
except IOError:
    msg = 'Soory, the file ' + file_name + ' does not exist.'
    print msg
else:
    print contents


# 4. 存储数据
'''
模块json 让你能够将简单的Python数据结构转储到文件中，并在程序再次运行时加载该文件中的数据。
还可以使用json 在Python程序之间分享数据。更重要的是，JSON数据
格式并非Python专用的，能够将以JSON格式存储的数据与使用其他编程语言的人分享。
'''

# 4.1 使用 json.dump() 和 json.load()
import  json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)


with open(filename) as f_obj:
    numbers = json.load(f_obj)

print numbers


# 4.2 保存和读取用户生成的数据
'''
如果以前存储了用户名，就加载它
否则，就提示用户输入用户名并保存它
'''
filename = 'username.json'

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except IOError:
    username = raw_input('What is your name?')
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print "We'll remember you when you come back, " + username.title() + '!'
else:
    print 'Welcome back, ' + username.title() + '!'



# 4.3 重构
'''
代码能够正确地运行，但可以做进一步的改进---将代码划分为完成具体工作的函数，这个过程叫重构。
重构让代码更清晰，更易理解，更容易扩展。
'''
def get_stored_username():
    '''如果存储了用户名，就获取它'''
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except IOError:
        return None
    else:
        return username


def get_new_username():
    '''提示用户输入用户名'''
    username = raw_input("Waht is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print "Welcome back, " + username.title() + '!'
    else:
        username = get_new_username()
        print "We'll remember you when you come back," + username.title() + '!'

greet_user()



















