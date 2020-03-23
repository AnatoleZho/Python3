#!/usr/bin/python
# -*- coding: utf-8 -*-


# 1.列表由一系列按特定顺序排列的元素组成。
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print bicycles

# 2.访问元素
print bicycles[0]
print bicycles[0].title()


# 3. 索引 -1 返回倒数第一个元素
print bicycles[-1]
print bicycles[-2]


# 4. 修改，添加，删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print motorcycles

# 4.1. 修改
motorcycles[0] = 'ducati'
print motorcycles

# 4.2. 末尾添加元素
motorcycles.append('ducati')
print motorcycles

# 4.3. 插入元素
motorcycles.insert(0, 'ducati')
print motorcycles

# 4.4.1 删除  使用 del 语句删除元素
del motorcycles[0]
print motorcycles

# 4.4.2 删除  使用方法 pop（） 删除元素， pop（）可以删除列表末尾的元素
popped_motorcycle = motorcycles.pop()
print motorcycles
print popped_motorcycle

# 4.4.3 删除  使用 pop() 方法 删除列表任何位置的元素
first_owned = motorcycles.pop(0)
print motorcycles
print 'The first motorcyle I owned a ' + first_owned.title() + '.'


# 4.4.4 根据值删除元素  remove() 只删除第一个指定的值。 如果删除的值在列表中多次出现则需要使用循环删除
motorcycles.remove('yamaha')
print motorcycles


# 5. 组织列表
# 5.1 使用方法 sort() 对列表进行永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print  cars

# 按与字母顺序相反的顺序排列列表元素
cars.sort(reverse=True)
print cars


# 5.2 使用函数 sorted() 对列表进行临时排序
sorted_cars = sorted(cars)
print sorted_cars
print cars


# 5.3 使用 reverse() 方法倒着输出列表  反转列表元素的排列顺序
cars.reverse()
print cars


# 5.4 使用 len() 方法确定列表的长度
print len(cars)


# 6。 使用列表时避免索引错误：一个包含三个元素的列表，却要求获取第四个元素
# -*- 获取列表长度在进行访问 -*-



# 7. 操作列表
# 7.1. 遍历整个列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print magician.title()

# 7.1.1 深入地研究循环
# 使用的简单循环中，Python将首先读取其中的第一行代码: 在前面的magicians.py中使用的简单循环中，Python将首先读取其中的第一行代码:
# for magician in magicians:
# 这行代码让Python获取列表magicians 中的第一个值('alice' )，并将其存储到变量magician 中。接下来，Python读取下一行代码:
#  print(magician)
# 它让Python打印magician 的值——依然是'alice' 。鉴于该列表还包含其他值，Python返回到循环的第一行:


# 7.1.2 在 for 循环中执行更多的操作
for magician in magicians:
    print magician.title() + ", that was a great trick!"
    print "\tI can't wait to see your next trick," + magician.title() + ".\n"


# 7.1.3  在 for 循环后执行一些操作
for magician in magicians:
    print magician.title()
print "Thank you."


# 7.2  避免缩进错误
# 7.2.1 忘记缩进 对于位于for 语句后面且属于循环组成部分的代码行，一定要缩进。如果你忘记缩进，Python会提醒你
# 7.2.2 忘记缩进额外的代码行  是一个逻辑错误 。从语法上看，这些Python代码是合法的，但由于存在逻辑错误，结果并不符合预期
# 7.2.3 不必要的缩进   如果你不小心缩进了无需缩进的代码行，Python将指出这一点:
# 7.2.4 循环后不必要的缩进  如果你不小心缩进了应在循环结束后执行的代码，这些代码将针对每个列表元素重复执行。
# 在有些情况下，这可能导致Python报告语法错误，但在大多数情况下，这只会导致逻辑 错误。
# 7.2.5 遗漏冒号  for 语句末尾的冒号告诉Python，下一行是循环的第一行。如果你不小心遗漏了冒号，如❶所示，将导致语法错误



