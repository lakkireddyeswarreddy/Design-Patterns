
from abc import ABC, abstractmethod

class Sender(ABC):
    
    def __init__(self, sender_type):
        self._sender_type = sender_type
        