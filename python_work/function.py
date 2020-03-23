#  函数
#  1. 定义函数
def greet_user():
	'''显示简单的问候语'''
	print("Hello!")

greet_user()
"""
  1. 关键字 def 来定义函数，后面接函数名
  2. 括号内部可以增加函数的参数
  3. 函数内部的注释文本称为 文档字符串(docstring）的注释，描述了函数功能
  4. 函数体内部代码要进行缩进
  5. 函数调用： 函数名加小括号，括号内部为函数的参数
"""

# 1.1 向函数传递信息
def greet_user(username):
	'''显示简单的问候语'''
	print("Hello, " + username.title() + "!")

greet_user("jesse")

# 1.2 实参和形参
'''
在函数 greet_user() 的定义中，变量 username 是一个形参
在代码 greet_user("jesse") 中， 值 'jesse' 是一个实参
'''

# 2. 传递实参
"""
鉴于函数定义是可能包含多个形参，因此函数调用中也可能包含多个实参。向函数传递实参的方式很多，可使用位置实参，
这要实参位置和形参位置相同；也可以用关键字实参，其中每个实参都由变量名和值组成；还可以使用列表和字典。
"""
# 2.1. 位置实参   顺序很重要
'''
调用函数时，必须将函数调用中的每个实参都关联到函数定义中的一个形参。为此，最简单的关联方式是基于实参的顺序
'''
def describe_pet(animal_type, pet_name):
	'''显示宠物的信息'''
	print("\nI have a " + animal_type + '.')
	print("My " + animal_type + "'s name  is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')


# 2.2 关键字实参
'''
关键字实参 是传递给函数的名称--值对。直接在是惨重将名称和值关联起来
'''
def describe_pet(animal_type, pet_name):
	'''显示宠物的信息'''
	print('\nI have a ' + animal_type + '.')
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type="hamster", pet_name='harry')


# 2.3 默认值
def describe_pet(pet_name, animal_type='dog'):
	'''显示宠物的信息'''
	print('\nI have a ' + animal_type + '.')
	print("My " + animal_type + "'s name is " + pet_name.title() + '.')

describe_pet(pet_name='willie')

describe_pet('willie')

describe_pet(pet_name='harry', animal_type='hamster')

# 2.4 等效的函数调用
'''
鉴于可混合使用位置实参、关键字实参和默认值，通常有多种等效的函数调用方式。
为形参提供默认值的函数：def describe_pet(pet_name, animal_type='dog'):
基于这种定义，在任何情况下都必须给pet_name提供实参；指定实参是可以使用位置方式，也可以使用关键字方式
如果要给有默认值形参提供实参，同样，指定该实参时可以使用位置方式，也可以使用关键字方式

使用哪种调用方式无关紧要，只要函数调用能生成你希望的输出就行。使用最容易理解的调用方式即可
'''

# 2.5 避免实参错误
'''
使用函数后，如果遇到实参不匹配错误，则你提供的实参多于或少于函数完成其工作所需的信息。
'''


# 3. 返回值
# 3.1. 返回简单值
def get_formatted_name(first_name, last_name):
	'''返回整洁的姓名'''
	full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name("jimi", 'hendrix')
print(musician)

# 3.2. 让实参变成可选的
'''使用默认值让实参变成可选的'''
def get_formatted_name(first_name, last_name, middle_name=''):
	'''返回整洁的姓名'''
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else: 
		full_name = first_name + ' ' + last_name
	return full_name

musician = get_formatted_name('jimi', 'hendrix')
print(musician.title())

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician.title())


# 3.3 返回字典
def build_person(first_name, last_name):
	'''返回一个字典，其中包含有关一个人的信息'''
	person = {'first': first_name, 'last': last_name}
	return person

musician = build_person('jimi', 'hendrix')
print(musician)


def build_person(first_name, last_name, age=''):
	'''返回一个字典，其中包含有关一个人的信息'''
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person

musician = build_person('jimi', 'hendrix', age=2)
print(musician)


# 4.  传递列表
def greet_users(names):
	'''向列表中的每位用户都发出简单的问候'''
	for name in names:
		msg = 'Hello, ' + name.title() + '!'
		print(msg)

usernames = ['hanah', 'ty', 'margot']
greet_users(usernames)


# 4.1 在函数中修改列表
'''将列表传递给函数后，函数就可对其进行修改。在函数中对列表所做的任何修改都是永久性的'''
# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 模拟打印每个设计，知道没有未打印的设计为止
#  打印每个设计后，都将其移到列表 completed_models 中
while unprinted_designs:
	current_design = unprinted_designs.pop()

	# 模拟根据设计制作的3D打印模型的过程
	print("Printing model:" + current_design)
	completed_models.append(current_design)

# 显示打印好的所有模型
print('\nThe following models have been printed:')
for completed_model in completed_models:
	print(completed_model)


