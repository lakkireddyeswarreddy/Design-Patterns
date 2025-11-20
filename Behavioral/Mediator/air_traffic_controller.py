
from abc import ABC, abstractmethod

class AirTrafficController(ABC):
    
    @abstractmethod
    def register_aircraft(self):
        pass
    
    @abstractmethod
    def send_landing_clearance(self):
        pass
    
    @abstractmethod
    def send_takeoff_clearance(self):
        pass
    
    @abstractmethod
    def receive_landing_clearance(self):
        pass
    
    @abstractmethod
    def receive_takeoff_clearance(self):
        pass
    
    @abstractmethod
    def receive_warning_message(self):
        pass
    
    @abstractmethod
    def receive_position(self):
        pass
    
    @abstractmethod
    def free_runway(self):
        pass