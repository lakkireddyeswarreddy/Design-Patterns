
from base_decorator import BaseDecorator

class SizeDecorator(BaseDecorator):
    
    def __init__(self, pizza, size):
        super().__init__(pizza)
        self._size = size

    def cost(self):
        return self._pizza.cost() + self._size.value
    
    def description(self):
        return self._pizza.description() + str(self._size.name) + " ,"