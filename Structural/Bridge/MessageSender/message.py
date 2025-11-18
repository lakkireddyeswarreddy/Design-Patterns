from abc import ABC, abstractmethod
from sender import Sender

class Message(ABC):
    
    def __init__(self, sender : Sender):
        self._sender = sender
        
    @abstractmethod
    def send(self, msg):
        pass