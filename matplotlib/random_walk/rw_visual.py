import matplotlib.pylab as plt

from random_walk import RandomWalk


# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    # 创建一个 RandomWalk 实例，并将其包含的点绘制出来
    # 增加点数
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 设置绘制窗口的尺寸
    '''
    函数figure() 用于指定图表的宽度、高度、分辨率和背景色。你需要给形参figsize 指定一个元组
    ，向matplotlib指出绘图窗口的尺寸，单位为英寸。
    '''
    plt.figure(dpi=128, figsize=(20, 12))

    points_numbers = list(range(rw.num_points))
    # 给点着色
    '''
    为根据漫步中各点的先后顺序进行着色，我们传递参数c ，并将其设置为
    一个列表，其中包含各点的先后顺序。由于这些点是按顺序绘制的，因此给参数c 
    指定的列表只需包含数字1~5000
    '''
    plt.scatter(rw.x_values, rw.y_values, c=points_numbers, cmap=plt.cm.gist_rainbow, s=5)

    # 突出起点和终点
    plt.scatter(rw.x_values[0], rw.y_values[0], c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    # plt.savefig('random_walk.png')
    keep_running = input('Make another walk? (y/n):')
    if keep_running == 'n':
        break
