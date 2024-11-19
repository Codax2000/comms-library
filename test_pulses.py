from constellations.qam import QAM
from pulses.square import SquarePulse
from mixers.iq_mixer import IQMixer
from channels.awgn_channel import AWGNChannel
import matplotlib.pyplot as plt
import numpy as np


def main():
    fs = 5e3  # fs is samples per second, not samples per symbol
    fc = 20  # 150 Hz carrier frequency
    period = 0.25
    amplitude = 0.25
    n_pulses = 30
    channel = AWGNChannel(1, list())
    iq_mixer = IQMixer(fs, fc, period, [channel])
    square_modulator = SquarePulse(fs, period, n_pulses, [iq_mixer])
    qam16 = QAM(amplitude, 16, [square_modulator], list())
    qam16.generate_data(n_pulses)
    square_modulator.plot()
    iq_mixer.plot()
    channel.plot(period, fs, fc)
    plt.show()


if __name__ == '__main__':
    main()