
from abc import ABC, abstractmethod

class Iterator(ABC):
    
    def __init__(self, items = None):
        self._current_index = 0
        self._items = items
    
    @abstractmethod
    def has_next(self):
        pass
    
    @abstractmethod
    def next(self):
        pass
    
    @abstractmethod
    def reset(self):
        pass