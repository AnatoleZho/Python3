#  类
# 1. 创建和使用类
# 1.1 创建 Dog 类
class Dog():   # Python 中约定 首字母大写的名称指定为类
	'''一次模拟小狗的简单尝试'''

	def __init__(self, name, age):
		'''初始化属性name和age'''
		self.name = name
		self.age = age

	def sit(self):
		'''模拟小狗被命令时蹲下'''
		print(self.name.title() + 'is now sitting.')

	def roll_over(self):
		'''模拟小狗被命令时打滚'''
		print(self.name.title() + ' rolled over!')

# 1.1.1 方法 __init__()
'''
类中的函数称为方法；__init__() 是一种特殊的方法，每当根据 Dog 类创建新实例时，Python 都会自动运行它。
开头和末尾有两个下划线，这是一种约定，旨在避免 Python 默认方法与普通方法发生名称冲突
__init__() 方法定义成了包含三个形参： self、name 和 age。 在方法定义中，形参 self 必不可少，还必须位于其他形参的前面
因为 Python 调用这个 __init__() 方法来创建 Dog 实例时，将自动传入实参 self。 每个与类相关联的方法调用都自动传入实参 self
它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。
创建 Dog 实例时，Python 将调用 Dog 类的方法 __init__().将通过实参向 Dog() 传递名称和年龄；self 会自动传递
因此不需要传递它。每当根据 Dog 类创建实例时，都只需要最后两个形参（name 和 age ）提供值。

'''

# 1.2 根据类创建实例
'''可将类视为有关如何创建实例的说明，Dog 类是一系列说明，让 Python 知道如何创建表示特定小狗的实例'''
my_dog = Dog('willie', 6) #通常可以认为首字母大写的名称指的是类，而小写的名称指的是根据类创建的实例

print("My dog's name is " + my_dog.name.title() + '.')
print("My dog  is " + str(my_dog.age) + 'years old.')

# 1.2.1 访问属性
'''要访问实例的属性，可使用句点表示法。'''
print(my_dog.name.title())

# 1.2.2 调用方法
'''根据 Dog 类创建实例后，就可以使用句点表示法来调用 Dog 类中定义的任何方法'''
my_dog.sit()
my_dog.roll_over()


# 1.2.3 创建多个实例
my_dog = Dog("willie", 6)
your_dog = Dog('lucy', 3)


# 2. 使用类和实例
# 2.1 Car 类
class Car():
	'''一次模拟汽车的简单尝试'''

	def __init__(self, make, model, year):
		'''初始化描述汽车的属性'''
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		'''返回整洁的描述性信息'''
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		'''打印一条指出汽车里程的消息'''
		print("This car has " + str(self.odometer_reading) + ' miles on it.')

    
	def update_odometer(self,mileage):
		'''将里程表读数设置为指定的值'''
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		'''将里程表读数增加指定的量'''
		self.odometer_reading += miles

	def fill_gas_tank(self):
		'''将油箱加满油'''
		print('This car tank is full.')


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())


# 2.2 给属性指定默认值
my_new_car.read_odometer()


# 2.3 修改属性的值
'''可以以三种不同的方式修改属性的值: 直接通过实例进行修改； 通过方法进行设置；通过方法进行递增（增加特定的值）'''

# 2.3.1 直接修改属性的值
my_new_car.odometer_reading = 23
my_new_car.read_odometer()


# 2.3.2 通过方法修改属性的值
my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_new_car.update_odometer(11)
my_new_car.read_odometer()


# 2.3.3 通过方法对属性值进行递增
my_new_car.increment_odometer(100)
my_new_car.read_odometer()


# 3. 继承
'''
一个类继承另一个类时，它将自动获得另一个类的所有属性和方法
原有的类称为父类，而新类称为子类。子类继承了其父类的所有属性和方法，同时还可以定义自己属性和方法
'''


# 3.1 子类的方法 __init__()
'''
创建子类实例时，Python 首先需要完成的任务是给父类的所有属性赋值
创建 ElectricCar 类 继承自 Car 类
'''
class ElectricCar(Car):
	'''电动汽车的独特之处'''

	def __init__(self, make, model, year):
		'''初始化父类的属行'''
		super().__init__(make, model, year)
		self.battery = 70

	def describe_batery(self):
		'''打印一条描述电瓶容量的信息'''
		print('This car has a ' + str(self.battery_size) + '-kWh battery.')

	def fill_gas_tank(self):
		'''电动汽车没有油箱'''
		print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

'''
1. 创建子类时，父类必须包含在当前文件中，且位于子类前面。
2. 定义子类时，必须在括号内指定父类的名称
3. supper() 是一个特殊函数，帮助 Python 将父类和子类关联起来。
   super().__init__(make, model, year)让子类包含父类的所有属性
'''

# 3.2 给子类定义属行和方法
'''让一个类继承自另一个类后，可以添加区分子类和父类所需的新属性和方法'''
my_tesla.describe_batery()
my_tesla.read_odometer()


# 3.3 重写父类的方法
'''
对于父类的方法，只要它不符合子类模拟的实物的行为，都可以对其进行重写。为此，
可在子类中定义一个这样的方法，即它与要重写的父类方法同名。这样 Python 将不会考虑这个父类的方法
而只关注在子类中定义的相应方法
'''
my_tesla.fill_gas_tank()


