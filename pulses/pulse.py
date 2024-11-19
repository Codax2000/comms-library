'''
Defines the Pulse abstract class
'''
from abc import ABC, abstractmethod
from utils import *
import matplotlib.pyplot as plt
import numpy as np
import pdb


class Pulse(ABC):

    @abstractmethod
    def __init__(self, wave, fs, period, mixers):
        if type(mixers) is not type([]):
            raise ValueError('mixers must be a list')
        self._mixers = mixers
        self._wave = wave
        self._fs = fs
        self._period = period
        self._data = None
    
    def modulate(self, data):
        nfft = self._wave.shape[0]
        dataf = data[0] * np.ones((nfft))
        pulse_fft = np.fft.fft(self._wave)
        f = np.zeros((nfft))
        df = self._fs / nfft
        f[0:(nfft // 2)] = np.arange((nfft // 2)) * df
        f[(nfft // 2):] = np.arange((nfft // 2)) * df - self._fs / 2
        for i in range(1, data.shape[0]):
            dataf = dataf + data[i] * np.exp(-1j * 2 * np.pi * f * i * self._period)
        sf = dataf * pulse_fft
        signal_time = np.fft.ifft(sf) / df
        self._data = signal_time
        for mixer in self._mixers:
            mixer.mix(self._data.copy())
        return signal_time
    
    def plot(self, ax=None, n_pulses=5):
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
        ax_time.plot(t_plot, np.real(data_plot), label='real')
        ax_time.plot(t_plot, np.imag(data_plot), label='imag')
        psd, freq = fft_psd(self._data, self._fs)
        set_xlim = ax is None
        plot_psd(psd, freq, ax_fft)

        if set_xlim:
            ax_time.set_xlabel('Time [s]')
            ax_time.set_ylabel('Amplitude [V]')
            ax_time.set_title('Pulse Waveforms')
            ax_fft.set_xlabel('Frequency [Hz]')
            ax_fft.set_ylabel('PSD [dB/Hz]')
            ax_time.legend()

            # deal with axis limits
            max_yval = 10 * np.log10(np.max(psd))
            ax_fft.set_ylim(max_yval - 50, np.max([0, max_yval + 6]))
            freq_limit = 4 / self._period
            ax_fft.set_xlim(-freq_limit, freq_limit)
        return fig

    def plot_pulse(self, ax=None):
        '''
        Assumes ax is an array of 2 axes
        '''
        t = np.arange(0, len(self._wave)) / self._fs
        set_xlim = ax is None
        if ax is None:
            fig, (ax_time, ax_fft) = plt.subplots(2, 1)
        else:
            ax_time = ax[0]
            ax_fft = ax[1]
            fig = ax.figure
        ax_time.plot(t, self._wave)
        psd, freq = fft_psd(self._wave, self._fs)
        plot_psd(psd, freq, ax_fft)

        if set_xlim:
            ax_time.set_xlabel('Time [s]')
            ax_time.set_ylabel('Amplitude [V]')
            ax_time.set_title('Pulse Waveforms')
            ax_fft.set_xlabel('Frequency [Hz]')
            ax_fft.set_ylabel('PSD [dB/Hz]')

            # deal with axis limits
            max_yval = 10 * np.log10(np.max(psd))
            ax_fft.set_ylim(max_yval - 50, np.max([0, max_yval + 6]))
            freq_limit = 4 / self._period
            ax_fft.set_xlim(-freq_limit, freq_limit)
        return fig