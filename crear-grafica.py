
import matplotlib.pyplot as plt
import sys

x_list = []
y_list = []
for line in open(sys.argv[1]):
	x, y = line.split()
	x = int(x)
	y = float(y)
	x_list.append(x)
	y_list.append(y)

plt.scatter(x_list, y_list)
plt.show()
