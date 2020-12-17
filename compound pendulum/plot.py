import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit


f = open("实验数据.txt")
lines = f.readlines()
f.close()

x = np.array([])
T = np.array([])
for i in lines:
    line = i.split()
    x0 = line[0]
    T0 = float(line[-1])
    if x0[0] == '-':
        x0 = - float(x0[1:])
    else:
        x0 = float(x0)
    x = np.append(x, x0)
    T = np.append(T, T0)


def func(x, i, g):

    m = 0.4128
    x0 = 0.00
    T = 2 * np.pi * ((i + m * ((x - x0) / 100) ** 2) / (m * g * abs(x - x0) / 100)) ** 0.5
    return T


para, _ = curve_fit(func, x, T)
i0, g0 = para
T_fit = func(x, i0, g0)
print(para)
"""
ax1 = plt.subplot(2, 1, 1)
ax2 = plt.subplot(2, 1, 2)

plt.sca(ax1)
"""

x_dot = [-27.4552, 10.8820, -10.6319, 27.3927, -20.0129, 14.8221]
y_dot = [1.24945, 1.24945, 1.24945, 1.24945, 1.19316, 1.19316]
txt = ['A', 'A\'', 'B', 'B\'', 'C', 'C\'']
plt.scatter(x_dot, y_dot, c='black', marker='x', linewidths=2)

for i in range(len(x_dot)):
    plt.annotate(txt[i], xy=(x_dot[i], y_dot[i]), xytext=(x_dot[i],
                 y_dot[i] + 0.05))

plt.plot(x[:28], T[:28], color='black', label='experiment data',
         linestyle='-', linewidth=1.0)
plt.plot(x[28:], T[28:], color='black', label='experiment data',
         linestyle='-', linewidth=1.0)
plt.xlabel("position(cm)")
plt.ylabel("cycle time(s)")
plt.hlines(1.24945, -27.4552, 27.3927, color='black',
           linestyle='--', linewidth=0.8)
plt.hlines(1.19316, -20.0912, 14.8221, color='black',
           linestyle='--', linewidth=0.8)
"""
plt.plot(x[:28], T_fit[:28], color='black', label='fit curve')
plt.plot(x[28:], T_fit[28:], color='black', label='fit curve')
plt.legend()


plt.sca(ax2)
e = T_fit - T
plt.plot(x[:28], e[:28], color='black')
plt.plot(x[28:], e[28:], color='black')
"""
plt.savefig("conjugate_point.eps")
plt.show()
