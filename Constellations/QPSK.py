import numpy as np
import matplotlib.pyplot as plt
from Constellation import Constellation

class QPSK(Constellation):

    def get_series(L=100):
        return np.sign(np.random.randn(L)) + 1j * np.sign(np.random.randn(L))
    
    def plot_constellation(self):
        xdata = np.reshape(np.array([-1, 1]), (1, 2))
        ydata = np.reshape(np.array([-1, 1]), (2, 1))
        data = xdata + ydata
        return super().plot_constellation(data, 'QPSK')