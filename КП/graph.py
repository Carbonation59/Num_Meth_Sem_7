import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
a = ["real", "new", "16", "8", "4"]

cl = ["red", "blue", "green", "black", "purple"]

f, ax = plt.subplots(1, 3)

file = open("info1.txt", "r");
lines = file.readlines()

t = [float(x) for x in lines[0].split()]
A1 = [float(x) for x in lines[1].split()]
ax[1].plot(t, A1, c=cl[2], label=a[2])

t = [float(x) for x in lines[2].split()]
A1 = [float(x) for x in lines[3].split()]
ax[2].plot(t, A1, c=cl[2], label=a[2])

t = [float(x) for x in lines[4].split()]
A1 = [float(x) for x in lines[5].split()]
ax[1].plot(t, A1, c=cl[3], label=a[3])

t = [float(x) for x in lines[6].split()]
A1 = [float(x) for x in lines[7].split()]
ax[2].plot(t, A1, c=cl[3], label=a[3])

t = [float(x) for x in lines[8].split()]
A1 = [float(x) for x in lines[9].split()]
ax[1].plot(t, A1, c=cl[4], label=a[4])

t = [float(x) for x in lines[10].split()]
A1 = [float(x) for x in lines[11].split()]
ax[2].plot(t, A1, c=cl[4], label=a[4])

t = [float(x) for x in lines[12].split()]
A1 = [float(x) for x in lines[13].split()]
ax[0].plot(t, A1, c=cl[0], label=a[0])

t = [float(x) for x in lines[14].split()]
A1 = [float(x) for x in lines[15].split()]
ax[0].plot(t, A1, c=cl[1], label=a[1])


ax[0].set_title('Values')
ax[0].legend()
ax[1].set_title('C')
ax[1].legend()
ax[2].set_title('D')
ax[2].legend()
plt.show()
