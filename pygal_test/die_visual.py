import pygal

from pygal_test.die import Die

# 创建一个Die实例
die = Die()

# 骰子几次骰子，并将结果保存在列表中
results = []
for roll in range(120000):
    result = die.roll()
    results.append(result)

# print(results)

# 分析结果
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6",frequencies)
hist.render_to_file('die_svg.svg')
