import matplotlib.pylab as plt


x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# 删除数据点的轮廓
# 自定义颜色
# 颜色映射 起始颜色渐变到结束颜色
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.brg, edgecolors='none', s=10)

plt.title('Square Number', fontdict={'fontsize':24})
plt.xlabel('Value', fontdict={'fontsize': 14})
plt.ylabel('Square of Value', fontdict={'fontsize': 14})

plt.tick_params(axis='both', which='major', labelsize=14)

# plt.show()
# 自动保存成图表
'''
第一个实参指定要以什么样的文件名保存图表，这个文件将存储到scatter_squares.py所在的目录中;
第二个实参指定将图表多余的空白区域裁剪掉。如果要保留图表周围多余的空 白区域，可省略这个实参。
'''
plt.savefig('squares_plot.png', bbox_inches='tight')