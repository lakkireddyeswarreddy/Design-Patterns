
from abc import ABC, abstractmethod

class Compression(ABC):
    
    @abstractmethod
    def compress(self, file):
        pass