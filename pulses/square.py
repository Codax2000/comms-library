from .pulse import Pulse
import numpy as np


class SquarePulse(Pulse):

    def __init__(self, fs, period, mixers):
        # generate data from 0 to 2*period, round up to next power of 2
        wave = np.zeros(np.floor(fs * period).astype(int))
        upper_limit = int(fs*period+1)
        wave[1:upper_limit] = 1
        super().__init__(wave, fs, period, mixers)
