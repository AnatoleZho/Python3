'''
Python 模块 unittest 中的工具来测试代码
将学习编写测试用例，核实一系列输入都将得到预期的输出。将看到测试通过了是什么样子，
测试未通过又是什么样子，还将知道测试未通过如何有助于改进代码。
将学习如何测试函数和类，并将知道该为项目编写多少个测试。
'''

# 1. 测试函数

# 1.1 单元测试和测试用例
'''
Python 标准库中的模块 unittest 提供了代码测试工具。单元测试用于核实函数的
某个方面没有问题；测试用例是一组单元测试，这些单元测试一起核实函数在各种情形
下的行为都符合要求。良好的测试用例考虑到函数可能收到的各种输入，包含针对所有
这些情形的测试。全覆盖式测试 用例包含一整套单元测试，涵盖了各种可能的函数使
用方式。对于大型项目，要实现全覆盖可能很难。通常最初只要针对代码的重要行为
编写测试即可，等项目被广泛使用时在考虑全覆盖。
'''

# 1.2 可通过的测试
'''
创建测试用例的语法需要一段时间才能习惯，但是测试用例创建后，再添加针对函数的
的单元测试就很简单了。要为函数编写测试用例，可先导入模块 unittest 以及要
测试的函数，再创建一个集成 unittest.TestCase 的类，并编写一系列方法对
函数行为的不同方面进行测试。
'''

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	'''测试 name_function.py'''

	def test_first_last_name(self):
		'''能够正确地处理像Janis Joplin 这样的名字吗？'''
		formatted_name = get_formatted_name("janis", "Joplin")
		self.assertEqual(formatted_name, "Janis Joplin")

	def test_first_last_middle_name(self):
		'''能够正确地处理像Wolfgang Amadeus Mozart 这样的姓名吗'''
		formatted_name = get_formatted_name('Wolfgang', 'mozart', 'amadeus')
		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

# unittest.main()
'''
首先，导入了模块 unittest和要测试的函数 get_formatted_name().创建爱你了一个名为
NamesTestCase 的类，用于包含一系列针对get_formatted_name() 的单元测试。可随便给
这个类命名，但最好让它看起来与要测试的函数相关，并包含字样Test。这个类必须继承自
unittest.TestCase 类，这样 Python才知道如何运行编写的测试。

NamesTestCase 包含一个方法，用户测试 get_formatted_name() 的一个方面。将这个方法
命名为test_first_last_name(),因为要核实的只有名和姓能否被正确地格式化。运行该测试
程序时，所有以test打头的方法都将自动运行。在这个方法中，调用了要测试的函数，并存储了
要测试的返回值。
然后使用 unittest 类最有用的功能之一：一个断言方法。断言方法用来核实得到的结果是否
与期望的结果一致。在这里 get_formatted_name() 应该返回这样的名字，即名和姓的首字母
为大写，且他们之间有一个空格，因此期望 formatted_name 的值为 Janis Joplin。
为检查是否确实如此，调用 unittest 的方法 assertEqual(),并向它传递 formatted_name
和 'Janis Joplin'. 代码行 self.assertEqual(formatted_name, 'Janis Joplin'）

'''

# 1.3  不能通过的测试
#  修改 get_formatted_name() 函数
'''
运行单元测试，最后还看到了一条消息，它指出整个单元测试未通过，因为运行该测试用例时
发生了一个错误。这条消息位于输出末尾，让你一眼就能看到。
'''


# 1.4  测试未通过时该怎么办
'''
如果检查的条件没错，测试通过了意味着函数的行为是对的，而测试未通过意味着编写
新的代码有错。因此，测试未通过时，不要修改测试，而应该修复导致测试不通过的代码：
核对刚对函数所做的修改，找出导致函数行为不符合预期的修改。
'''


# 1.5  添加新测试


