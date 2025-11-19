
class WeatherStation:
    
    def __init__(self):
        self._observers = list()
        self._temperature = 27.1
        
    def add_observer(self, observer):
        self._observers.append(observer)
        
    def remove_observer(self, observer):
        self._observers.remove(observer)
        
    def notify_observers(self):
        for observer in self._observers:
            observer.notify(self._temperature)
            
    def update_temperature(self, temp):
        print(f"Temperature changed from {self._temperature} C to {temp} C")
        self._temperature = temp
        self.notify_observers()