def print_mdoels(unprint_designs, completed_models):
	'''
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
	'''
	while unprint_designs:
		current_design = unprint_designs.pop()

		# 模拟根据设计制作的3D打印模型的过程
		print("Printing model: " + current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
	'''显示打印好的所有模型'''
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)


unprinted_designs = ['iphone case', 'robot', 'dodecahedron']
completed_models = []

print_mdoels(unprinted_designs, completed_models)
show_completed_models(completed_models)


# 4.2 禁止函数修改列表
'''
向函数传递列表的副本而不是原件
function_name(list_name[:])
'''
unprinted_designs = ['iphone case', 'robot', 'dodecahedron']
completed_models = []
print_mdoels(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)


# 4.3 传递任意数量的实参
'''形参名 *toppings  中的星号让 Python 创建一个名为 toppings 的空元组， 并将所收到的所有值封装到这个元祖中'''
def make_pizza(*toppings): 
	'''打印顾客点的所有配料'''
	print(toppings)

make_pizza('pepeperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def make_pizza(*toppings):
	'''概述要制作的比萨'''
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print('- ' + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 5.1  结合使用位置实参和任意数量实参
'''
如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。 Python 先匹配位置实参和关键字实参
再将余下的实参都收集到最后一个形参中
'''
def make_pizza(size, *toppings):
	'''概述要制作的比萨'''
	print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
	for topping in toppings:
	     print('- ' + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 5.2  使用任意数量的关键字实参
'''
有时候需要接受任意数量的实参，但是预先不知道传递给函数的会是什么样的信息。这样的情况系，可将函数编写成能够接受
任意数量的键-值对----调用语句提供了多少就接受多少
'''
def build_profile(first, last, **user_info):
	'''创建一个字典， 其中包含我们知道的有关用户的一切'''
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)


# 6. 将函数存储在模块中
'''
函数的优点之一是，使用它们可以将代码块与主程序分离。还可以更进一步，将函数存储在被称为模块的独立文件中
再将模块导入到主程序中。import 语句允许在当前运行的程序文件中使用模块中的代码。
'''

# 6.1 导入整个模块
'''
要让函数是可导入的，得先创建模块。模块 是扩展名为 .py 的文件，包含要导入到程序中的代码。
'''
# 创建一个包含函数 make_pizza() 的模块, 即将 make_pizza() 函数放在 pizza.py 文件中

# 导入模块， 只要编写一条 import 语句并在其中指定模块名，就可以在程序中使用该模块中的所有函数。
import pizza
# 要调用被导入的模块中的函数，可指定导入的模块的名称和函数名，并用句点分隔开
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')


# 6.2 导入特定的函数
'''
可以导入模块中的特定函数，这种导入方法的语法如下：
from module_name import function_name
from module_name import function_0, function_1, function_2
调用的时候，只需要使用函数名即可
'''
from pizza import make_pizza

make_pizza(20, 'pepperoni')


# 6.3 使用 as 给函数指定别名
'''
如果要导入的函数的名称可能与程序中现有的名称冲突，或者函数的名称太长，可指定简短而独一无二的别名----函数的另一个名称
指定别名的通用语法如下：
from module_name import function_name as fn
'''
from pizza import make_pizza as mp

mp(18, 'pepperoni')


# 6.4 使用 as 给模块指定别名
'''
可以给模块指定别名，通过给模块指定简短的别名，能够更轻松的调用模块中的函数
'''
import pizza as p 

p.make_pizza(15, 'mushrooms')

# 6.5. 导入模块中的所有函数
'''
使用（*）运算符可让 Python 导入模块中的所有函数
import 语句中的星号让 Python 将模块 pizza 找那个的每个函数都复制到这个程序文件中。由于导入了每个函数，
可通过名称来调用每个函数，而无需使用句点表示法。然而，使用并非自己编写的大型模块时，最好不要采用这种导入方法；
如果模块中有函数的名称与自己的项目中使用的名称相同，可能导致意想不到的问题：Python 可能遇到多个名称相同的函数
或变量，进而覆盖函数，而不是分别导入所有的函数。
最好的做法是，要么只导入自己需要使用的函数，要么导入整个模块并使用句点表示法。这样让代码给清晰，更容易于阅读和理解
'''
from pizza import *

make_pizza(11, 'extra cheese')


# 7. 函数编写指南
'''
编写函数时，需要牢记几个细节。应该给函数指定描述性名称，并只在其中使用小写字母和下划线。
描述性名称可帮助你和别人明白代码想要做什么。给模块命名时也应遵守上述约定。
每个函数都应包含简要地描述其功能的注释，该注释应紧跟在函数定义后面，并采用文档字符串格式。
文档良好的函数让其他程序员只需要阅读文档字符串就可以使用它
1.给形参指定默认值时，等号两边不要有空格
2.对于函数调用中的关键字实参，也应该遵循这样的约定
3.如果程序或模块包含多个函数，可使用两个空行将相邻的函数分开
4.所有的 import 语句都应该放在文件开头，唯一例外的情形是，在文件开头使用了注释来描述整个程序
'''





