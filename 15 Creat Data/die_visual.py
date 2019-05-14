#coding=utf-8

import pygal
from die import Die

# 创建两个D6
die_1 = Die()
die_2 = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化分析
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = []
for i in range(2, 13):
    hist.x_labels.append(str(i))
hist.x_title = "Results"
hist.y_title = "Frequency of Results"

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')