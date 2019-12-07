import numpy as np
from matplotlib import pylab as plt
"""
x = np.array([1.749, 1.955, 2.085, 2.15, 2.194, 2.222, 2.2495, 2.278,
 2.311, 2.355, 2.436, 2.859, 2.909])
y = np.array([-81.22356, -71.7876, -59.6727, -45.5112,
 -29.69798, -17.11829, 0, 16.56562, 30.28334, 45.95076, 59.63328, 79.25148, 78.33355])

x0 = np.arange(1.749, 2.910, 0.001)
y0 = np.arctan((2 * np.pi * 1000 * x0 * 0.1 - 1 / (2 * np.pi * 1000 * x0 * 0.05 * 0.000001)) / 130.86) / np.pi * 180
plt.xlabel("frequence(KHz)")
plt.ylabel("phase difference(°)")
plt.scatter(x, y, marker="+", color="black", label="experiment data")
plt.plot(x0, y0, color='black', label='theoretical value')

plt.legend()

"""
"""
f = np.array([1.7490, 1.8, 1.955, 2, 2.085, 2.12, 2.15, 2.17, 2.194,
    2.2, 2.222, 2.24, 2.2494, 2.26, 2.278, 2.29, 2.31, 2.34, 2.355,
    2.4, 2.4360, 2.7, 2.8560, 2.9090])
uR = np.array([0.13705, 0.15434, 0.23967, 0.28711, 0.4185, 0.4757, 0.5505,
    0.6080, 0.6769, 0.6928, 0.7371, 0.7602, 0.7616, 0.7561, 0.7310, 0.7058,
    0.6548, 0.5746, 0.5367, 0.44, 0.3816, 0.18614, 0.14305, 0.13355])
iR = uR * 10
"""
plt.xlabel("frequence(kHz)")
plt.ylabel("i(mA)")
f0 = np.arange(1.749, 2.910, 0.001)
i0 = 1000 / (130.86 ** 2 + (2 * np.pi * f0 * 1000 * 0.1 - 1 / (2 * np.pi * f0 * 1000 * 0.05 * 0.000001))** 2)** 0.5
i1 = 1000 / (530.86 ** 2 + (2 * np.pi * f0 * 1000 * 0.1 - 1 / (2 * np.pi * f0 * 1000 * 0.05 * 0.000001))** 2)** 0.5

# plt.scatter(f, iR, marker="+", color="black", label="experiment data")
plt.plot(f0, i0, color='black', label='R = 100 Ω')
plt.plot(f0, i1, color='black', label='R = 500 Ω', linestyle='dashed')
plt.legend()
plt.savefig('compare.eps')
plt.show()