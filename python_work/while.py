
# 在终端中运行： 1. cd 到当前程序的所在目录 2. 输入 python3 while.py 然后回车


# 1. 函数 input() 的工作原理
#       函数 input() 让程序暂停运行，等待用户输入一些文本。获取用户输入后吗， Python将其存储在一个变量中，以方便实用


message = input('Tell me something, and I will repeat it back to you:')
print(message)

# 1.1 编写清晰的应用程序
name = input('Please enter your name: ')
print('Hello, ' + name + '!')

# 1.2 使用 int() 来获取数值输入
age = input('How old are you? ')
age = int(age)

print(age >= 18)


height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
	print("\nYou're tall enough to ride!")
else:
	print("\nYou'll be able to ride when you're a little older.")

# 1.3 求模运算符
mod = 4 % 3
print(mod)


number = input("Enter a number, and I'll tell you if it's even or odd:")
number = int(number)

if number % 2 == 0:
	print("\nThe number " + str(number) + ' is envn.')
else:
	print("\nThe number " + str(number) + ' is odd.')


# 2. while 循环
current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1

# 2.1 让用户选择何时退出
prompt = '\nTell me something, and I will repeat it back to you: '
prompt += "\nEnter 'quit' to end the program."
message = ""

while message != 'quit':
	message = input(prompt)
	print(message)

# 2.2 使用标志
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
	message = input(prompt)

	if message == 'quit':
		active = False
	else:
		print(message)


# 2.3 使用 break 退出循环
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
	city = input(prompt)

	if city == 'quit':
		break
	else:
		print("I'd love to go to " + city.title() + '!')


# 2.4 在循环中使用 continue 
#         要返回到循环开头，并根据条件测试结果决定是否继续执行循环， 可使用 continue 语句
current_number = 0
while current_number <= 10:
	current_number += 1
	if current_number % 2 == 0:
		continue

	print(current_number)

# 2.5  避免无限循环

# 3. 使用 while 循环来处理列表和字典
#        for 循环是一种遍历列表的有效方式，但在 for 循环中不应该修改列表，否则将导致 Python 难以跟踪其中的元素。
#        要在遍历列表的同时对其进行修改，可以使用 while 循环
# 3.1 在列表之间移动元素

# 首先，创建一个待验证用户列表和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 验证每个用户，直到没有未验证的用户为止
# 将每个经过验证的用户都移动到已验证用户列表中
while unconfirmed_users:
	current_user = unconfirmed_users.pop()

	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)

# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())


# 3.2 删除包含特定值的所有列表的元素
pets = ['dog', 'cat', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')

print(pets)


# 3.3 使用用户输入来填充字典
responses = {}
# 设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
	# 提示输入被调查者的名字和回答
	name = input("\nWhat is your name? ")
	response = input("which mountain would you like to climb someday?")

	# 将答卷存储在字典中
	responses[name] = response

	# 看看是否还有人要参加调查
	repeat = input("Would you like to let another person respond? (yes/ no) ")
	if repeat == 'no':
		polling_active = False

# 调查结束，显示结果
print('\n--- Poll Results ---')
for name, response in responses.items():
	print(name + ' would like to climb ' + response + ".")









