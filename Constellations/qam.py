import numpy as np
from constellation import Constellation


class QAM4(Constellation):

    def __init__(energy, pulses, classifiers):
        a = np.sqrt(energy ** 2 / 2)
        constellation = np.array([[-a, a],
                                  [a, a],
                                  [a, -a],
                                  [-a, -a]])
        super.__init__(pulses, classifiers, constellation)