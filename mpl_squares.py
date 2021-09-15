import matplotlib.pyplot as plt

input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
# 尝试根据这些数字绘制出有意义的图形
# lineheight决定了plot()绘制的线条粗细
plt.plot(input_value,squares, linewidth=5)
# 打开matplotlib查看器 并显示绘制的图形

# 设置图标标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis="both", labelsize=14)
plt.show()
