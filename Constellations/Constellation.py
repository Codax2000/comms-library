'''
Alex Knowlton
9/30/24

Defines a Python Interface that returns a numpy array that represents
a series of complex numbers corresponding to IQ numbers. Meant to be
extended by different objects that implement different constellations
'''
import matplotlib.pyplot as plt
import numpy as np
from abc import ABC, abstractmethod

class Constellation(ABC):
    '''
    Defines the Constellation class
    '''

    @abstractmethod
    def get_series(self, L):
        pass

    @abstractmethod
    def get_min_euclidean_distance(self):
        pass

    @abstractmethod
    def get_energy_per_bit(self):
        pass

    def plot_constellation(self, data, figname):
        plt.figure()
        x = np.real(data)
        y = np.imag(data)
        plt.xlabel('In-phase [I]')
        plt.ylabel('Quadrature [Q]')
        plt.title(f'{figname} Constellation')
        plt.grid()
        plt.scatter(x, y)
        x_lim = np.max(x) * 1.2
        y_lim = np.max(y) * 1.2
        plt.xlim([-x_lim, x_lim])
        plt.ylim([-y_lim, y_lim])
        plt.savefig(figname)
