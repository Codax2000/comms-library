'''
Contains the BPSK Constellation class, does binary phase-shift keying
'''
from constellation import Constellation
import numpy as np

class BPSK(Constellation):
    '''
    BPSK class
    '''

    def __init__(self, energy, pulses, classifiers):
        constellation = np.array([-energy, 0, energy, 0]).reshape((2, 2))
        super.__init__(pulses, classifiers, constellation)