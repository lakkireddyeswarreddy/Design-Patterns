from abc import ABC, abstractmethod

class FileSystem(ABC):
    
    @abstractmethod
    def get_size():
        pass
    
    @abstractmethod
    def display(indent):
        pass