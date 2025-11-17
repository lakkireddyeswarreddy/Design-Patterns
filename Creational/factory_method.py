from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
class Circle(Shape):
    
    def __init__(self,radius):
        self._radius = radius
    
    def area(self):
        return 3.14 * self._radius * self._radius
    
class Rectangle(Shape):
    
    def __init__(self, width, height):
        self._width = width
        self._height = height
        
    def area(self):
        return self._height * self._width
    
class Square(Shape):
    
    def __init__(self, side):
        self._side = side
        
    def area(self):
        return self._side * self._side
    
    
class ShapeFactory:
    
    def __init__(self, shape : Shape):
        self.shape = shape
        
    def calculate_area(self):
        print(f"Area of {self.shape.__class__.__name__} is {self.shape.area()}")
        
        
        
if __name__ == "__main__":
    
    ShapeFactory(Circle(7)).calculate_area()
    ShapeFactory(Rectangle(7,8)).calculate_area()
    ShapeFactory(Square(7)).calculate_area()
