from abc import ABC, abstractmethod


class Classifier(ABC):

    def __init__(self, constellation=None):
        self._constellation = constellation
        self._data = None
    
    @abstractmethod
    def classify(self, data):
        pass

    def plot(self, ax=None):
        '''
        Plot time-domain only, since we don't care about frequency content
        '''
        print("TODO: Implement classifier plotting")