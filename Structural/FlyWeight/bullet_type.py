
class BulletType:
    
    def __init__(self, type, color):
        self._type = type
        self._color = color
        
    def fire(self, position_x, position_y, speed):
        print(f"{self._type} Bullet of color {self._color} was fired from({position_x},{position_y} with speed {speed})")