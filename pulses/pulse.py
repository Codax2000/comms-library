'''
Defines the Pulse abstract class
'''
from abc import ABC, abstractmethod
from utils import *
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
        self._period = period
        self._data = None
    
    def modulate(self, data):
        print('Modulation not done yet')
        # generate data stream, assuming data is complex array
        # nfft = self._wave.shape
        # dataf = np.ones(nfft)
        # pulse_fft = np.fft(self._wave)
        # f =  # TODO: add frequency range
        # df = 2 * self._fs / nfft
        # for i in range(data.shape[0]):
        #     dataf += data[i] * np.exp(-1j * np.pi * f * (i) * self._period)
        # sf = dataf * pulse_fft
        # signal_time = np.fft.ifft(sf) / df
        # for mixer in self._mixers:
        #     print("TODO: Mixing not implemented yet")
        # return signal_time
    

    def plot(self, ax=None, n_pulses=5):
        t = np.arange(0, n_pulses*np.floor(self._fs * self._period)) / self._fs
        if ax is None:
            fig, (ax_time, ax_fft) = plt.subplots(2, 1)
        else:
            fig = ax.figure
            (ax_time, ax_fft) = ax
        t_slice = np.arange(n_pulses * np.floor(self._fs * self._period).astype(int))
        ax_time.plot(t, self._data[t_slice])

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
            ax_fft.set_ylabel('PSD $ V^2/Hz $')
        return fig