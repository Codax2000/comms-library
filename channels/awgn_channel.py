from .channel import Channel
import numpy as np


class AWGNChannel(Channel):

    def __init__(self, N0, receivers):
        self._N0 = N0
        super().__init__(receivers)

    def distort(self, data):
        sigma = np.sqrt(self._N0 / 2)
        noise = np.random.normal(0, sigma, data.shape[0])
        self._data = data + noise
        for receiver in self._receivers:
            receiver.mix(data + noise)
        return data + noise