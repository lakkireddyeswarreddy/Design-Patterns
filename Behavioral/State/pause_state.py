from media_player_state import MediaPlayerState

class PauseState(MediaPlayerState):
    
    def __init__(self, paused_song):
        self._paused_song = paused_song
        
    def pause(self):
        print(f"Paused playing song : {self._paused_song}")
        

        
        
        
    