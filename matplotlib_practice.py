import matplotlib.pyplot as plt

x = [2, 4, 6, 8, 10]
y = [5, 8, 4, 5, 3]

x2 = [1, 3, 5, 9, 11]
y2 = [3, 2, 3, 5, 5]

plt.bar(x, y, label = 'bar chart 1', color = 'r')
plt.bar(x2, y2, label = 'bar chart 2', color = 'c')

plt.xlabel('x')
plt.ylabel('y')
plt.title("interesting graph\nCheck it out")
plt.legend()

plt.show()
