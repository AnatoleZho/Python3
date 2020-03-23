'''
异常 是 Python创建的特殊对象，用于管理程序运行时出现的错误。
'''

# 1. 从文件中读取数据
'''
文本文件可存储在数据量多得难以置信：天气数据、交通数据、社会经济数据、文学作品等。
每当需要分析或修改存储在文件中的信息时，读取文件都很有用，对数据分析应用程序也有其
如此.例如，可以编写一个程序：读取一个文本文件内容，重新设置这些数据的格式并将其写入文件，
让浏览器能够显示这些内容。

需要使用文本文件中的信息，首先需要将信息读取到内存中。为此，可以一次读取文件的全部内容，
也可以以每次一行的方式逐步读取。
'''

# 1.1 读取整个文件
'''
创建一个文件，它包含精确到小数点后30位的圆周率值，且在小数后每10位出都换行
将其保存在 pi_digits.txt 中
'''

# 打开并读取这个文件，将其内容显示到屏幕上：
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)

'''
1. 函数 open() 接受一个参数：要打开的文件的名称。Python 在当前执行的文件目录中
   查找指定的文件。
   函数 open() 返回一个表示文件的对象。Python 将这个对象存储在将在后面使用的变量中。

2. 关键字 with 在不再需要访问文件后将其关闭。这个程序中，注意到调用了 open() 函数，
   但并没哟调用 close() 函数；也可以调用 open() 和 close() 来打开和关闭文件，但
   这样做时，如果程序存在 bug，导致 close() 语句未执行，文件将不会关闭。未妥善关闭
   文件可能会导致数据丢失或受损。如果在程序中过早地调用 close(),会发现需要使用文件时
   它已关闭（无法访问），导致更多错误。通过使用 with，自己只管打开文件，并在需要时使用它，
   Python 自会在合适的时候自动将其关闭。

3. 使用 read() 函数读取文件的全部内容，并将其作为一个长长的字符串存储在变量 contents 中，
   这样通过打印 contents 的值，就可将这个文本文件的全部内容显示出来。
'''


# 1.2 文件路径
'''
当将类似于 pi_digits.txt 这样的简单文件名传递给函数 open() 时，Python 将在当前执行的文件
（file_error.py） 所在的目录中查找文件。

根据自己组织文件的方式，有时要打开不在程序文件所属目录中的文件。
要让 Python 打开不与程序文件位于同一个目录中的文件，需要提供文件路径，它让 Python 到
系统特定位置去查找。

可使用相对文件路径来打开文件夹中的文件。相对文件路径将让 Python 到指定的位置去查找，
而该位置是相对于当前运行的程序所在目录的。如：
with open('text_files/filename.txt') as file_object:

还可以将文件在计算机中的精确位置告诉 Python，这样就不用关心当前运行的程序存储在什么地方。
称为 绝对文件路径。在相对路径行不通时，可使用绝对路径。如：
file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
with open(file_path) as file_object:

通过使用绝对路径，可读取系统任何地方的文件。就目前而言，最简单的做法是，要么将数据文件存储在
程序文件所在的目录，要么将其存储在程序文件所在目录下的一个文件中
'''


# 1.3 逐行读取
'''
读取文件时，常常需要检查其中的每一行：可能要在文件找那个查找特定的信息，或者要以某种方式
修改文件的文本。
'''
# 要以每次一行的方式检查文件，可对文件对象使用for 循环：
filename = 'pi_digits.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())   # 出现空白行？ 因为在这个文件正，每行的末尾都一个看不见的换行符，使用 rstrip() 函数



# 1.4 创建一个包含文件各行内容的列表
'''
使用关键字 with 时，open() 返回的文件对象只在 with 代码块内可用。如果要在 with 代码块外访问文件的内容，
可在代码块内将文件的各行存储在一个列表中，并在 with 代码块外使用该列表：可以立即处理文件的各部分，
也可推迟到程序后面再处理。
'''
filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines() # readlines() 从文件中读取每一行，并将其存储在列表中

for line in lines:
	print(line.rstrip())


# 1.5  使用文件的内容
filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))


# 1.6 包含一百万位的大型文件
'''
对于可以处理的数据量， Python 没有任何限制，只要系统内存足够多。
'''


# 2. 写入文件
'''
保存数据的最简单的方式之一是将其写入到文件中。通过将输出写入文件，即便关闭
包含程序输出的终端窗口，这些输出也依然存在：可以在程序结束运行后查看这些输出，
可以与别人分享输出的文件，还可编写程序来将这些输出读取到内存中并进行处理
'''

