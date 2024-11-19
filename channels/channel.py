from abc import ABC, abstractmethod
import numpy as np
import matplotlib.pyplot as plt
from utils import *

class Channel(ABC):

    def __init__(self, receivers):
        if type(receivers) is not type([]):
            raise ValueError('receivers must be a list')
        self._receivers = receivers
        self._data = None

    def plot(self, period, fs, fc, n_pulses=5, ax=None):
        if ax is None:
            fig, (ax_time, ax_fft) = plt.subplots(2, 1)
        else:
            fig = ax.figure
            (ax_time, ax_fft) = ax
        max_time = n_pulses * period
        t = np.arange(self._data.shape[0]) / fs
        filt = t < max_time
        t_plot = t[filt]
        data_plot = self._data[filt]
        ax_time.plot(t_plot, np.real(data_plot))
        psd, freq = fft_psd(self._data, fs)
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
            freq_limit = 4 / period
            ax_fft.set_xlim(-freq_limit - fc, freq_limit + fc)
        return fig

    @abstractmethod
    def distort(self):
        pass