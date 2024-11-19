from .pulse import Pulse
import numpy as np


class SquarePulse(Pulse):

    def __init__(self, fs, period, n_pulses, mixers):
        length = 2**np.ceil(np.log2(fs * period * n_pulses)).astype(int) + 2
        if length % 2 == 1:
            length += 1
        wave = np.zeros(length)
        upper_limit = np.ceil(fs*period+1).astype(int)
        wave[1:upper_limit] = 1
        super().__init__(wave, fs, period, mixers)
