import csv
from matplotlib import pyplot as plt

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)
    print(head_row)

    # for index, column_header in enumerate(head_row):
    #     print(index, column_header)

    highs = []
    for row in reader:
        highs.append(int(row[1]))

    print(highs)

# 根据数据绘制图形
fig = plt.figure(figsize=(16, 9))
plt.plot(highs, c='red')

# 设置图形的格式
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature(F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
