from abc import ABC, abstractmethod
from color import Color

class Shape(ABC):
    
    def __init__(self, color : Color):
        self._color = color
        
    @abstractmethod
    def draw(self):
        pass