from bullet_type import BulletType

class Bullet:
    
    def __init__(self, x, y, speed, bullet_type):
        self._x = x
        self._y = y
        self._speed = speed
        self._bullet_type = bullet_type
        
    def fire(self):
        self._bullet_type.fire(self._x, self._y, self._speed)