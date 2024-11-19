from .mixer import Mixer

class IQMixer(Mixer):

    def mix(self, data):
        super().mix(data)