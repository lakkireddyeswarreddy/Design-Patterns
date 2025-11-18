
class DVDPlayer:
    
    def __init__(self):
        self._power = False
        self._disk = None
    
    def power_on(self):
        if not self._power:
            self._power = True
            print("DVD powered on successfully.")
            
    def power_off(self):
        self._power = False
        print("DVD powered off successfully.")
        
    def start(self):
        print("you have started watching")
    
    def stop(self):
        print("you have stopped watching")
    
    def inser_disk(self, disk:str):
        print(f"Inserted disk {disk} successfully")
        
    def remove_disk(self):
        print(f"Removed disk {self._disk} successfully")