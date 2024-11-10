from receivers.receiver import Receiver

class IQReceiver(Receiver):

    def mix(self, data):
        super.mix(data)