# 2.1 写入空文件
'''
要将文本写入文件，在调用 open() 需要提供另一个实参，告诉 Python 要写入打开
的文件。为明白其中的工作原理，来讲一条简单的消息存储到文件中。
'''
filename = 'programing.txt'

with open(filename, 'w') as file_object:
	file_object.write('I love programing.')
    

'''
调用 open() 时提供两个实参。第一个实参也是要代开的文件的名称；
第二个实参('w')告诉 Python，要以写入模式打开这个文件。
打开文件时，可指定读取模式('r')、写入模式('w')、附加模式('a')
或能够读取和写入文件的模式('r+').如果省略了模式实参，Python 
将以默认的只读模式打开文件。

如果要写入的文件不存在，函数 open() 将自动创建它。然而，以写入
('w')模式打开文件时千万要小心，因为如果指定的文件已经存在，Python
将在返回文件对象前清空该文件。

Python只能将字符串写入文本文件。要将数值数据存储到文本文件中，
必须先使用函数 str() 将其转换为字符串格式。
'''


# 2.2 写入多行
'''
函数 write() 不会再写入的文本末尾添加换行符，因此如果写入多行时
没有指定换行符，文件看起来可能不是希望的那样
'''
filename = 'programing.txt'

with open(filename, 'w') as file_object:
	file_object.write('I love programing.')
	file_object.write('I love creating new games.')

# 要让每个字符串都独占一行，需要在 write() 语句中包含换行符：
filename = 'programing.txt'

with open(filename, 'w') as file_object:
	file_object.write('I love programing.\n')
	file_object.write('I love creating new games.\n')



# 2.3 附加到文件
'''
如果要给文件添加内容，而不是覆盖原有的内容，可以附加模式打开文件。
以附加模式打开文件时，Python 不会在返回文件对象前清空文件，而写入到文件的行
都将添加到文件末尾。如果指定的文件不存在，Python 将会创建一个空文件
'''

filename = 'programing.txt'

with open(filename, 'a') as file_object:
	file_object.write('I also love finding meaning in large datasets.\n')
	file_object.write('I lova creating apps that can run in a browser.\n')



# 3. 异常
'''
Python使用被称为异常的特殊对象，来管理程序执行期间发生的错误。每当发生让 Python 不知所措
的错误时，它都会创建一个异常对象。如果编写处理该异常的代码，程序将继续运行；如果未对异常进行
处理，程序将停止，并显示一个 traceback， 其中包含有关异常的报告。

异常时使用 try-except 代码块处理的。try-except 代码块让Python执行指定的操作，
同时告诉Python发生异常时怎么办。使用了 try-except 代码块时，即便出现异常，程序
也能继续运行：显示编写的友好的错误消息，而不是令用户迷惑的 traceback。

'''

# 3.1 处理 ZeroDivisionError 异常
#  print(5/0)

'''
错误 ZeroDivisionError 是一个异常对象。 Python 无法按要求做时，就会创建
这种对象。在这种情况下，Python 将停止运行程序，并指出引发了哪种异常，而我们
可根据这些信息对程序进行修改。
'''

# 3.2 使用 try-except 代码块
try: 
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")


# 3.3 使用异常以免崩溃


# 3.4 else 代码块
'''
通过将可能引发错误的代码放在 try-except 代码块找那个，可提高这个程序抵御错误的
能力。
此外还有一个 else 代码块，依赖于 try 代码块成功执行的代码都应放到 else 代码块中
'''

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number:")
	if first_number == 'q':
		break
	second_number = input("Second_number:")
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by 0!")
	else:
		print(answer)

'''
try-except-else 代码块的工作原理大致如下：Python 尝试执行 try 代码块中的代码；
只有可能引发异常的代码才需要放在 try 语句中。有时候，有一些仅在 try 代码块成功
执行时才需要运行的代码；这代码应放在 else 代码块中。except 代码块告诉 Python，
如果它尝试运行 try 代码块中的代码是引发了指定的异常该怎么办。
'''

# 3.5 处理 FileNotFoundError 异常
'''
使用文件时，一种常见的问题是找不到文件：要查找的文件可能在其他地方、文件名可能
不正确、这个文件根本就不存在。对于所有这些情形，都可以使用 try-except代码块以
直观的方式进行处理。
'''

filename = 'alice.txt'

try:
	with open(filename) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = "Sorry, the file " + filename + ' does not exists.'
	print('msg')


# 3.6 分析文本
'''
可以分析包含整本书的文本文件。很多经典文学作品都是以简单文本文件的方式提供的，
因为它们不受版权限制。
'''
# 尝试计算含有多少个单词  使用方法 split()
filename = 'alice.txt'

try:
	with open(filename) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = "Sorry, the file " + filename + ' does not exist.'
	print(msg)
