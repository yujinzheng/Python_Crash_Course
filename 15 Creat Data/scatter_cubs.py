#coding=utf-8

import matplotlib.pyplot as plt

x_value = list(range(1, 5001))
y_value = [x**3 for x in x_value]
# 设置颜色映射
plt.scatter(x_value, y_value, c='red', edgecolor='none', s=40)
# 设置图表标题并给坐标轴加上标签
plt.title("Cub Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cub of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)
# 设置每个坐标轴的取值范围
plt.axis([0, 5200, 0, 150000000000])
plt.show()