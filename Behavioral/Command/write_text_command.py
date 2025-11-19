from command import Command
from receiver import Receiver

class WriteTextCommand(Command):
    
    def __init__(self, text, receiver : Receiver):
        self._receiver = receiver
        self._text = text
    
    def excute(self):
        self._receiver.write(self._text)