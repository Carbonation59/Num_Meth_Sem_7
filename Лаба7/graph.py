import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

file = open("info1.txt", "r");
#file = open("info2.txt", "r");
#file = open("info3.txt", "r");
lines = file.readlines()

size = [int(x) for x in lines[0].split()]
x = [float(x) for x in lines[1].split()]
t = [float(x) for x in lines[2].split()]


data = np.array([[float(x) for x in line.split()] for line in lines[3:]]).reshape(-1,size[0], size[1])
file.close()
f, ax = plt.subplots(1, 2)
# ax = fig.add_subplot(111, projection='3d')
a = ["real",
     "simp_iter_method", "zeidel_method", "simp_iter_method_relax"]

cl = ["red",
     "orange", "black", "pink"]
for i, d in enumerate(data):
        #if(a[i] != "simp_iter_method"):
            ax[1].plot(x, d[340,:], c=cl[i], label=a[i])



file = open("info11.txt", "r");
lines = file.readlines()

t = [float(x) for x in lines[0].split()]

A1 = [float(x) for x in lines[1].split()]
ax[0].plot(t, A1, c=cl[1], label=a[1])

A1 = [float(x) for x in lines[2].split()]
ax[0].plot(t, A1, c=cl[2], label=a[2])

A1 = [float(x) for x in lines[1].split()]
ax[0].plot(t, A1, c=cl[3], label=a[3])


ax[0].set_title('Error')
ax[0].legend()
ax[1].set_title('U(t,x) / U(t,y), t = const')
ax[1].legend()
plt.show()
