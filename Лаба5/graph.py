import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

file = open("info.txt", "r");
#file = open("info30.txt", "r");
lines = file.readlines()

size = [int(x) for x in lines[0].split()]
x = [float(x) for x in lines[1].split()]
t = [float(x) for x in lines[2].split()]


data = np.array([[float(x) for x in line.split()] for line in lines[3:]]).reshape(-1,size[0], size[1])
file.close()
f, ax = plt.subplots(1, 2)
# ax = fig.add_subplot(111, projection='3d')
a = ["real",
     "explicit_2_O(h)", "explicit_3_O(h^2)", "explicit_2_O(h^2)",
     "implicit_2_O(h)", "implicit_3_O(h^2)", "implicit_2_O(h^2)",
     "combined_2_O(h)", "combined_3_O(h^2)", "combined_2_O(h^2)"]
for i, d in enumerate(data):
    #if(a[i] == "real" or a[i] == "explicit_2_O(h)"):
    #if (a[i] == "real" or a[i] == "explicit_3_O(h^2)"):
    #if (a[i] == "real" or a[i] == "explicit_2_O(h^2)"):
    #if (a[i] == "real" or a[i] == "implicit_2_O(h)"):
    #if (a[i] == "real" or a[i] == "implicit_3_O(h^2)"):
    #if (a[i] == "real" or a[i] == "implicit_2_O(h^2)"):
    #if (a[i] == "real" or a[i] == "combined_2_O(h)"):
    #if (a[i] == "real" or a[i] == "combined_3_O(h^2)"):
    #if (a[i] == "real" or a[i] == "combined_2_O(h^2)"):
    if (a[i] != "explicit_2_O(h^2)"):

        cl = np.random.rand(3,)
        #ax[0].plot(t, d[:,5], c=cl, label=a[i])
        ax[1].plot(x, d[30,:], c=cl, label=a[i])
        # ax.plot(t, d[:,size[1]-1], c=np.random.rand(3,), label=a[i])
        # ax.plot_surface(x, t, d, color=np.random.rand(3,))

file = open("info1.txt", "r");
#file = open("info1_30.txt", "r");
lines = file.readlines()

A1 = [float(x) for x in lines[0].split()]
ax[0].plot(t, A1, c=cl, label=a[1])
A1 = [float(x) for x in lines[1].split()]
ax[0].plot(t, A1, c=cl, label=a[1])
A1 = [float(x) for x in lines[2].split()]
ax[0].plot(t, A1, c=cl, label=a[1])
A1 = [float(x) for x in lines[3].split()]
ax[0].plot(t, A1, c=cl, label=a[1])
A1 = [float(x) for x in lines[4].split()]
ax[0].plot(t, A1, c=cl, label=a[1])
A1 = [float(x) for x in lines[5].split()]
ax[0].plot(t, A1, c=cl, label=a[1])
A1 = [float(x) for x in lines[6].split()]
ax[0].plot(t, A1, c=cl, label=a[1])
A1 = [float(x) for x in lines[7].split()]
ax[0].plot(t, A1, c=cl, label=a[1])
A1 = [float(x) for x in lines[8].split()]
ax[0].plot(t, A1, c=cl, label=a[1])


ax[0].set_title('U(t,x), x = 5')
ax[0].legend()
ax[1].set_title('U(t,x), t = 500')
ax[1].legend()
plt.show()
