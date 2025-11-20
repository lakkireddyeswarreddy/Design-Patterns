from aircraft import Aircraft

class CargoAircraft(Aircraft):
    
    def __init__(self, flight_number, control_room, latitude, longitude, is_landed=True, altitude=0):
        super().__init__(flight_number, control_room, latitude, longitude, is_landed, altitude)