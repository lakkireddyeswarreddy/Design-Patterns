from abc import ABC, abstractmethod
from air_traffic_controller import AirTrafficController

class Aircraft(ABC):
    
    def __init__(self, flight_number, control_room : AirTrafficController, latitude, longitude, is_landed = True, altitude = 0):
        self._control_room= control_room
        self._flight_number = flight_number
        self._control_room.register_aircraft(self)
        self._is_landed = is_landed
        self._altitude = altitude
        self._runway = None
        self._latitude = latitude
        self._longitude = longitude
    
    def request_landing(self):
        self._control_room.receive_landing_clearance(self)
    
    def request_takeoff(self):
        self._control_room.receive_takeoff_clearance(self)
    
    def send_position(self):
        self._control_room.receive_position(self)
    
    def send_message(self, message):
        self._control_room.receive_warning_message(self, message)
    
    def receive_message(self, message):
        print(f"Received message from control room {self._flight_number} : {message}")
    
    def receive_landing_permission(self, runway : str):
        self._runway = runway
        self._altitude = 0
        self._is_landed =True
        print(f"Aircraft : {self._flight_number} landed successfully on {self._runway}")
        self.free_runway()
    
    def receive_takeoff_permission(self, runway : str):
        self._runway = runway
        self._altitude = 1000
        self._is_landed =False
        print(f"Aircraft : {self._flight_number} takeoff from {self._runway} successfully")
        self.free_runway()
    
    def free_runway(self):
        self._control_room.free_runway(self._runway)
        self._runway = None