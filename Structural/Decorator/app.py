
"""
Decorator pattern is used for adding the behaviours to the object dynamically without changing the behaviours of other objects that belong to the same class.

"""
from farm_house import FarmHouse
from size_enum import Size
from cheese_decorator import CheeseDecorator
from size_decorator import SizeDecorator
from olive_decorator import OliveDecorator

if __name__ == "__main__":
    
    pizza = FarmHouse()
    pizza = SizeDecorator(pizza, Size.Medium)
    pizza = CheeseDecorator(pizza)
    pizza = OliveDecorator(pizza)
    print(pizza.cost())
    print(pizza.description())
    