# from pylab import subplot, plot, grid, text, show, arange
from scipy import misc
import matplotlib.pyplot as plt
import numpy as np

ax = plt.subplot(111)


def fonction(x):
    return 3 * x * x + 2 * x + 1


x = np.arange(-2.0, 2.0, 0.01)

y = fonction(x)

plt.plot(x, y, "r-")

yp = misc.derivative(fonction, x)
# print(yp)
plt.plot(x, yp, "b-")

plt.grid(True)

ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")

plt.text(
    -0.75,
    6.0,
    r"$f(x)=3x^2+2x+1$",
    horizontalalignment="center",
    fontsize=18,
    color="red",
)

plt.text(
    -1.0, -8.0, r"$f'(x)=6x+2$", horizontalalignment="center", fontsize=18, color="blue"
)

plt.show()
