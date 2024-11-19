from abc import ABC, abstractmethod
from numpy.fft import fft, ifft, fftshift
from utils import *
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

    def mix(self, data):
        t = np.arange(len(data)) / self._fs
        mult = np.sqrt(2 / self._period)
        cos_branch = mult * np.cos(2 * np.pi * self._fc * t) * np.real(data)
        sin_branch = mult * np.sin(2 * np.pi * self._fc * t) * np.imag(data)
        self._data = np.real(cos_branch + sin_branch)
        for channel in self._channels:
            channel.distort(self._data)
    
    def plot(self, n_pulses=5, ax=None):
        if ax is None:
            fig, (ax_time, ax_fft) = plt.subplots(2, 1)
        else:
            fig = ax.figure
            (ax_time, ax_fft) = ax
        max_time = n_pulses * self._period
        t = np.arange(self._data.shape[0]) / self._fs
        filt = t < max_time
        t_plot = t[filt]
        data_plot = self._data[filt]
        ax_time.plot(t_plot, np.real(data_plot))
        psd, freq = fft_psd(self._data, self._fs)
        set_xlim = ax is None
        plot_psd(psd, freq, ax_fft)

        if set_xlim:
            ax_time.set_xlabel('Time [s]')
            ax_time.set_ylabel('Amplitude [V]')
            ax_time.set_title('Mixed Waveforms')
            ax_fft.set_xlabel('Frequency [Hz]')
            ax_fft.set_ylabel('PSD [dB/Hz]')

            # deal with axis limits
            max_yval = 10 * np.log10(np.max(psd))
            ax_fft.set_ylim(max_yval - 50, np.max([0, max_yval + 6]))
            freq_limit = 4 / self._period
            ax_fft.set_xlim(-freq_limit - self._fc, freq_limit + self._fc)
        return fig