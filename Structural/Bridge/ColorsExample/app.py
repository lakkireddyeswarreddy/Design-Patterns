from circle import Circle
from rectangle import Rectangle
from red import Red
from green import Green


if __name__ == "__main__":
    
    circle_obj = Circle(Red())
    circle_obj.draw()
    
    rectangle = Rectangle(Green())
    rectangle.draw()