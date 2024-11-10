from abc import ABC, abstractmethod
from ..utils import DataNotGeneratedError
import numpy as np
import matplotlib.pyplot as plt


class Filter(ABC):

    def __init__(self, waveform, fs, period, converters):
        self._filt = waveform
        self._fs = fs
        self._period = period
        self._converters = converters
        self._data = None

    def filter(self, data, td):
        '''
        Assumes data is complex
        '''
        I = np.real(data)
        Q = np.imag(data)
        I_filt = np.convolve(I, self._filt)
        Q_filt = np.convolve(Q, self._filt)
        self._data = I_filt + 1j * Q_filt
        nd = 0  # TODO: change nd to number of samples to delay by when it is known
        for adc in self._converters:
            adc.sample(self._data, nd)
        return I_filt + 1j * Q_filt
    
    def plot(self, ax=None):
        if self._data is None:
            raise DataNotGeneratedError('Data must be generated before plotting')
        if ax is None:
            fig, ax = plt.subplots()
        else:
            fig = ax.figure
        print("TODO: Still need plotting functions for filter")
