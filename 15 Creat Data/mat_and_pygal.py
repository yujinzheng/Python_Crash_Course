#coding=utf-8

import matplotlib.pyplot as plt
from random_walk import RandomWalk
import pygal
from die import Die
import math

# 创建一个D6的实例
die = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = [die.roll() for roll_num in range(50000)]
x_value = list(range(1, die.num_sides + 1))
y_value = [results.count(value) for value in x_value]
# 设置颜色映射
plt.scatter(x_value, y_value, c='red', edgecolor='none', s=40)
# 设置图表标题并给坐标轴加上标签
plt.title("Cub Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cub of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)
# 设置每个坐标轴的取值范围
plt.axis([0, 7, 0, 50000])
plt.show()

# 创建随机漫步实例，并根据随机漫步的距离生成柱形图
rw =RandomWalk(100)
rw.fill_walk()
x_values = rw.x_values[:]
y_values = rw.y_values[:]
x_distance = []
y_distance = []
distance = []
# 提取在x方形和y方向移动的距离
for x in range(len(x_values)-1):
    x_distance.append(x_values[x+1] - x_values[x])

for y in range(len(y_values)-1):
    y_distance.append(y_values[y+1] - y_values[y])

# 算出漫步距离的平方
distance = [(x_distance[x]**2 + y_distance[x]**2) for x in range(len(x_distance))]


# 分析结果
probably_result = list(set([(x*x + y*y) for x in range(1,5) for y in range(0, 5)]))
probably_result.sort()
frequencies = [distance.count(value) for value in probably_result]
print(probably_result)
# 对结果进行可视化分析
hist = pygal.Bar()

hist.title = "Results of RandomWalk 100 times."
hist.x_labels = [str(x) for x in probably_result]
hist.x_title = "Results"
hist.y_title = "Frequency of Distance"

hist.add('Distance', frequencies)
hist.render_to_file('RandomWalk.svg')
