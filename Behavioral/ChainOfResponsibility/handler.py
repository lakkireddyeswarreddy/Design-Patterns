
from abc import ABC, abstractmethod
from log_message import LogMessage

class LoggerHandler(ABC):
    
    def __init__(self):
        self._level = None
        self._next_handler = None
        
    @abstractmethod
    def handle_message(self, log_message :LogMessage):
        pass
    
    def set_next_handler(self, handler):
        self._next_handler = handler
        
        
    