# 2. 测试类
'''
前面编写的是针对单个函数的测试，下面针对类的测试。如果针对类的测试通过了，
就能确信对类所做的改进信息没有意外地破坏其原有的行为。
'''

# 2.1 各种断言方法
'''
Python在 unittest.TestCase 类中提供了很多断言方法。断言方法检查你认为
应该满足的条件或是否确实满足。如果该条件确实满足，则对程序行为的假设就得到
了确认，就可以确信其中没有错误。如果认为应该满足的条件，实际上并不满足，
Python将引发异常。

6中常用的断言方法。使用这些方法可以核实返回的值等于或不等于预期的值、返回
的值为 True或False、返回的值在列表中或不在列表中。只能在继承unittest.TestCase
的类中使用这些方法：

assertEqual(a,b)
assertNotEqual(a,b)
assertTrue(x)
assertFalse(x)
assertIn(item, list)
assertNotIn(item,list)

'''

# 2.2 一个要测试的类
from survey import AnonymousSurvey

# # 定义一个问题，并创建一个表示调查的 AnonymousSurvey 对象
# question = "What language did you first learn to speak? "
# my_survey = AnonymousSurvey(question)

# # 显示问题并存储答案
# my_survey.show_question()
# print("Enter 'q' at any time to quit.\n")
# while True:
# 	response = input("Language")
# 	if response == 'q':
# 		break
# 	my_survey.store_response(response)

# # 显示调查结果
# print("\nThank you to everyone who participated in the survey!")
# my_survey.show_results()


# class TestAnomyousServey(unittest.TestCase):
# 	'''针对 A农业noUSServey 类的测试'''

# 	def test_store_single_response(self):
# 		'''测试单个答案会被妥善地存储'''
# 		question = "What language did you first learn to speak?"
# 		my_survey = AnonymousSurvey(question)
# 		my_survey.store_response("English")

# 		self.assertIn("English", my_survey.responses)

# 	def test_store_three_responses(self):
# 		'''测试三个答案会被妥善地存储'''
# 		question = 'What language did you first learn to speak?'
# 		my_survey = AnonymousSurvey(question)
# 		responses = ["English", 'Spanish', 'Mandarin']
# 		for response in responses:
# 			my_survey.store_response(response)

# 		for response in responses:
# 			self.assertIn(response, my_survey.responses)


# unittest.main()


# 2.4 方法 setUp()
'''
在前面的 test_survey.py 中，在每个测试方法中都创建了一个 AnonymousSurvey
实例，并且每个方法中都创建了答案。unittest.TestCase 类包含方法 setUp()
让我们只需创建这些对象一次，并在每个测试方法中使用它们。如果在 TestCase 类
中包含了方法 setUp()， Python 将先运行它，再运行各个以 test_ 打头的方法。
这样，在编写的每个测试方法中都可以使用在方法 setUp() 中创建的对象。
'''

class TestAnonymousSurvey(unittest.TestCase):
	'''针对 AnonymousSurvey 类的测试'''

	def setUp(self):
		'''创建一个调查对象和一组答案，供使用的测试方法使用'''
		question = 'What language did you first learn to speak?'
		self.my_survey = AnonymousSurvey(question)
		self.responses = ["English", 'Spanish', 'Mandarin']

	def test_store_single_response(self):
		'''测试单个答案会被妥善地存储'''
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0], self.my_survey.responses)

	def test_store_three_responses(self):
		'''测试三个答案会被妥善地存储'''
		for response in self.responses:
			self.my_survey.store_response(response)

		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)

	unittest.main()

'''
方法 setUp() 做了两件事：创建一个调查对象；创建一个答案列表。
存储这两个变量名包含前缀 self，因此可在类的任何地方使用。这让两个测试方法
都更加简单，因为它们不用创建调查对象和答案。

测试自己编写的类时，方法 setUp() 让测试方法编写起来更容易：可在 setUp()
方法中创建一系列实例并设置它们的属性，再在测试方法中直接使用这些实例。
'''



















