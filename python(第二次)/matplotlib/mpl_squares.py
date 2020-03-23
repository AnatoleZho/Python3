
# 1. matplotlib 画廊 http:matplotlib.org

import matplotlib.pyplot as plt

# 2. 绘制简单的折线图
# squares = [1, 4, 9, 16, 25]
# plt.plot(squares) # 尝试根据数字绘制出有意义的图形
# plt.show() # 打开matplotlib 查看器，并显示绘制的图形。查看器能够缩放和导航图形，单击磁盘图形保存起来


# 2.1 修改标签文字和线条粗细
# squares = [1, 4, 9, 16, 25]
# plt.plot(squares, linewidth=5)

# # 设置图表标题，并给坐标轴加上标签
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel('Value', fontsize=14)
# plt.ylabel('Square of value', fontsize=14)

# # 设置刻度标记的大小
# plt.tick_params(axis='both', labelsize=14)

# plt.show()


# 2.2 矫正图形
'''
图形更易阅读后，返现没有正确地绘制数据：折线图的终点指出4.0的平方为25！
'''

# input_values = [1, 2, 3, 4, 5]

# squares = [1, 4, 9, 16, 25]
# plt.plot(input_values, squares, linewidth=5) # 提供输入值和输出值

# # 设置图表标题，并给坐标轴加上标签
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel('Value', fontsize=14)
# plt.ylabel('Square of value', fontsize=14)

# # 设置刻度标记的大小
# plt.tick_params(axis='both', labelsize=14)

# plt.show()


# 2.3 使用 scatter() 绘制散点图并设置其样式
'''
有时候需要绘制散点图并设置各个数据点的样式。例如，可能想以一种颜色显示较小的值，
而用另一种颜色显示较大的值。绘制大型数据集时，还可以对每个点都设置同样的样式，
再使用不同的样式选项绘制某些点，以突出它们。
'''
#要绘制单个点，可使用 scatter() 函数，并向它传递一对 x 和 y 坐标，它将在指定位置绘制一个点儿

import matplotlib.pyplot as plt

# plt.scatter(2, 4)
# plt.show()

# # 下面设置输出的样式，使其更有趣：添加标题，给轴上加标签，并确保所有文本都大到能够看清：
# plt.scatter(2, 4, s=200) # 实参 s 设置了绘制图形时使用的点的尺寸 

# #  设置图表标题并给坐标轴加上标签
# plt.title('Square Numbers', fontsize=24)
# plt.xlabel('Value', fontsize=14)
# plt.ylabel('Square of Value', fontsize=14)

# # 设置刻度标记的大小
# plt.tick_params(axis='both', which='major', labelsize=14)

# plt.show()


# # 使用 scatter() 绘制一系列点
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

# plt.scatter(x_values, y_values, s=100)
# plt.title('Square Numbers', fontsize=24)
# plt.xlabel('Value', fontsize=14)
# plt.ylabel('Square of Value', fontsize=14)
# plt.tick_params(axis='both', which='major', labelsize=14)

# plt.show()


# 2.5 自动计算数据
'''
手工计算列表要包含的值可能效率低下，需要绘制点很多是有其如此。
可以不必手工计算包含点坐标的列表，而让 Python 循环来代替我们完成计算
'''
# x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]

# # plt.scatter(x_values, y_values, edgecolor='none', s=40)
# # plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)
# # plt.scatter(x_values, y_values, c=(0, 0, 0.8,), edgecolor='none', s=40)
# plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

# plt.title('Square Numbers', fontsize=24)
# plt.xlabel('Value', fontsize=14)
# plt.ylabel('Square of Value', fontsize=14)
# plt.tick_params(axis='both', which='major', labelsize=14)

# # 设置每个坐标轴的取值范围
# plt.axis([0, 1100, 0, 1100000])

# # plt.show()
# plt.savefig('squares_plot.png', bbox_inches='tight')

# 2.6 删除数据点的轮廓
'''
matplotlib 允许给散点图中的各个点指定颜色。默认为蓝色点和黑色轮廓，在散点图包含的数据点
不多时效果较好。但是绘制很多点时，黑色轮廓可能会粘连在一起。要删除数据点的轮廓，可使用
scatter() 时传递实参 edgecolor='none'
'''


# 2.7 自定义颜色
'''
要修改数据点的颜色，可向scatter() 传递参数c，并将其设置为要是用的颜色名称
plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)
plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)

'''
 

# 2.8 使用颜色映射
'''
颜色映射（colormap）是一系列颜色，它们从起始颜色渐变到结束颜色。在可视化中，颜色映射
用于突出数据规律，例如，可能用较浅的颜色来显示较小的值，并使用较深的颜色来显示较大的值。

模块 pyplot 内置了一组颜色映射。要使用这些颜色映射，需要告诉 pyplot 该如何设置数据集中
每个点的颜色。下面演示了如何根据各个点的y 值来设置其颜色：
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

将参数 c 设置成了一个 y 值列表，并使用参数 cmp 告诉 pyplot 使用哪个颜色映射。
这些代码将 y 值较小的点显示为浅蓝色，并将 y 值较大的点显示为深蓝色，生成图形
'''

