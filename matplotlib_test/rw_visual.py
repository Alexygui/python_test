import matplotlib.pyplot as plt
from matplotlib_test.random_walk import RandomWalk

# 创建一个RandomWalk实例，并将其中包含的点都绘制出来
rw = RandomWalk(10000)
rw.fill_walk()

plt.figure(figsize=(16, 9))

point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, s=1, c=point_numbers, cmap=plt.cm.Blues)
plt.scatter(0, 0, c='green', s=30)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=30)

# plt.axes().get_xaxis().set_visible(False)
# plt.axes().get_yaxis().set_visible(False)

plt.show()
