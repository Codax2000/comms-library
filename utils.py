import numpy as np
import matplotlib.pyplot as plt


def fft_psd(wave, fs):
    '''
    Returns the power spectral density of the given wave with the frequency.
    '''
    N = wave.shape[0]
    xdft = np.fft.fftshift(np.fft.fft(wave))
    psd = np.real(xdft * np.conj(xdft)) / (fs * N)
    f = np.arange(-N/2, N/2) * fs / N
    return psd, f


def plot_psd(psd, freq, ax=None):
    '''
    Plots the given psd and frequency on the given axis. If ax is None, creates
    a new figure and plots on that. Returns the handle of the Figure on which
    it is plotted
    '''
    psd_db = 10 * np.log10(psd)
    if ax is None:
        fig, ax = plt.subplots()
        ax.grid()
        ax.set_xlabel('Frequency [Hz]')
        ax.set_ylabel('PSD [dB/Hz]')
        max_y = np.max(psd_db)
        ax.set_ylim(max_y - 50, np.max([0, max_y + 5]))
    else:
        fig = ax.figure
    ax.plot(freq, psd_db)
    return fig

class DataNotGeneratedError(Exception):
    pass