from BPSK import BPSK
import matplotlib.pyplot as plt
import numpy as np

bpsk = BPSK()

vals = bpsk.get_series(200)
plt.scatter(np.real(vals), np.imag(vals))

bpsk.plot_constellation()
