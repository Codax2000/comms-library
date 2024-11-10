from adc import ADC


class IdealADC(ADC):

    def __init__(self, fs, period, classifiers):
        super.__init__(fs, period, classifiers)