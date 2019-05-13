#coding=utf-8

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 只要程序处于活动状态，就不断地布朗运动
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(5000)
    rw.direction_choice = [-1, 1]
    rw.distance_choice = list(range(0, 9))
    rw.fill_walk()

    # 设置绘图窗口尺寸
    plt.figure(dpi=100, figsize=(19.24, 10.8))
    line_width = 2
    plt.plot(rw.x_values, rw.y_values, linewidth=line_width)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break