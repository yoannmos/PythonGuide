
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(start=0, stop=np.pi, num=101)
y = np.sin(2*x)

# plt.figure()
plt.plot(x, y)
plt.show()
