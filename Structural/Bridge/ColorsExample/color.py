from abc import ABC, abstractmethod

class Color(ABC):
    
    def __init__(self, name):
        self._name = name