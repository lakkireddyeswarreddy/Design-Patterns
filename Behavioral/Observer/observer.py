
from abc import ABC, abstractmethod
from weather_station import WeatherStation

class Observer(ABC):
    
    def __init__(self, weather_station : WeatherStation):
        self._weather_station = weather_station
        
    @abstractmethod
    def notify(self, temperature):
        pass
    
    