# 2.9 自动保存图表
'''
要让程序自动将图表保存到文件中，可将对 plt.show() 的调用替换成对 plt.savefig() 调用
plt.savefig('squares_plot.png', bbox_inches='tight')

第一个实参指定要以什么样的文件名保存图表，这个文件将存储到 scatter_squares.py所在的目录中；
第二个参数指定将图表多于的空白区域裁减掉。如果要保留图表周围多于的空白区域，可省略这个实参
'''

# 3. 随机漫步
'''
本节将使用 Python 来生成随机漫步数据，再使用 matplotlib 以引人注目的方式将这些数据呈现出来。
随机漫步 ： 每次行走都完全随机的，没有明确的方向，结果是由一系列随机决策决定的。可以这样认为：
随机漫步就是蚂蚁在晕头转向的情况下，每次都沿随机的方向前行所经过的路径。
'''

# 3.1 创建 RandomWalk() 类
'''
为模拟随机漫步，将创建一个名为 RandomWalk 的类，它随机地选择前进的方向。这个类需要三个属性，
其中一个是存储随机漫步次数的变量，其他两个是列表，分别存储随机漫步经过的每个点的 x 和 y 坐标
'''

from random import choice
class RandomWalk():
	'''一个生成随机漫步数据的类'''

	def __init__(self, num_points=5000):
		'''初始化随机漫步的属行'''
		self.num_points = num_points

		# 所有随机漫步都始于 (0, 0)
		self.x_values = [0]
		self.y_values = [0]

	def fill_walk(self):
		'''计算随机漫步包含的所有点'''

		# 不断漫步，直到列表达到指定的长度
		while len(self.x_values) < self.num_points:
		    # 决定前进方向以及沿这个方向前进的距离
		    x_direction = choice([1, -1])
		    x_distance = choice([0, 1, 2, 3, 4])
		    x_step = x_direction * x_distance

		    y_direction = choice([1, -1])
		    y_distance = choice([0, 1, 2, 3, 4])
		    y_step = y_direction * y_distance

		    # 拒绝原地踏步
		    if x_step == 0 and y_step == 0:
		    	continue

		    # 计算下一个点的 x 和 y 值
		    next_x = self.x_values[-1] + x_step
		    next_y = self.y_values[-1] + y_step

		    self.x_values.append(next_x)
		    self.y_values.append(next_y)

'''
为做出随机决策，我们将所有可能的选择都存储在一个列表中，并在每次都决策时使用 choice() 来
决定哪种选择。接下来，将随机漫步包含的默认点数设置为 5000，这到足以生成有趣的模式，同时又
足够小，可确保能够快速地模拟随机漫步。然后创建两个英语存储 x 和 y 值的列表。并让每次漫步
都从点 (0, 0)出发
'''

# 3.2 选择方向

'''
这个方法的主要部分告诉 Python 如何模拟四种漫步决定：向左走还是向右走？沿指定的方向走多远？
向上走还是向下走？沿指定的方向走多远？

使用 choice([1, -1]) 给 x_direction 选择一个值，结果要么是表示向右走的1，要么是表示
向左走的-1. 接下来， choice([0, 1, 2, 3, 4]) 随机的选择一个 0-4 之间的整数，告诉 Python
沿指定的方向走多远（x_direction）。（通过包含0，我们不仅能够沿两个轴移动，还能沿y轴移动。）

获取漫步中下一个点的 x 值，将 x_step 与 x_values 中的最后一个值加，对于y值也做相同的处理。
获取下一个点x值和y值后，将他们分别附加到列表x_values 和 y_values的末尾。
'''

# 3.3 绘制随机漫步图
# 创建一个 RandomWalk 实例，并将其包含的点都绘制出来

# 增加点数
rw = RandomWalk(50000)
rw.fill_walk()

# 设置绘制窗口的尺寸
plt.figure(dpi=128, figsize=(10, 6))
# plt.scatter(rw.x_values, rw.y_values, s=15)
# 给点着色
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15)

# 重新绘制起始点，以表突出
plt.scatter(0, 0, c='green', edgecolor='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

# 隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()


'''
函数 figure() 用于指定图表的宽度、高度、分辨率和背景色。需要给形参figsize指定一个元组，
向matplotlib 指出绘制窗口的尺寸，单位为英寸。

Python 假定屏幕分辨率为 80像素/英寸，如果上述代码没有指定图表尺寸不合适，可根据需要调整
其中的数字。如果知道自己系统的分辨率，可使用 dpi 向 figure() 传递该分辨率，以有效地利用可用的屏幕空间
'''














