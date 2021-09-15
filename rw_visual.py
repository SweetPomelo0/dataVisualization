import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:

    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(50000)
    rw.fill_walk()

    # # 隐藏坐标轴  该函数失效 反而隐藏了随机漫步
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)

    # 设置绘图窗口的尺寸
    plt.figure(dpi=128,figsize=(10,6))

    # 成功隐藏坐标轴
    current_axes = plt.axes()
    current_axes.xaxis.set_visible(False)
    current_axes.yaxis.set_visible(False)

    point_numbers = list(range(rw.num_points))
    # plt.scatter(rw.x_values, rw.y_values, s=5, c='black', edgecolors='None')
    plt.scatter(rw.x_values, rw.y_values, s=1, c=point_numbers, cmap=plt.cm.Blues, edgecolors='None')
    # 突出起点和终点
    # plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='None', s=100)



    plt.show()

    keep_running = input("Make another walk (y or n)")
    if keep_running == 'n':
        break
