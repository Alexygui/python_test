import matplotlib.pyplot as plt

# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
# plt.scatter(input_values, squares, s=200)
#
# plt.tick_params(axis='both', which='major', labelsize=15)


x_values = list(range(1, 100))
y_values = [x ** 2 for x in x_values]
plt.scatter(x_values, y_values, s=10)

plt.axis([0, 150, 1, 15000])

plt.show()
