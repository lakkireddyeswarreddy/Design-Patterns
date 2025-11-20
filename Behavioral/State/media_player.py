
from media_player_state import MediaPlayerState
from playing_state import PlayingState
from resume_state import ResumeState
from pause_state import PauseState
from stop_state import StopState
from typing import Optional

class MediaPlayer:
    
    def __init__(self):
        self._current_state = None
        
    def set_current_state(self, state : Optional[MediaPlayerState]):
        self._current_state = state
        
    def play(self):
        self._current_state.play()
        self.set_current_state(PauseState(self._current_state._song_name))
        
    def pause(self):
        self._current_state.pause()
        self.set_current_state(ResumeState(self._current_state._paused_song))
        
    def resume(self):
        self._current_state.resume()
        self.set_current_state(StopState())
        
    def stop(self):
        self._current_state.stop()
        self.set_current_state(None)