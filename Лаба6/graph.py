import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

file = open("info.txt", "r");
lines = file.readlines()

size = [int(x) for x in lines[0].split()]
x = [float(x) for x in lines[1].split()]
t = [float(x) for x in lines[2].split()]


data = np.array([[float(x) for x in line.split()] for line in lines[3:]]).reshape(-1,size[0], size[1])
file.close()
f, ax = plt.subplots(1, 2)
# ax = fig.add_subplot(111, projection='3d')
a = ["real",
     "explicit_2_1(h)", "explicit_2_2(h)", "explicit_3_1(h^2)", "explicit_3_2(h^2)", "explicit_2_1(h^2)", "explicit_2_2(h^2)",
     "implicit_2_1(h)", "implicit_2_2(h)", "implicit_3_1(h^2)", "implicit_3_2(h^2)", "implicit_2_1(h^2)", "implicit_2_2(h^2)"]
for i, d in enumerate(data):
    #if(a[i] == "explicit_2_1(h)" or a[i] == "explicit_2_2(h)" or a[i] == "explicit_3_1(h^2)" or a[i] == "explicit_3_2(h^2)"or a[i] == "explicit_2_1(h^2)" or a[i] == "explicit_2_2(h^2)"):
        cl = np.random.rand(3,)
        ax[1].plot(x, d[1000,:], c=cl, label=a[i])

file = open("info1.txt", "r");
lines = file.readlines()

cl = np.random.rand(3,)
A1 = [float(x) for x in lines[0].split()]
ax[0].plot(t, A1, c=cl, label=a[1])
cl = np.random.rand(3,)
A1 = [float(x) for x in lines[1].split()]
ax[0].plot(t, A1, c=cl, label=a[2])
cl = np.random.rand(3,)
A1 = [float(x) for x in lines[2].split()]
ax[0].plot(t, A1, c=cl, label=a[3])
cl = np.random.rand(3,)
A1 = [float(x) for x in lines[3].split()]
ax[0].plot(t, A1, c=cl, label=a[4])
cl = np.random.rand(3,)
A1 = [float(x) for x in lines[4].split()]
ax[0].plot(t, A1, c=cl, label=a[5])
cl = np.random.rand(3,)
A1 = [float(x) for x in lines[5].split()]
ax[0].plot(t, A1, c=cl, label=a[6])
cl = np.random.rand(3,)
A1 = [float(x) for x in lines[6].split()]
ax[0].plot(t, A1, c=cl, label=a[7])
cl = np.random.rand(3,)
A1 = [float(x) for x in lines[7].split()]
ax[0].plot(t, A1, c=cl, label=a[8])
cl = np.random.rand(3,)
A1 = [float(x) for x in lines[8].split()]
ax[0].plot(t, A1, c=cl, label=a[9])
cl = np.random.rand(3,)
A1 = [float(x) for x in lines[9].split()]
ax[0].plot(t, A1, c=cl, label=a[10])
cl = np.random.rand(3,)
A1 = [float(x) for x in lines[10].split()]
ax[0].plot(t, A1, c=cl, label=a[11])
cl = np.random.rand(3,)
A1 = [float(x) for x in lines[11].split()]
ax[0].plot(t, A1, c=cl, label=a[12])

ax[0].set_title('Loss')
ax[0].legend()
ax[1].set_title('U(t,x), t = const')
ax[1].legend()
plt.show()
