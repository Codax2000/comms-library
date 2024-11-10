'''
Contains the PSK Constellation class, does amplitude keying with M signals
'''
from constellation import Constellation
import numpy as np

class ASK(Constellation):
    '''
    Amplitude shift keying in 1 dimension
    '''

    def __init__(self, amplitude, number, pulses, classifiers):
        if np.mod(number, 2) != 0:
            raise ValueError('Number of points must be even')
        a = amplitude * np.linspace(0, 2 * (number - 1), num=number)
        a = a - np.mean(a)
        q = np.zeros((number, 1))
        constellation = np.hstack((a.reshape((number, 1)), q))
        super.__init__(pulses, classifiers, constellation)