from dvdplayer import DVDPlayer
from projector import Projector
from sound_system import SoundSystem


class HomeTheaterFacade:
    
    def __init__(self):
        self._dvd_player = DVDPlayer()
        self._projector = Projector()
        self._sound_system = SoundSystem()
        
    def watch_movie(self, name):
        self._projector.power_on()
        
        self._sound_system.power_on()
        
        self._sound_system.volume_up()
        
        self._dvd_player.power_on()
        
        self._dvd_player.inser_disk(name)
        
        self._dvd_player.start()
        
    def stop_movie(self):
        
        self._dvd_player.stop()
        
        self._dvd_player.remove_disk()
        
        self._dvd_player.power_off()
        
        self._sound_system.power_off()
        
        self._projector.power_off()
        
    