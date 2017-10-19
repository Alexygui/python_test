import pygal

from pygal_test.die import Die

# 创建一个Die实例
die_1 = Die()
die_2 = Die()

# 骰子几次骰子，并将结果保存在列表中
results = []
for roll in range(12000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# print(results)

# 分析结果
frequencies = []
max_result = die_1.num_sides * 2
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
x_lables = []
for v in range(2, max_result + 1):
    x_lables.append(v)
hist.x_labels = x_lables
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6", frequencies)
hist.render_to_file('die_svg.svg')
