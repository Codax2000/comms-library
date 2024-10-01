import matplotlib.pyplot as plt
import numpy as np
from Constellation import Constellation


class BPSK(Constellation):
    '''
    Defines object for BPSK modulation
    '''

    def get_series(self, L=100):
        return np.sign(np.random.randn(L))
    
    def plot_constellation(self):
        super().plot_constellation(np.array([-1, 1]), 'BPSK')