# 8 创建数值列表
# 8.1 使用函数 range()  轻松生成一系列数字 函数range() 让Python从你指定的第一个值开始数，
# 并在到达你指定的第二个值 后停止，因此输出不包含第二个值(这里为5)。
for value in range(1, 5):
    print value


# 8.2  使用 range() 函数创建数字列表
numbers = list(range(1, 6))
print numbers

#  使用 range()时， 还可以指定步长。 例如， 下面的代码打印 1-10 内的偶数
even_numbers = list(range(2, 11, 2))
print even_numbers

# 使用 range() 函数几乎能够创建任何需要的数字集，例如创建一个包含前十个整数平方的列表
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)

print squares

# 8.3 对数字列表执行简单的统计计算
print "min_squares = " + str(min(squares))
print "max_squares = " + str(max(squares))
print "sum_squares = " + str(sum(squares))



# 8.4 列表解析
# 前面介绍的生成列表 squares 的方式包含三四行代码， 而列表解析只需要编写一行代码就能生成这样的列表。
# 而列表解析将 for 循环和创建新元素的代码合并成一行并自动附加新元素。
squs = [val**2 for val in range(1, 11)]
print "squs = " + str(squs)



# 9. 使用列表的一部分
# 9.1 切片---- 处理列表中的部分元素，Python 称之为 切片
# 要创建切片，可指定要使用的第一个元素和最后一个元素的索引。与 range() 函数一样，Python 在到达指定第二个元素索引之前
# 的元素会停止，要输出列表中的前三个元素，需要指定索引 0-3， 这将输出分别为0， 1， 2 的元素
players = ['charles', 'martina', 'martina', 'florence', 'eli']
print players[0:3]

# 列表的第 2-4个元素
print  players[1:4]

# 如果没有指定其实索引，Python 从列表开头开始提取
print players[:4]

# 如果让切片终止于列表末尾，可以使用类似的语法，省略终止索引
print players[2:]

# 使用负索引返会列表末尾相应距离的元素，因此可以输出列表末尾的任何切片
print players[-1:]

# 9.2 便利切片
for player in players[:3]:
    print player.title()



# 9.3 复制列表
# 经常需要根据既有列表创建全新的列表。复制列表的工作原理：
# 要复制列表，可以创建一个包含整个列表的切片，方式是同时省略起始索引和结束索引([:])。 这样就
# 创建一个起始于第一个，终止于最后一个的切片，即复制整个列表
#

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print "My favorite foods are:"
print my_foods

print "\nMy friend's favorite foods are:"
print friend_foods

# 为核实确实有两个列表， 下面在每个列表中添加一种食品，并核实每个列表都记录了相应人所喜欢的食品
my_foods.append('cannoli')
print my_foods

friend_foods.append('ice cream')
print friend_foods

# 倘若只是简单的将 my_foods 赋值给 friend_foods， 就不能得到两个列表



# 10 元组
# 列表非常适合用于存储在程序运行期间可能变化的数据集。列表是可以修改的，然而有时候需要创建一系列不可修改的元素，元组可以满足这种需求。
# Python 将不能修改的值称之为不可变的，而不可变的列表称之为元组。

# 10.1. 定义元组
'''
# 元组看起来犹如列表，但使用圆括号而不是方括号来标识。定义元组后，就可以使用索引来访问元素
# 一个大小不应该改变的矩形，可以将其长度和宽度存储在一个元组中，从而确保它们是不可修改的
'''
dimensions = (200, 50)
print dimensions[0]
print dimensions[1]


# 10.2 遍历元组中的所有值
for dimension in dimensions:
    print dimension


# 10.3 修改元组变量   虽然不能修改元组的元素，但可以给存储元组的变量赋值
dimensions = (400, 100)
print "\nModified dimensions:"
for dimension in dimensions:
    print dimension

















