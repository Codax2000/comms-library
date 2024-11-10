from abc import ABC, abstractmethod
from numpy.fft import fft, ifft, fftshift
import numpy as np
import matplotlib.pyplot as plt

class Mixer(ABC):

    def __init__(self, fs, fc, period, channels):
        if type(channels) is not type([]):
            raise ValueError('channels must be a list')
        self._fs = fs
        self._fc = fc
        self._data = None
        self._channels = channels
        self._period = period

    @abstractmethod
    def mix(self, data):
        t = np.arange(len(data)) / self._fs
        mult = np.sqrt(2 / self._period)
        cos_branch = mult * np.cos(2 * np.pi * self._fc * t) * data[0]
        sin_branch = mult * np.sin(2 * np.pi * self._fc * t) * data[1]
        self._data = cos_branch + sin_branch
        for channel in self._channels:
            channel.distort(self._data)
    
    def plot(self, ax=None):
        pass