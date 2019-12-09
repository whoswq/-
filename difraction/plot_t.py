import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

f = open("experiment data/t_11716.txt", mode="r")
lines = f.readlines()
f.close()
i = np.array([])
x = np.array([])

for s in lines:
    i0 = int(s.split()[1])
    x0 = float(s.split()[0])
    i = np.append(i, i0)
    x = np.append(x, x0)


def func_d(x, a, d, I):
    s_theta = (x - 33.6501) / ((x - 33.6501)**2 + 658**2)**0.5
    u = np.pi * a * s_theta / 632.8 * 10 ** 3
    beta = np.pi * d * s_theta / 632.8 * 10 ** 3
    return I * (np.sin(u) / u)**(2) * (np.sin(3 * beta) / np.sin(beta))**(2)


guess = [40, 100, 4000]
para, _ = curve_fit(func_d, x, i, guess)
a0, d0, I0 = para
i_s_f = func_d(x[1000:-1000], a0, d0, I0)
print(para)


ax1 = plt.subplot(2, 1, 1)
ax2 = plt.subplot(2, 1, 2)

plt.sca(ax1)
plt.plot(x[1000:-1000], i[1000:-1000], color="black", linestyle="--",
         label="experiment data", linewidth=1)  # 绘制原始数据图像
plt.plot(x[1000:-1000], i_s_f, color="black", linewidth=0.8,
         label="optimized curve")
plt.legend()
plt.ylabel("light intensity")

plt.sca(ax2)
# 由于绘制残差图
e = i_s_f - i[1000:-1000]
plt.plot(x[1000:-1000], e, color='black', label='err', linewidth=0.7)
plt.legend()
plt.xlabel("coordinate(mm)")
plt.ylabel("")
plt.axhline(y=0, ls="--", c="black", linewidth=0.7)  # 显示一个水平的参考线
plt.savefig("image\\triple_fit.eps")
plt.show()
