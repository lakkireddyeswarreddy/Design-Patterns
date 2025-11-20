
from media_player_state import MediaPlayerState

class PlayingState(MediaPlayerState):
    
    def __init__(self, song_name):
        self._song_name = song_name
        
    def play(self):
        print(f"Started playing song : {self._song_name}")
        
    def pause(self):
        print("No song is playing currently.")
        
    def stop(self):
        print("No song is playing currently.")
        
    def resume(self):
        raise Exception("You are currently playing song")