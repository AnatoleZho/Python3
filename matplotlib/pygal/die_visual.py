from die import Die
import pygal

'''
# 创建一个 D6
die = Die()

# 掷几次骰子， 并将结果存储在一个列表中
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# print(results)

# 分析结果
'''
# 创建了空列表frequencies ，用于存储每种点数出现的次数。遍历可能的点数(这里为1~6),
# 计算每种点数在results 中出现了多少次，并将这个值附加到列表frequencies 的末尾
'''
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)


# 绘制直方图
hist = pygal.Bar()

hist.title = 'Results of rolling one D6 1000 times.'
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = 'Reslut'
hist.y_title = 'Frequency of Result'

# 将一系列值添加到图表中
hist.add('D6', frequencies)

hist.render_to_file('dice_visual_1.svg')
'''




# 创建两个骰子
die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frquencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result + 1):
    frequency = results.count(value)
    frquencies.append(frequency)

# 可视化结果
hist = pygal.Bar()

hist.title = 'Results of rolling two D6 dice 1000 times.'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6', frquencies)
hist.render_to_file('dice_visual_2.svg')


# 创建两个不同骰子
die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(5000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frquencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result + 1):
    frequency = results.count(value)
    frquencies.append(frequency)

# 可视化结果
hist = pygal.Bar()

hist.title = 'Results of rolling a D6 and a D10  5000 times.'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',
                 '14', '15', '16']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D10', frquencies)
hist.render_to_file('dice_visual_3.svg')
