import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

f = open("1.txt", mode="r")
# 第一个参数是你要打开的文件，可以使用相对路径
lines = f.readlines()
f.close()
i = np.array([])
x = np.array([])

for s in lines:
    i0 = int(s.split()[1])
    x0 = float(s.split()[0])
    i = np.append(i, i0)
    x = np.append(x, x0)

"""
用于隐藏顶部与右侧的坐标轴
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
"""


# plt.legend() # 用于显示图例

xm = [18.950, 13.690, 24.080]
ym = [2893, 148, 156]


"""
用于绘制特殊点
plt.scatter(xm, ym, color="black", marker="x")
plt.annotate("(18.950, 2893)", xy=(18.950, 2893), xytext=(15.950, 2953))
plt.annotate("(13.690, 148)", xy=(13.690, 148), xytext=(9.690, 220))
plt.annotate("(24.080, 156)", xy=(24.080, 156), xytext=(22.080, 230))
plt.savefig("image\\single_original.eps")
plt.show()
"""


def func_s(x, a, I):
    """
    x: 自变量
    a: 狭缝宽度-参数 单位是微米
    I: 最大光强-参数
    x减去的是最大光强处的坐标，稍微改动就可以避免分母为零
    """
    u = np.pi * a * ((x - 11.996) / 663) / 632.8 * 10 ** 3
    return I * (np.sin(u) / u)**(2)


guess = [100, 3000]
para, _ = curve_fit(func_s, x, i, guess)
a0, I0 = para  # 最终得到的拟合后的参数
print(para)
i_s_f = func_s(x[460:], a0, I0)  # 拟合后的光强，这里为了让图像对称只选取了部分数据


ax1 = plt.subplot(2, 1, 1)
ax2 = plt.subplot(2, 1, 2)

plt.sca(ax1)
plt.plot(x[460:], i[460:], color="black", linestyle="--",
         label="experiment data", linewidth=1)  # 绘制原始数据图像
plt.plot(x[460:], i_s_f, color="black", linewidth=0.8, label="optimized curve")
plt.legend()
plt.ylabel("light intensity")

plt.sca(ax2)
# 由于绘制残差图
e = i_s_f - i[460:]
plt.plot(x[460:], e, color='black', label='err', linewidth=0.7)
plt.legend()
plt.xlabel("coordinate(mm)")
plt.ylabel("")
plt.axhline(y=0, ls="--", c="black", linewidth=0.6)  # 显示一个水平的参考线
plt.savefig("Single_fit.eps")  # 想要保存的文件名称
plt.show()