else:
	# 计算文件大致包含多少个单词
	words = contents.split()
	num_words = len(words)
	print("THe file " + filename + " has about" + str(num_words) + " words.")



# 3.7 使用多个文件
def count_words(filename):
	'''计算一个文件大致包含多少个单词'''
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
		except FileNotFoundError:
			msg = "Sorry, the file " + filename + " does not exist."
			print(msg)
		else:
			'''计算文件大致包含多少个单词'''
			words = contents.split()
			num_words = len(words)
			print("The file ") + filename + ' has about ' + str(num_words) + " words."

filename = 'alice.txt'
count_words(filename)


filenames = ['alice.txt', 'siddartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
	count_words(filename)


# 3.8 失败时一声不吭
'''
在 except 代码块中明确地告诉Python什么都不要做。Python 有一个 pass 语句，可在
代码块中使用它，来让 Python什么都不要做
'''


# 3.9 决定报告哪些错误
'''
在什么情况下向该用户报告错误？在什么情况下又应该在失败时不吭一声？如果用户知道分析哪些文件，
他们可能希望在有文件没有分析时出现一条消息，将其中的原因告诉他们。如果用户只想看到结果，
而并不知道要分析哪些文件，可能就需在有些文件不存在时告诉他们。向用户显示他不想看到的信息
可能降低程序的可用性。Python的错误处理结构能够细致地控制与用户分享错误信息的程度。

编写得很好且经过详尽测试的代码不容易出现内部错误，如语法或逻辑错误，但只要程序依赖于外部
因素，如用户输入、存在指定的文件、有网络链接，就有可能出现异常。凭借经验可判断该在程序的
什么地方包含异常处理块，以及出现错误时该向用户提供多少相关的信息。
'''


# 4. 存储数据
'''
程序都把用户提供的信息存储在列表和字典等数据结构中。用户关闭程序时，几乎总是要保存他们提供
的信息，一种简单的方式是使用模块 json 来存储数据。

模块 json 能够将简单的 Python 数据结构转储到文件中，并在程序再次运行时加载该文件中的数据。
还可以使用 json 在 Python 程序间分项数据。更重要的是，JSON 数据格式并非Python专用的，
这样能够将以 JSON 格式存储的数据与使用其他编程语言的人分享。
'''

# 4.1 使用 json.dump() 和 json.load()
'''
函数 json.dump() 接受两个实参：要存储的数据以及可用于存储数据的文件对象
'''
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
	json.dump(numbers, f_obj)

'''
先导入模块 json， 再创建一个数字列表。指定了要将该数字列表存储到其中的文件的名称。
通常使用文件扩展名 .json 来指出文件存储的数据为 JSON 格式。接下来，以写入模式打开
这个文件，让 json能够将数据写入其中。使用函数 json.dump() 将数字列表存储到文件
numbers.json 中。
'''

# 在编写一个程序，使用 json.load() 将这个列表读取到内存中：
filename = 'numbers.json'
with open(filenam) as f_obj:
	numbers = json.load(f_obj)

print(numbers)


# 4.2 保存和读取用户生成的数据
'''
对于用户生成的数据，使用 json 保存它们大有裨益，因为如果以某种方式进行存储，等程序
停止运行时用户的信息将丢失。
'''
# 存储用户的名字
username = input('What is your name?')

filename = 'username.json'
with open(filename, 'w') as f_obj:
	json.dump(username, f_obj)
	print("We'll remember you when you come back, " + username + '!')


filename = 'username.json'

with open(filename) as f_obj:
	username = json.load(f_obj)
	print("Welcome back, " + username + "!")


#两个程序合并到一个程序中
filename = 'username.json'

try:
	with open(filename) as f_obj:
		username = json.load(f_obj)
except FileNotFoundError:
	username = input("What is your name?")
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
		print("We'll remember you when you come back, " + username + "!")
else:
	print("Welcome back, " + username + "!")


# 4.3 重构
'''
代码能够正确地运行，但可做进一步的改进----将代码划分为一系列完成具体工作的函数。
这样的过程被称为重构。重构让代码更清晰、更易于理解、更容易扩展。
'''
def get_stored_username():
	'''如果存储了用户名，就获取它'''
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
		except FileNotFoundError:
			return None
		else: 
			return username

def get_new_username():
	'''提示用户输入用户名'''
	username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
    	json.dump(username, f_obj)
    return username

def greet_user():
	'''问候用户，并指出其名字'''
	username = get_stored_username()
	if username:
		print("Welcome back, " + username + "!")
	else:
		username = get_new_username()
		print("We'll remember you when you come back, " + username + "!")

greet_user()












