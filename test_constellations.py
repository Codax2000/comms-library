from constellations.psk import PSK
from constellations.ask import ASK
from constellations.qam import QAM
import matplotlib.pyplot as plt
import pdb


def main():
    fs = 64  # fs is samples per second, not samples per symbol
    period = 0.25
    psk8 = PSK(3, 8, list(), list())
    ask4 = ASK(2, 4, list(), list())
    qam16 = QAM(16, list(), list())
    fig, ax = plt.subplots(3, 1)
    psk8.plot(ax[0])
    ask4.plot(ax[1])
    qam16.plot(ax[2])
    plt.show()


if __name__ == '__main__':
    main()