from classifier import Classifier
import numpy as np
import matplotlib.pyplot as plt


class IQClassifier(Classifier):

    def __init__(self, constellation=None):
        self._constellation = constellation
        self._data = None

    def classify(self, data):
        self._received_data = data
        ideal_data = self._constellation._constellation[0] + \
            1j * self._constellation._constellation[1]
        diff = np.abs(data - ideal_data)  # 2D matrix 
        print("Minimum distance lookup not yet finished")
        # TODO: need to set self._data as indices
    
    def plot(self, ax=None):
        '''
        Plot received signal and constellation on the same plot
        '''
        if ax is None:
            fig, ax = plt.subplots()
        else:
            fig = ax.figure
        self._constellation.plot(ax)
        ax.plot(np.real(self._received_data), np.imag(self._received_data))
        return fig
    
    def calculate_pes(self):
        '''
        Return the symbol error probability as a fraction
        '''
        n_incorrect = np.sum(self._data == self._constellation._data)
        n_signals = self._data.shape[0]
        return n_incorrect / n_signals

    