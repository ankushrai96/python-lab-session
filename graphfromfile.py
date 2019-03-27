import matplotlib.pyplot as plt
import numpy as np
x, y = np.loadtxt('myfile.csv', delimiter=',', unpack=True)
plt.plot(x,y)
plt.show()