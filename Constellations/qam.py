import numpy as np
from constellation import Constellation


class QAM(Constellation):

    def __init__(amplitude, number, pulses, classifiers):
        if np.mod(np.log2(number), 2) != 0:
            raise ValueError("number must be an even power of 2")
        n = np.sqrt(number)
        a = np.linspace(0, 2*(n - 1), n).reshape((1, n))
        a = a - np.mean(a)
        a_iq = a + 1j * a.T
        a_iq = a_iq.reshape((number, 1))
        a_q = np.imag(a_iq)
        a_i = np.real(a_iq)
        constellation = np.hstack((a_i, a_q))
        super.__init__(pulses, classifiers, constellation)