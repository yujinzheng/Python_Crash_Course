#coding=utf-8

import pygal
from die import Die

# 创建两个D8的骰子
die_1 = Die(8)
die_2 = Die(8)

# 掷几次骰子，并将结果存储在一个列表中
results = [(die_1.roll() + die_2.roll()) for roll_num in range(10000000)]

# 分析结果
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# 对结果进行可视化分析
hist = pygal.Bar()

hist.title = "Results of rolling two D8 50000 times."
hist.x_labels = [str(x) for x in range(2, 17)]
hist.x_title = "Results"
hist.y_title = "Frequency of Results"

hist.add('D8 + D8', frequencies)
hist.render_to_file('two_D8_dice.svg')