# 3.4 将实例用作属性
class Battery():
	'''一次模拟电动汽车电瓶的简单尝试'''

	def __init__(self, battery_size=70):
		'''初始化电瓶的属行'''
		self.battery_size = battery_size

	def describe_berrery(self):
		'''打印一条描述电瓶容量的消息'''
		print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
    	'''打印一条消息， 指出电瓶的续航里程'''
    	if self.battery_size == 70:
    		range = 240
    	elif self.battery_size == 85:
    		range = 270

    	message = 'This car can go approximately ' + str(range)
    	message +=" miles on a full charge."
    	print(message)

# class ElectricCar(Car):
# 	'''电动汽车的独特之处'''

# 	def __init__(self, make, model, year):
# 		'''初始化父类的属行'''
# 		super().__init__(make, model, year)
# 		self.battery = Battery()



# 4. 导入类
'''
Python 允许将类存储在模块中，然后在主程序中导入所需的模块
'''
# 4.1 导入单个类
'''
下面来创建一个只包含 Car 类的模块。这让我们面临一个微妙的命名问题：在本章中已有一个名为 car.py
的文件，但是这个模块也应命名为 car.py ，因为它包含表示汽车的代码。
将这样解决这个命名问题：将 Car 类存储在一个名为 car.py 的模块中，该模块将覆盖前面使用的文件 car.py.
从现在开始使用该模块的程序都必须使用更具体的文件名，如 my_car.py
'''
from car import Car

new_car = Car("audi", 'a4', 2016)
print(new_car.get_descriptive_name())

new_car.odometer_reading = 23
new_car.read_odometer()


# 4.2 在一个模块中存储多个类
'''虽然同一个模块中的类之间应存在某种相关性，但是可根据需要在一个模块中存储任意数量的类'''
from car import ElectricCar


# 4.3 从一个模块中导入多个类
from car import Car, ElectricCar


# 4.4 导入整个模块
'''
可以导入整个模块，再使用句点表示法访问需要的类。这种导入方法很简单，代码也易于阅读。
由于创建类实例的代码都包含模块名，因此不会与当前文件内使用的任何名称发生冲突
'''
import car

my_beetle = car.Car('volkswagen', 'beetle', 2016)


# 4.5 导入模块中的所有类
'''
导入模块中的每个类，可以使用下面的语法：
from module_name import *
不推荐使用这种导入方式，原因有二：
首先，如果只要看一下文件开头的 import 语句，就能清楚地知道程序使用了哪些类，将大有裨益；
这种导入方式还可能引发名称上的困惑。如果不小心导入了一个与程序文件中其他东西同名的类，将引发难以诊断的错误

要从一个模块中导入很多类时，最好导入整个模块，并使用 module_name.class_name 语法来访问
这样做时，虽然文件开头并没有列出用到的所有类，但是清楚地知道在程序的哪些地方使用了导入的模块；
还避免了导入模块中的每个类可能引发的名称冲突
'''

# 4.6 在一个模块中导入另一个模块
'''
有时候需要将类分散在多个模块中，以免模块太大，或在同一个模块中存储不相关的类。
将类存储在多个模块中时，可能会发现一个模块中的类依赖另一个模块中的类，
在这种情况下，可在前一个模块中导入必要的类

例如，将 Car 类存储在一个模块中，并将 ELectricCar 和 Bettery 类存储在另一个模块中。
将第二个模块命名为 eLectric_car.py 
ElectricCar 类需要访问其父类 Car， 因此直接将 Car 类导入该模块中。
如果忘记导入，Python 将在试图创建 ELectricELectricCar 实例时引发错误。
现在可以分别从每个模块中导入类，以根据需要创建任何类型的汽车了。
'''

# 4.7 自定义工作流程
'''
在组织大型项目的代码方面，Python 提供了很多选项。熟悉这些选项很重要，
这样才能确定哪种项目组织方式是最佳的，并能理解别人开发的项目。
一开始应让代码结构尽可能简单。先尽可能在一个文件中完成所有的工作，确定一切都能正确运行后，
再将类转移到独立的模块中。如果喜欢在模块和文件的交互方式，可在项目开始时就尝试将类存储到模块中。
想找出能够编写出可行代码的方式，在尝试让代码更有组织有序。
'''


# 5. Python 标准库
'''
Python 标准库 是一组模块，安装的 Python 都包含它。
'''


# 6. 类编码风格
'''
类名采用驼峰命名法。实例名和模块名都采用小写格式，并在单词之间加上划线
每个类都应紧跟在类定义后面包含一个文档字符串。这个文档字符串简要地描述类的功能，
并遵循写函数文档字符串时采用的格式约定。
每个模块也都应包含一个文档字符串，对其中的类可用于做什么进行描述。

可使用空行还组织代码，但不要滥用。在类中，可使用一个空行来分隔方法；而在模块中，可使用两个空行来分隔类。

需要同时导入标准库中的模块和自己编写的模块时，先编写导入标准模块的 import 语句
再添加一行空格，然后编写导入自己编写的模块的 import 语句。
在包含多条 import 语句的程序中，这种做法让人容易明白程序使用的各个木块来自何方
'''










