from air_traffic_controller import AirTrafficController
from queue import Queue
from aircraft import Aircraft

class ControlRoom(AirTrafficController):
    
    def __init__(self, total_runways):
        self._aircrafts = list()
        self._landing_queue = Queue(maxsize=10)
        self._takeoff_queue = Queue(maxsize=10)
        self._occupied_runways = set()
        self._total_runways = total_runways
        
    def register_aircraft(self, aircraft : Aircraft):
        self._aircrafts.append(aircraft)
        print(f"Aircraft : {aircraft._flight_number} regsitered successfully.")
        
    def process_queues(self):
        
        if not self._landing_queue.empty() and len(self._occupied_runways) < self._total_runways:
            aircraft = self._landing_queue.get(timeout=5)
            for i in range(1, self._total_runways+1):
                runway = f"Runway-{i}"
                if runway not in self._occupied_runways:
                    self._occupied_runways.add(runway)
                    self.send_landing_clearance(aircraft, runway)
                    break
                
        if not self._takeoff_queue.empty() and len(self._occupied_runways) < self._total_runways:
            aircraft = self._takeoff_queue.get(timeout=5)
            for i in range(1, self._total_runways+1):
                runway = f"Runway-{i}"
                if runway not in self._occupied_runways:
                    self._occupied_runways.add(runway)
                    self.send_takeoff_clearance(aircraft, runway)
                    break
                    
    def free_runway(self, runway : str):
        self._occupied_runways.remove(runway)
        
    def send_landing_clearance(self, aircraft : Aircraft, runway : str):
        aircraft.receive_landing_permission(runway)
        
    def send_takeoff_clearance(self, aircraft : Aircraft, runway : str):
        aircraft.receive_takeoff_permission(runway)
        
    def receive_landing_clearance(self, aircraft : Aircraft):
        self._landing_queue.put_nowait(aircraft)
        self.process_queues()
    
    def receive_takeoff_clearance(self, aircraft : Aircraft):
        self._takeoff_queue.put_nowait(aircraft)
        self.process_queues()
        
    def receive_warning_message(self, aircraft : Aircraft, message : str):
        print(f"Broad casting message from {aircraft._flight_number}")
        
        for element in self._aircrafts:
            if element._flight_number != aircraft._flight_number:
                element.receive_message(message)
                
                
    def receive_position(self, aircraft : Aircraft):
        print(f"Aircraft : {aircraft._flight_number} position : latitude[{aircraft._latitude}, longitude[{aircraft._longitude}]]")