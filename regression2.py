
# https://www.kite.com/python/answers/how-to-plot-a-linear-regression-line-on-a-scatter-plot-in-python

import numpy as np
import matplotlib.pyplot as plt

data = []
for line in open("multiplicacio.data"):
    size, time = line.split()
    size = int(size)
    time = float(time)
    data.append( (size, time) )

x = np.array(list(zip(*data))[0])
y = np.array(list(zip(*data))[1])

plt.plot(x,y,'o')
m,b = np.polyfit(x,y,1)
# https://stackoverflow.com/questions/3433486/how-to-do-exponential-and-logarithmic-curve-fitting-in-python-i-found-only-poly
# m1, b1 = np.polyfit(np.log(x), y, 1)
plt.plot(x, m*x+b)
plt.show()
