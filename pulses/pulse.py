'''
Defines the Pulse abstract class
'''
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import numpy as np


class Pulse(ABC):

    @abstractmethod
    def __init__(self, wave, fs, period, mixers):
        if type(mixers) is not type([]):
            raise ValueError('mixers must be a list')
        self._mixers = mixers
        self._wave = wave
        self._fs = fs
        self._data = None
    
    def modulate(self, data):
        pass

    def plot_signal(self, ax=None, n_pulses=5):
        pass

    def plot_pulse(self, ax=None):
        '''
        Assumes ax is an array of 2 axes
        '''
        t = np.arange(0, len(self._wave)) / self._fs
        nfft = len(self._wave)
        freq = np.arange(-nfft/2, nfft/2) * self._fs / nfft
        x_f = np.fft.fft(self._wave) / nfft
        x_f = x_f * np.conj(x_f) / self._period  # get power spectral density
        x_f_db = 10 * np.log10(x_f)
        x_f_db = np.fft.fftshift(x_f_db)
        set_xlim = ax is None
        if ax is None:
            fig, (ax_time, ax_fft) = plt.subplots(2, 1)
        else:
            ax_time = ax[0]
            ax_fft = ax[1]
        ax_time.plot(t, self._wave)
        ax_fft.plot(freq, x_f_db)

        if set_xlim:
            ax_time.set_xlabel('Time [s]')
            ax_time.set_ylabel('Amplitude [V]')
            ax_time.set_title('Pulse Waveforms')
            ax_fft.set_xlabel('Frequency [Hz]')
            ax_fft.set_ylabel('PSD $ V^2/Hz $')
        return fig