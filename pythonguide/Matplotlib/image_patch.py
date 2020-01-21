import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from matplotlib.path import Path
from matplotlib.patches import PathPatch


image_file = "Matplotlib/image.png"
image = plt.imread(image_file)

fig, ax = plt.subplots()
ax.imshow(image)
ax.axis("off")  # clear x-axis and y-axis


# And another image

w, h = 512, 512

with cbook.get_sample_data("ct.raw.gz", asfileobj=True) as datafile:
    s = datafile.read()
A = np.fromstring(s, np.uint16).astype(float).reshape((w, h))
A /= A.max()

fig, ax = plt.subplots()
extent = (0, 25, 0, 25)
# pylint: disable=maybe-no-member
im = ax.imshow(A, cmap=plt.cm.hot, origin="upper", extent=extent)
# pylint: enable=maybe-no-member

markers = [(15.9, 14.5), (16.8, 15)]
x, y = zip(*markers)
ax.plot(x, y, "o")

ax.set_title("CT density")

plt.show()
