
class SoundSystem:
    
    def __init__(self):
        self._power = False
        self._volume = 1
        
    def power_on(self):
        if not self._power:
            self._power = True
            print("Sound System powered on successfully..")
            
    def power_off(self):
        self._power = False
        print("Sound System powered off successfully..")
        
    def volume_up(self):
        self._volume+=1
        print("Volume increased by 1 successfully.")
        
    def volume_down(self):
        self._volume-=1
        print("Volume decreased by 1 successfully.")