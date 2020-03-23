#!/usr/bin/python
# -*- coding: utf-8 -*-


'''   函数   '''
# 1. 定义函数
def greet_user():
    '''显示简单的问候语'''
    print 'Hello!'


greet_user()


# 1.1 向函数传递信息
def great_user(username):
    print 'Hello, ' + username.title() + '!'

great_user('jesse')


# 1.2 实参和形参
'''
在函数greet_user() 的定义中，变量username 是一个形参 ——函数完成其工作所需的一项信息。在代
码greet_user('jesse') 中，值'jesse' 是一个实参 。实参是 调用函数时传递给函数的信息。我们
调用函数时，将要让函数使用的信息放在括号内。在greet_user('jesse') 中，将实参'jesse' 传递
给了函数greet_user() ，这个 值被存储在形参username 中。
'''


# 2. 传递实参
'''
鉴于函数定义中可能包含多个形参，因此函数调用中可能包含多个实参。向函数传递实参的方式很多，可以
使用位置实参，这要求实参的顺序和形参相同；可以使用关键字实参，其中每个实参都由变量名和值组成；
还可以使用列表和字典。
'''

# 2.1 位置实参
'''调用函数时，Python 必须将函数调用中的每个实参都关联到函数定义中的一个形参。为此最简单的关联
方式是基于实参的顺序。
'''
def describe_pet(animal_type, pet_name):
    print '\nI have a ' + animal_type + '.'
    print 'My ' + animal_type + "'s name is " + pet_name.title() + '.'

describe_pet('hamster', 'harry')


# 2.2 关键字实参
'''
关键字实参是传递给函数的名称--值对。直接在实参中将名字和值关联起来，因此向函数传递实参不会混淆。
关键字实参无需考虑函数调用中的实参顺序，还很清楚的指出了函数调用中各个值的用途。
'''
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')


# 2.3 默认值
# 注意：此处要注意实参顺序
def describe_pet(pet_name, animal_type='dog'):
    print '\nI have a ' + animal_type + '.'
    print "My " + animal_type + "'s name is " + pet_name.title() + "."

describe_pet(pet_name='willie')

# 2.4 等效的函数调用
# 一条名为Willie的小狗
describe_pet('willie')

describe_pet(pet_name='willie')
# 一只名为Harry的仓鼠
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')



# 2.5 避免实参错误
'''要注意实参匹配'''



# 3. 返回值

# 3.1. 返回简单值
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print '\n'
print musician


# 3.2 让实参变成可选的
'''
有时候，需要让实参变成可选的，这样使用函数是就只需要在必要时才提供额外的信息。可使用默认值来
实现实参可选
'''
def get_formatted_nameB(first_name, last_name, middle_name = ''):
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_nameB('john', 'hooker', 'lee')
print musician


musician = get_formatted_nameB("jimi", 'hendrix')
print musician


# 3.3 返回字典
def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print musician

