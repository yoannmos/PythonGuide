import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

verts = [
    (0., 0.), # left, bottom
    (0., 2.), # left, top
    (1., 3.), # right, top
    (1., 0.), # right, bottom
    (0., 0.), # ignored
    ]

# codes = [Path.MOVETO,
#          Path.LINETO,
#          Path.LINETO,
#          Path.LINETO,
#          Path.CLOSEPOLY,
#          ]

path = Path(verts)#, codes)

fig = plt.figure()
ax = fig.add_subplot(111)
patch = patches.PathPatch(path, facecolor='orange', lw=2)
ax.add_patch(patch)
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
plt.show()