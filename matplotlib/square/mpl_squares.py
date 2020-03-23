import  matplotlib.pylab as plt

squares = [1,4,9, 16, 25]
plt.plot(squares)
plt.show()


input_values = [1, 2, 3, 4, 5]
plt.plot(input_values, squares, linewidth=5)
plt.title('Square Number', fontdict={'fontsize':24})
plt.xlabel('Value', fontdict={'fontsize':14})
plt.ylabel('Square of value', fontdict={'fontsize':14})

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.show()