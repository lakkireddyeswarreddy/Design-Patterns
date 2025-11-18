from color import Color
from shape import Shape

class Circle(Shape):
    
    def __init__(self, color : Color):
        super().__init__(color)
        
    def draw(self):
        print(f"Drawing  circle in {self._color._name}")