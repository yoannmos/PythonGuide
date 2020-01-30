import matplotlib.pyplot as plt
import pickle

from pathlib import Path


pickle_file = Path(__file__).parent / "repetabilite.pkl"
with open(pickle_file, "rb") as fid:
    ax = pickle.load(fid)
plt.show()
