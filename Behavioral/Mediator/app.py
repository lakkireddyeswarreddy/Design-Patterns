
from control_room import ControlRoom
from commercial_aircraft import CommercialAircraft
from cargo_aircraft import CargoAircraft
from private_aircraft import PrivateAircraft

if __name__ == "__main__":
    
    control_room = ControlRoom(2)
    commercial_flight1 = CommercialAircraft("COF23", control_room, 85.083654, 78.934764)
    cargo_flight1 = CargoAircraft("CF56",control_room, 97.46444, 67.7345473, is_landed=False, altitude=800)
    cargo_flight2 = CargoAircraft("CF757",control_room, 45.46444, 24.7345473)
    private_flight = PrivateAircraft("PF87", control_room, 85.93474,64.9373)
    
    cargo_flight2.request_landing()
    cargo_flight2.send_position()
    cargo_flight2.send_message("weather turbulence ahead")
    cargo_flight1.request_takeoff()
    commercial_flight1.request_takeoff()
    private_flight.request_takeoff()
    