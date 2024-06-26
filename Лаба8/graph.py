import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

file = open("info.txt", "r");
lines = file.readlines()
size = [int(x) for x in lines[0].split()]
t = [float(x) for x in lines[1].split()]
x = [float(x) for x in lines[2].split()]
y = [float(x) for x in lines[3].split()]
data = np.array([[float(x) for x in line.split()] for line in lines[4:]]).reshape(-1,size[0], size[1], size[2])
file.close()

# ax = fig.add_subplot(111, projection='3d')
a = ["real", "variable_directions", "fractional_step",]

# for sh in range(0,100, 10):
sh_t1 = 100
sh_x1 = 5

sh_t2 = 100
sh_y2 = 5

sh_x3 = 5
sh_y3 = 5

f1, ax1 = plt.subplots(1, 2)
f2, ax2 = plt.subplots(1, 2)
f3, ax3 = plt.subplots(1, 2)
for i, d in enumerate(data):
    # if (i == 7 or i==5 or i == 0):
        cl = np.random.rand(3,)
        if i == 1:
            cl = "red"
        elif i == 2:
            cl = "blue"
        else:
            cl = "green"

        # ax[2].plot(t, d[:,5], c=cl, label=a[i])
        ax1[1].plot(y, d[sh_t1, sh_x1, :], c=cl, label=a[i])
        ax2[1].plot(x, d[sh_t2, :, sh_y2], c=cl, label=a[i])
        ax3[1].plot(t, d[:, sh_x3, sh_y3], c=cl, label=a[i])
        if (i>0):
            ax1[0].plot(y, np.max(np.max(d-data[0], axis=0), axis=0), c=cl, label=a[i])
            ax2[0].plot(x, np.max(np.max(d-data[0], axis=2), axis=0), c=cl, label=a[i])
            razn = d-data[0]
            arr = np.zeros(size[0])
            for k in range(size[0]):
                  arr[k] = np.max(razn[k])

            ax3[0].plot(t, arr, c=cl, label=a[i])
    # ax.plot(t, d[:,size[1]-1], c=np.random.rand(3,), label=a[i])
    # ax.plot_surface(x, t, d, color=np.random.rand(3,))

ax1[1].set_title(f'k = {sh_t1}, t_k = {sh_t1*(t[1]-t[0]) :3f} i = {sh_x1}, x_i = {sh_x1*(x[1]-x[0]) :3f}')
ax1[1].legend()
ax1[0].set_title(f'Погрешность (x и t)')
ax1[0].legend()
ax2[1].set_title(f'k = {sh_t2}, t_k = {sh_t2*(t[1]-t[0]) :3f} j = {sh_y2}, y_j = {sh_y2*(y[1]-y[0]) :3f}')
ax2[1].legend()
ax2[0].set_title(f'Погрешность (y и t)')
ax2[0].legend()
ax3[1].set_title(f'i = {sh_x3}, x_i = {sh_x3*(x[1]-x[0]) :3f} j = {sh_y3}, y_j = {sh_y3*(y[1]-y[0]) :3f}')
ax3[1].legend()
ax3[0].set_title(f'Погрешность (x и y)')
ax3[0].legend()
plt.show()

# test = np.array([[[1,  2,  3],  [4,  5,  6],  [7,  8,  9]],
#                  [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
#                  [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])

# print(np.max(np.max(test, axis=1), axis=1))
# print(np.max(np.max(test, axis=2), axis=0))
# print(np.max(np.max(test, axis=0), axis=0))
