#coding=utf-8

import csv
from matplotlib import pyplot as plt
from datetime import datetime

def read_file(filename):
    """用于读取文件信息的函数，返回三个列表，分别是日期，高温和低温"""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        dates, highs, lows = [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(current_date, 'missing data')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
    return dates, highs, lows

# 从文件中获取日期和最高气温
sitka_filename = 'sitka_weather_2014.csv'
death_filename = 'death_valley_2014.csv'
sitka_dates, sitka_highs, sitka_lows = read_file(sitka_filename)
death_dates, death_highs, death_lows = read_file(death_filename)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(sitka_dates, sitka_highs, c='red', alpha=0.7)
plt.plot(sitka_dates, sitka_lows, c='green', alpha=0.7)
plt.fill_between(sitka_dates, sitka_highs, sitka_lows, facecolor='blue', alpha=1)
plt.plot(death_dates, death_highs, c='red', alpha=0.2)
plt.plot(death_dates, death_lows, c='green', alpha=0.2)
plt.fill_between(death_dates, death_highs, death_lows, facecolor='blue', alpha=0.5)

# 设置图形格式
title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

