from filter import Filter
import numpy as np
import matplotlib.pyplot as plt


class SquareFilter(Filter):

    def __init__(self, fs, period, amplitude, converters):
        waveform = np.zeros((1, 2 * fs * period))
        n_samples_one = 1 + np.arange(np.floor(fs * period).astype(int))
        waveform[n_samples_one] = amplitude
        super.__init__(waveform, fs, period, converters)