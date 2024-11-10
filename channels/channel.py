from abc import ABC, abstractmethod
import numpy as np
import matplotlib.pyplot as plt

class Channel(ABC):

    def __init__(self, receivers):
        if type(receivers) is not type([]):
            raise ValueError('receivers must be a list')
        self._receivers = receivers

    def plot(self, ax=None):
        print("TODO: Implement plotting later")

    @abstractmethod
    def distort(self):
        pass