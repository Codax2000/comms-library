import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from abc import ABC, abstractmethod

class Constellation(ABC):
    '''
    Constellation class. By default, assumes 2D data. Otherwise, override
    the plot function and get_min_euclidean_distance function.
    '''

    @abstractmethod
    def __init__(self, pulses, classifiers, constellation):
        '''
        Constellation initializer. Requires a list of pulses and a list
        of classifiers that are targets for sending data
        '''
        if type(pulses) is not type([]) or type(classifiers) is not type([]):
            raise ValueError('Inputs must be lists')
        self._pulses = pulses
        self._classifiers = classifiers
        self._constellation = constellation

    def get_rate(self):
        '''
        Returns the rate in bits per dimension
        '''
        M, d = self._constellation.shape
        return np.log2(M) / d

    def get_min_euclidean_distance(self):
        '''
        Returns minimum Euclidean distance
        '''
        I = self._constellation[:, 0]
        Q = self._constellation[:, 1]
        signals = I + 1j * Q
        diff = signals - signals.T
        d_e = np.abs(diff * diff)
        return np.min(d_e[d_e > 0])

    def get_squared_euclidean_distance(self, i1, i2, normalized=False):
        '''
        Returns the euclidean distance of the signals i1 and i2. Both i1 and
        i2 must be less than the number of signals in the constellation, M
        '''
        M = self._constellation.shape[0]
        if i1 < M:
            raise ValueError('i1 must be less than number of signals')
        if i2 < M:
            raise ValueError('i2 must be less than number of signals')
        diff = self._constellation[i1, :] - self._constellation[i2, :]
        d_E_sq = np.sum(diff * diff)
        if normalized:
            d_E_sq = d_E_sq / self.get_e_b()
        return d_E_sq

    def get_e_b(self):
        '''
        Returns energy per bit of the constellation
        '''
        M, d = self._constellation.shape
        nb = np.log2(M)
        energy = np.sum(np.power(self._constellation, 2), axis=1)
        energy_mean = np.mean(energy)
        return energy_mean / nb

    def plot(self, ax=None):
        '''
        Plots constellation in the IQ plane. If ax is given, plots on the
        given axis. Otherwise, creates a new plot. Returns the figure
        handle.
        '''
        if ax is None:
            fig, ax = plt.figure()
            x_min, x_max, y_min, y_max = self._get_plot_limits()
            ax.set_xlim(x_min, x_max)
            ax.set_ylim(y_min, y_max)
            ax.scatter(self._constellation[:, 0],
                       self._constellation[:, 1],
                       label='Constellation')
        else:
            fig = ax.figure
        ax.scatter(self._constellation[:, 0],
                   self._constellation[:, 1],
                   label='Constellation')
        ax.grid()
        ax.legend()
        return fig    
        
    def generate_data(self, length=256):
        '''
        Generates a numpy array of size (d, length), where d is the
        dimension of the constellation, and sends it to the constellation's
        associated pulse and classifier objects
        '''
        M, d = self._constellation.shape
        indices = np.random.randint(0, M, length)
        self._data = self._constellation[indices, :]
        for pulse in self._pulses:
            pulse.modulate(self._data)
        for classifier in self._classifiers:
            classifier._expected_data = self._data.copy()
        return self._data

    def _get_plot_limits(self):
        '''
        Utility function for returning the x and y limits of the constellation
        '''
        y_min = np.min(self._constellation[:, 1])
        y_max = np.max(self._constellation[:, 1])
        x_min = np.min(self._constellation[:, 1])
        x_max = np.max(self._constellation[:, 1])

        # adjust as necessary
        if y_min == y_max:
            y_min = -1
            y_max = +1
        if x_min == x_max:
            x_min = -1
            x_max = +1
        x_min -= 0.05 * np.abs(x_min)
        x_max += 0.05 * np.abs(x_max)
        y_min += 0.05 * np.abs(y_min)
        y_max += 0.05 * np.abs(y_max)
        return x_min, x_max, y_min, y_max