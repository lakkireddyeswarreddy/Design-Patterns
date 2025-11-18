
from shape import Shape
from color import Color

class Rectangle(Shape):
    
    def __init__(self, color : Color):
        super().__init__(color)
        
    def draw(self):
        print(f"Drawing  rectangle in {self._color._name}")
        
    