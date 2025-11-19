from command import Command
from receiver import Receiver

class UndoCommand(Command):
    
    def __init__(self, receiver : Receiver):
        self._receiver = receiver
        
    def excute(self):
        self._receiver.undo()