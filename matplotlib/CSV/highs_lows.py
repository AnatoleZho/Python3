'''
要在文本文件中存储数据，最简单的方式是将数据作为一系列以逗号分隔的值（Comma-Separated Values，CSV）
这样的文件成为 CSV 文件
'''


'''下载数据'''

# 1. CSV 文件格式
# 1.1 分析 CSV 文件头
import csv

from matplotlib import pyplot as plt

from  datetime import datetime


filename = 'sitka_weather_07-2014.csv'
with open(filename) as file_object:
    # 创建文件阅读器对象
    reader = csv.reader(file_object)
    # 返回文件第一行
    header_row = next(reader)
    print(header_row)


# 1.2 打印文件头及其位置

with open(filename) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)
    # 获取每个元素的索引及其值
    for index, column_header in enumerate(header_row):
        print(index, column_header)


# 1.3 提取并读取数据

with open(filename) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)

    ''''
    创建了一个名为highs 的空列表(见❶)，再遍历文件中余下的各行(见❷)。阅读器对象从其停留的地
    方继续往下读取CSV文件，每次都自动返回当前所处位置的下一 行。由于我们已经读取了文件头行，
    这个循环将从第二行开始——从这行开始包含的是实际数据。每次执行该循环时，我们都将索引1处
    (第2列)的数据附加到highs 末尾
    '''
    highs = []
    for row in  reader:
        # 转成 int 类型
        high = int(row[1])
        highs.append(high)

    print(highs)


# 1.4 绘制气温图表

# 根据数据绘制图形
'''
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')

# 设置图形的格式
plt.title('Daily high temperatures, July 2014', fontdict={'fontsize': 24})
plt.xlabel('', fontdict={'fontsize': 16})
plt.ylabel('Temperature (F)', fontdict={'fontsize': 16})
plt.tick_params(axis='both', which='major', labelsize='16')

plt.show()

'''


# 1.5 模块 datetime
first_date = datetime.strptime('2014-7-1', '%Y-%m-%d')
print(first_date)

'''
with open(filename) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)

    dates = []
    highs = []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        print(current_date)
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

print(dates)
print(highs)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')

# 设置图形的格式
plt.title('Daily high temperatures, July 2014', fontdict={'fontsize': 24})
plt.xlabel('', fontdict={'fontsize': 16})

fig.autofmt_xdate()

plt.ylabel('Temperature (F)', fontdict={'fontsize': 16})
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

'''



# 1.7 涵盖更长的时间

'''
filename = 'sitka_weather_2014.csv'

with open(filename) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)

    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')

plt.title('Daily high temperatures - 2014', fontdict={'fontsize': 24})
plt.xlabel('', fontdict={'fontsize': 16})
# 绘制斜的日期标签，一面出现重叠
fig.autofmt_xdate()

plt.ylabel('Temperature (F)', fontdict={'fontsize': 16})
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

'''


# 1.8 再绘制一个数据系列
filename = 'sitka_weather_2014.csv'

with open(filename) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)
'''
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')

plt.title('Daily high and low temperatures - 2014', fontdict={'fontsize': 24})
plt.xlabel('', fontdict={'fontsize': 16})
# 绘制斜的日期标签，一面出现重叠
fig.autofmt_xdate()

plt.ylabel('Temperature (F)', fontdict={'fontsize': 16})
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
'''



# 1.9 给图表区域着色
'''
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')

plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.3)

plt.title('Daily high and low temperatures - 2014', fontdict={'fontsize': 24})
plt.xlabel('', fontdict={'fontsize': 16})
# 绘制斜的日期标签，一面出现重叠
fig.autofmt_xdate()

plt.ylabel('Temperature (F)', fontdict={'fontsize': 16})
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
'''


# 1.10  检查错误
filename = 'death_valley_2014.csv'

with open(filename) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')

plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.3)

plt.title('Daily high and low temperatures - 2014\nDeath Valley, CA', fontdict={'fontsize': 24})
plt.xlabel('', fontdict={'fontsize': 16})
# 绘制斜的日期标签，一面出现重叠
fig.autofmt_xdate()

plt.ylabel('Temperature (F)', fontdict={'fontsize': 16})
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
















