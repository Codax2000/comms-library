import numpy as np
import matplotlib.pyplot as plt


def fft_psd(wave, fs):
    '''
    Returns the power spectral density of the given wave with the frequency.
    '''
    nfft = wave.shape[0]
    xdft = np.fft.fftshift(np.fft.fft(wave))  # 2-sided PSD
    xdft_psd = np.power(np.abs(xdft), 2) / (nfft * fs)
    xdft_dB = 10 * np.log10(xdft_psd)
    freq = np.arange(-nfft/2, nfft/2) * fs / nfft
    return xdft_dB, freq


def plot_psd(psd, freq, ax=None):
    '''
    Plots the given psd and frequency on the given axis. If ax is None, creates
    a new figure and plots on that. Returns the handle of the Figure on which
    it is plotted
    '''
    if ax is None:
        fig, ax = plt.subplots()
        ax.grid()
    else:
        fig = ax.figure()
    ax.plot(freq, psd)
    return fig

class DataNotGeneratedError(Exception):
    pass