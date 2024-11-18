'''
Phase shift keying constellation
'''
from .constellation import Constellation
import numpy as np

class PSK(Constellation):

    def __init__(self, amplitude, number, pulses, classifiers):
        theta = np.linspace(0, 2 * np.pi, num = number + 1)
        theta = theta[:-1]
        I = amplitude * np.cos(theta)
        Q = amplitude * np.sim(theta)
        constellation = np.vstack((I, Q)).T
        super.__init__(pulses, classifiers, constellation)