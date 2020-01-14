from mpl_toolkits.mplot3d import Axes3D  # pylint: disable=unused-import

import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(projection="3d")

dt = [0, 1, 2, 3, 4, 5]
Ps = [3, 3.1, 3.2, 3.3, 3.4, 3.5]
Qc = [
    [0, 0.1, 0.2, 0.3, 0.4, 0.5],
    [0, 0.01, 0.02, 0.03, 0.04, 0.05],
    [0, 0.001, 0.002, 0.003, 0.004, 0.005],
    [0, 0.0001, 0.0002, 0.0003, 0.0004, 0.0005],
    [0, 0.00001, 0.00002, 0.00003, 0.00004, 0.00005],
    [0, 0.000001, 0.000002, 0.000003, 0.000004, 0.000005],
]

x = []
y = []
z = []

for px in range(len(dt)):
    for py in range(len(Ps)):
        x.append(dt[px])
        y.append(Ps[py])
        z.append(Qc[px][py])


ax.scatter(x, y, z)

plt.show()
# ax.set_xlabel("X Label")
# ax.set_ylabel("Y Label")
# ax.set_zlabel("Z Label")

