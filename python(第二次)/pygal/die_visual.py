
import pygal

from die import Die

# # 创建一个 D6
# die_1 = Die()
# die_2 = Die()

# # 掷几次骰子，并将结果存储在一个列表中
# results = []
# for roll_num in range(1000):
# 	result = die_1.roll() + die_2.roll()
# 	results.append(result)

# # 分析结果
# frequencies = []
# max_result = die_1.num_sides + die_2.num_sides
# for value in range(2, max_result+1):
# 	freuency = results.count(value)
# 	frequencies.append(freuency)

# # print(frequencies)

# # 对结果进行可视化
# hist = pygal.Bar()

# hist.title = "Results of rolling one D6 1000 times."
# hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
# hist.x_title = 'Result'
# hist.y_title = "Frequency of Result"

# hist.add('D6 + D6', frequencies)
# hist.render_to_file('die_visual_2.svg')


die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(50000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
	freuency = results.count(value)
	frequencies.append(freuency)

hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 5,000 times."
hist.x_labels = list(range(2, max_result + 1))
hist.x_title = "Result"
hist.y_title = 'Frequency of Result'

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual_2.svg')















