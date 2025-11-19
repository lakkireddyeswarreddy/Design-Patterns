from observer import Observer
from weather_station import WeatherStation

class LEDBoardObserver(Observer):
    
    def __init__(self, weather_station : WeatherStation):
        super().__init__(weather_station)
        self._weather_station.add_observer(self)
        
    def notify(self, temperature):
        print(f"LED Board : Temperature changed to {temperature} C") 