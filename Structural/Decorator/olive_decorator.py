

from base_decorator import BaseDecorator



from base_decorator import BaseDecorator

class OliveDecorator(BaseDecorator):

    def cost(self):
        return self._pizza.cost() + 30.00
    
    def description(self):
        return self._pizza.description() + "Olives."