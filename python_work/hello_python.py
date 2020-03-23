
# 终端退出 python3  使用 exit() 或 Control + D

print("Hello Python world")

name = 'ada lovelace'
print(name.title())

name = 'Ada Lovelace'
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

message = "Hello, " + full_name.title() + "!"
print(message)

 # 字符串中添加制表符
print('\tPython')

print('Languages:\n\tPython\n\tC\n\tJavascript')

# 删除末尾的空白
print(" python ".rstrip())

# 删除开头的空白
favorite_language = " python "
print(favorite_language.lstrip())

favorite_language = " python "
print(favorite_language.strip())

# 使用 str() 避免类型错误
age = 23
message = 'Happy ' + str(age) + 'rd Birthday!'


print(message)


# 列表 list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# 访问列表元素
print(bicycles[0])

# 修改列表元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0]	= 'ducati'
print(motorcycles)

# 在列表中添加元素
motorcycles.append('honda')
print(motorcycles)

# 在列表中插入元素
motorcycles.insert(0, 'ducati')
print(motorcycles)

# 从列表中删除元素
# 1. del
del motorcycles[0] # del 可以删除任何位置处的列表元素，条件知道其索引
print(motorcycles)


# 2. pop 删除最后一个元素，并返回删除元素的值
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# 3. 弹出列表中任何位置的元素
first_owned = motorcycles.pop(0)
print(motorcycles)
print(first_owned)


# 4. 根据值删除元素 方法remove() 只删除第一个指定的值。
#    如果要删除的值可能在列表中出现多次，就需要使用循环来判断是否删除了所有这样的值。

motorcycles.remove('suzuki')
print(motorcycles)


# 组织列表
# 1. 使用 sort() 对列表进行永久性排序  按字母顺序排列
cars = ['bow', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# 2. 按字母顺序相反顺序排列元素
cars.sort(reverse=True)
print(cars)


# 3. 使用 sorted() 对列表进行临时排序
cars  = ['bow', 'audi', 'toyota', 'subaru']
print('Here is the original list:')
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the reverse sorted list:")
print(sorted(cars, reverse=True))


print("\nHere is the original list again:")
print(cars)


# 4. 反向打印列表
cars.reverse()
print(cars)


# 5. 确定列表的长度
print(len(cars))



# 使用列表时避免索引错误
# 1. 例如只包含三个元素的列表，却要求获取第四个元素
# 2. 每当需要访问最后一个列表元素时，都可以使用索引-1. 仅当列表为空时，这种访问会出新错误
#    不知道列表长度的情况下最后一个元素索引为 -1， -2 是倒数第二个元素，以此列推
print(cars[-1])



# 操作列表
# 1. 遍历列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)

# 1.1 在 for 循环结束后执行一些操作
#     在 for 循环后，没有缩进的代码都只执行一次，而不会重复执行
for magician in magicians:
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title() +  ".\n")

print('Thank you, everyone. That was a great magic show!')


# 2. 避免缩进错误
# 2.1. 忘记缩进： 对于位于 for 语句后面且属于循环组成部分的代码行，一定要进行缩进
# 2.2. 忘记缩进额外的代码： 试图在循环中执行多项任务，却忘记缩进其中的一些代码行
# 2.3. 不必要的缩进： 缩进无需缩进的代码行
# 2.4. 循环后不必要的缩进： 如果不小心缩进了应该循环结束后执行的代码，这些代码将针对每个列表元素重复执行
# 2.5. 遗漏了冒号： for magician in magicians


# 3. 创建数值列表
# 3.1 使用 range() 函数： 生成一系列的数字, 打印 1~4，需要使用 range(1,5)
for value in range(1, 5):
	print(value)

# 3.2 使用 range() 创建数字列表  使用函数 list（） 将 range() 的结果直接转换成列表
numbers = list(range(1, 6))
print(numbers)

#      使用 range() 还可指定步长 
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# 3.3 对数字列表执行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))

print(max(digits))

print(sum(digits))


# 3.4 列表解析
# 列表解析： 将 for 循环和创建新元素的代码合并成一行，并自动附加新元素
squares = [value**2 for value in range(1, 11)]
print(squares)


# 4. 使用列表的一部分
# 4.1. 切片： 要创建切片，可指定要使用的第一个元素和最后一个元素。要输出列表中的前三个元素，需要指定索引0~3
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print(players[1:4])

print(players[:4]) # 如果没有指定第一个索引，Python自动从列表开头开始

print(players[2:]) # 如果没有指定终止索引，默认终止于列表结尾

print(players[-3:]) # 负数索引返回离列表末尾相应距离的元素


# 4.2 遍历切片
print("Here are the first three player on my team:")
for player in players[:3]:	
	print(player.title())

# 4.3 复制列表
#     要复制列表，可以创建一个包含整个列表的切片，方法是：同时省略起始索引和终止索引（[:]）
#     若只是简单的赋值，则两个变量指向同一个列表

my_foods = ['pizza', 'falafel', 'corrot cake']
frient_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(frient_foods)

#     为核实确实有两个列表，将每个列表中都添加一种食物 
my_foods.append('cannoli')
frient_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("My friend's favorite foods are:")
print(frient_foods)



# 5.元组
#     列表非常适合存储在程序运行期间可能变化的数据集。列表是可以修改的
#     Python 将不能修改的值称为不可变的，而不可变的列表称为元组
#  5.1. 定义元组    使用圆括号表示 
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# 5.2. 遍历元组中的所有值
for dimension in dimensions:
	print(dimension)

# 5.3  修改元组变量   
dimensions = (400, 100) # 虽然不能修改元组的元素，但可以给存储元组的变量赋值
print("\nModified dimensions:")
for dimesion in dimensions:
	print(dimesion)

















