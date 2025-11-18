from abc import ABC, abstractmethod
from pizza import Pizza

class BaseDecorator(ABC):
    
    def __init__(self, pizza : Pizza):
        self._pizza = pizza
    
    @abstractmethod
    def cost(self):
        pass
    
    def description(self):
        pass
    
    