def build_personB(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_personB('jimi', 'hendrix', age=27)
print musician



# 4. 传递列表
def greet_users(names):
    for name in names:
        msg = 'Hello,' + name.title() + '.'
        print msg

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


# 4.1 在函数中修改列表
def print_models(unprinted_designs, completed_models):
    '''
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    '''
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print 'Printing model:' + current_design
        completed_models.append(current_design)

def show_completed_models(completed_models):
    '''显示打印好的所有模型'''
    print '\nThe following models have been printed:'
    for completed_model in completed_models:
        print completed_models



unprinted_designs = ['iphone case', 'robot pendant', 'dodeca hedron']
compeleted_models = []

print_models(unprinted_designs, compeleted_models)
show_completed_models(compeleted_models)


# 4.2 禁止函数修改列表
'''
为解决这个问题，可向函数传递列表的副本而不是原件，这样函数所做的任意改动都只影响副本，对原件
没有任何影响
要将列表的副本传递给函数，使用切片表示法，创建列表的副本。

注意：虽然向函数传递列表的副本可保留原始列表的内容，但除非有充分的理由需要传递副本，否则还是应
该将原始列表传递给函数，因为让函数使用现成列表可避免花时间和内存创建副本，从而提高效率，在处理
大型列表时尤其如此。
'''

print_models(unprinted_designs[:], compeleted_models)



# 5. 传递任意数量的实参
'''
*toppings 中的星号让 Python 创建一个名为 toppings 的空元组，并将收到的值封装到这个元组中。
'''
def make_pizza(*toppings):
    print toppings


make_pizza('pepperoni')

make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 5.1 结合使用位置实参和任意数量实参
'''
如果让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的实参放在最后。Python 先匹配
位置实参和关键字实参，再将余下的实参都收集在最后一个形参中。
'''
def make_pizzaB(size, *toppings):
    '''概述要制作的披萨'''
    print '\nMaking a ' + str(size) + '-inch pizza with the following toppings: '
    for topping in toppings:
        print '-' + topping

make_pizzaB(16, 'pepperoni')

make_pizzaB(12, 'mushrooms', 'green peppers', 'extra cheese')


# 5.2 使用任意数量的关键字实参
'''
有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。这种情况下可将函数
编写成接受任意数量的键--值对，调用函数时提供了多少就接受多少.

注意：形参 **user_info 中的两个星号，让 Python 创建一个名为 user_info 的空字典，并将接收
到的名称--值对都封装在这个字典中。这个函数中可以像访问字典那样访问 user_info
'''

def build_profile(first, last, **user_info):
    '''创建一个字典，其中包含我们知道的相关用户的一切'''
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='prinecton', field='physics')

print user_profile



# 6. 将函数存储在模块中
'''
函数的优点之一是，使用它们可以将代码块与主程序分离。通过给函数指定描述性名称，可以让主程序好
理解的多。还可以更进一步，将函数存存储在被叫做 模块 的独立文件中，再将模块导入到主程序中。
'''

# 6.1 导入整个模块
'''
要让函数是可以导入的，得先创建模块。 模块 是扩展名为 .py 的文件，包含要导入到程序中的代码。

创建一个包含函数 make_pizza() 的模块 pizza.py 文件

接下来，在 pizza.py 所在目录中创建一个名为 making_pizzas.py 的文件

将 pizza 模块导入到 making_pizzas.py 的文件，然后使用 模块名 pizza 调用 make_pizza() 函数

注：Python读取这个文件时，代码行import pizza 让Python打开文件pizza.py，并将其中的所有
函数都复制到这个程序中。你看不到复制的代码，因为这个程序运行时，Python在幕后复制这些代码。
只需知道，在making_pizzas.py中，可以使用pizza.py中定义的所有函数。
'''



# 6.2 导入特定函数
'''
可以导入模块中的特定函数， 导入的语法如下：
from module_name import function_name

通过逗号分隔函数名，可以根据需要从模块中导入任意数量的函数：
from module_name import function_0, function_1, function_2

此时调用时不需要加上模块名字：function_0()
'''


# 6.3 使用 as 给函数指定别名
'''
如果要导入的函数的名字可能与程序中现有的名字冲突，或者函数的名字太长，可指定简短且独一无二的
别名。 
要给函数指定别名，需要在导入它时就指定。

from module_name import function_name as fn
'''


# 6.4 使用 as 给模块指定别名
'''
可以给模块指定别名。 通过给模块指定简短的别名，能够更加轻松的调用模块中的函数。

import module_name as m

m.function_name()o
'''


# 6.5 导入模块中的所有函数
'''
使用星号（*） 运算符可让 Python 导入模块中的所有函数。

from module_name import *

'''



# 7 函数编写指南
'''
编写函数时，需要注意一下几个细节：
1.应给函数指定描述性名称，且只在其中使用小写字母和下划线。
2.每个函数都应该包含简要的阐述其功能的注释，该注释应该紧跟咋函数的定义后面，并采用文档字符串
  形式。
3.给形参指定默认值时，等号两边不要有空格。
  def function_name(parameter_0, parameter_1='default value')
4.对于函数调用中的关键字实参，也要遵循等号两边不要有空格
  function_name(value_0, parameter_1='value')
5.如果程序或模块包含多个函数，可使用两个空行将相邻的函数分开。
6.所有 import 语句都应该放在文件开头，唯一例外的情形是，在文件开头使用了注释来描述整个程序。


'''