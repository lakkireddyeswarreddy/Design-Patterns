from media_player_state import MediaPlayerState

class ResumeState(MediaPlayerState):
    
    def __init__(self, current_playing_song):
        self._current_playing_song = current_playing_song
        
    def resume(self):
        print(f"Resumed playing song : {self._current_playing_song}")
        

        
        
        
    