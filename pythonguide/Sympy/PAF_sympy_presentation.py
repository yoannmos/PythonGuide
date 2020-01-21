from sympy import *

x, y, z = symbols("x y z")
init_printing()

sim1 = simplify(sin(x) ** 2 + cos(x) ** 2)

exp1 = expand((x + 1) ** 3)

a = 3
b = 8
c = 2
y = a * x ** 2 + b * x + c

plot(y)

solveset(y)

dy = y.diff(x)

plot(dy)

iy = integrate(y, x)

plot(iy)
