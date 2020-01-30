import matplotlib.pyplot as plt
import numpy as np
import pickle

from pathlib import Path

pickle_file = Path(__file__).parent / "repetabilite.pkl"

ax = plt.subplot(111)
x = np.linspace(0, 10)
y = np.exp(x)
plt.plot(x, y)
with open(pickle_file, "wb") as fid:
    pickle.dump(ax, fid)

