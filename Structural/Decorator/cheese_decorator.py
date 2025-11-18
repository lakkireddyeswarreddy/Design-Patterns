
from base_decorator import BaseDecorator

class CheeseDecorator(BaseDecorator):

    def cost(self):
        return self._pizza.cost() + 30.00
    
    def description(self):
        return self._pizza.description() + "Extra Cheese, "