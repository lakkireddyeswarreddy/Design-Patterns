"""
Facade pattern is used to provide a interface where we have complex set of sub systems, and interacting with each subsystem is very complex.
Facade pattern provides a interface that makes communicating with the subssystems easier, without knowing the internal details of the subsystems.

"""
from home_theater_facade import HomeTheaterFacade

if __name__ == "__main__":
    
    home_theater = HomeTheaterFacade()
    home_theater.watch_movie("Varanasi")
    home_theater.stop_movie()