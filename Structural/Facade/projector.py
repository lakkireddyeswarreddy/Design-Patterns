
class Projector:
    
    def __init__(self):
        self._power = False
        
    def power_on(self):
        if not self._power:
            self._power = True
            print("Projector powered on successfully..")
            
    def power_off(self):
        self._power = False
        print("Projector powered off successfully..")