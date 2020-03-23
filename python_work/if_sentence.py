# if 语句

# 1. 简单示例
cars = ["audi", 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

# 2.条件测试
# 2.1. 检查是否相等 ==
# 2.2. 检查是否相等时区分大小写  
# 2.3. 检查是否不等 !=
# 2.4. 比较数字
# 2.5. 检查多个条件  使用 and 检查多个条件    使用 or 检查多个条件
# 2.6. 检查特定值是否包含在列表中
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)

# 2.7. 检查特定值是否不包含在列表中
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
	print(user.title() + ", you can post a response if you wish.")

# 5.2.8 布尔表达式     game_active = True   can_edit = False


# 3. if语句
# 3.1. 简单 if 语句
age = 19
if age >= 18:
	print('You are old enough to vote!')

# 3.2. if-else 语句
age = 17 
if age >= 18:
	print("You are old enough to vote!")
else:
	print("Sorry, you are too young to vote.")


# 3.3.  if-elif-else结构
age = 12
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $5.")
else: 
	print("Your admission cost is $10.")

age = 12
if age < 4: 
	price = 0
elif age < 18:
	price = 5
else:
	price = 10

print("Your admission cost is $" + str(price) + ".")


# 3.4 使用多个 elif 代码块
age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
else:
	price = 5

print("YOur admission cost is $" + str(price) + '.')


# 3.5. 省略 else 代码块
age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
elif age >= 65:
	price = 5

print("Your admission cost is $" + str(price) + ".")


# 4. 使用 if 语句处理列表
# 4.1 检查特殊元素
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	print('Adding' + requested_topping + '.')

print("\nFinished making you pizza!")


for requested_topping in requested_toppings:
	if requested_topping == "green peppers":
		print("Sorry, we are out of green peppers right now.")
	else:
		print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")


# 4.2. 确定列表不是空的
requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + ".")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")


# 4.3. 使用多个列表
avaliable_toppings = ['mushrooms', 'olives', 'green_peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'frech fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in avaliable_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we don't have " + requested_topping + '.')

print("\nFinished making your pizza!")


