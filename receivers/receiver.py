from abc import ABC, abstractmethod
from numpy.fft import fft, ifft, fftshift
import numpy as np
import matplotlib.pyplot as plt

class Receiver(ABC):

    def __init__(self, fs, fc, period, filters):
        if type(filters) is not type([]):
            raise ValueError('filters must be a list')
        self._fs = fs
        self._fc = fc
        self._data = None
        self._filters = filters
        self._period = period

    @abstractmethod
    def mix(self, data):
        t = np.arange(len(data)) / self._fs
        mult = np.sqrt(2 / self._period)
        cos_branch = mult * np.cos(2 * np.pi * self._fc * t) * data
        sin_branch = mult * np.sin(2 * np.pi * self._fc * t) * data
        self._data = cos_branch + sin_branch
        for filter in self._filters:
            filter.filter(cos_branch + 1j * sin_branch)
    
    def plot(self, ax=None):
        print('TODO: plotting still has to be implemented')