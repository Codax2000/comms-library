from constellations.psk import PSK
from pulses.square import SquarePulse
from classifiers.iq_classifier import IQClassifier
import pdb


def main():
    fs = 64
    period = 0.25
    classifier = IQClassifier()
    pulse = SquarePulse(fs, period, [])
    constellation = PSK(4, 8, [pulse])

    constellation.generate_data()
    pdb.set_trace()
    constellation.plot()
    pulse.plot_pulse()


if __name__ == '__main__':
    main()