from abc import ABC, abstractmethod
import numpy as np


class ADC(ABC):

    def __init__(self, fs, period, classifiers):
        self._fs = fs
        self._period = period
        self._classifiers = classifiers
        self._data = None

    def sample(self, data, nd):
        samples = np.arange(nd, data.shape[0], self._fs * self._period)
        self._data = data[samples]
        for classifier in self._classifiers:
            classifier.classify(data[samples])

    def plot(self, ax=None):
        '''
        Plot time-domain only, don't care about 
        '''
        print("ADC Plotting not yet implemented")